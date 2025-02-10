import asyncio
import io
import logging
from dataclasses import dataclass
from itertools import cycle

import cv2
import numpy as np
from cv2.typing import MatLike
from PIL import Image
from PIL.ImageFile import ImageFile
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.coordinate import Coordinate
from textual.events import Key
from textual.widgets import DataTable, Footer, Header, Input, Label

from src.cli.app import App
from src.core.camera import Camera
from src.core.session import EosSession
from src.model.caption import get_caption_for_image
from src.model.correlation import compare_images
from src.model.edge import data_in_frame_center, draw_border_lines
from src.model.feature import Objects, detect_objects, draw_object_borders

type Box = tuple[float, float, float]

log = logging.getLogger(__name__)


@dataclass
class ImageMeta:
    caption: str
    objects: Objects


class EosApp(App):
    BINDINGS = [
        Binding(key="ctrl+q", action="quit", description="Quit the app"),
        Binding(key="delete", action="delete", description="Delete the last entry"),
        Binding(key="ctrl+space", action="📷", description="📷"),
    ]

    caption_worker = asyncio.Lock()
    objects_worker = asyncio.Lock()
    last_objects: Objects | None = None

    async def caption(self, image: ImageFile):
        if self.caption_worker.locked():
            return None

        async with self.caption_worker:
            return await get_caption_for_image(image)

    async def object_signiture(self, image: ImageFile) -> Objects:
        if self.objects_worker.locked() and self.last_objects is not None:
            return self.last_objects

        async with self.objects_worker:
            objects = await detect_objects(image)
            self.objects.clear()
            # sort from big box to small box
            objects.sort(key=lambda x: (x[2], x[0]), reverse=True)

            for box, label, score in objects:
                self.objects.add_row(label, box, score)

            return objects

    async def camera_loop(self, camera: Camera):
        """ """
        async with camera:
            # By observing the change of this, we can determine when a frame has categorically changed.
            key_items: list[tuple[Box, str, float]] = []
            previous_frames: list[MatLike] = []
            img_stable = False

            async for image in camera.live_view_stream():
                pil_image = Image.open(io.BytesIO(image))
                frame = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
                if previous_frames is not None:
                    scores = await asyncio.gather(
                        *[
                            asyncio.to_thread(compare_images, last, frame)
                            for last in previous_frames
                        ]
                    )

                    if scores:
                        min_score = min(scores)

                        self.checks.update_cell_at(Coordinate(1, 2), scores[-1])

                        if min_score > 0.9:
                            img_stable = True
                        else:
                            img_stable = False

                    previous_frames.append(frame.copy())
                    if len(previous_frames) > 4:
                        previous_frames.pop(0)

                if not img_stable:
                    cv2.imshow(camera.viewfinder, frame)  # pyright: ignore
                    cv2.waitKey(1)
                    continue

                objects, data, violations_found, caption = await asyncio.gather(
                    self.object_signiture(pil_image),
                    data_in_frame_center(frame),
                    draw_border_lines(frame),
                    self.caption(pil_image),
                )

                draw_object_borders(frame, objects)

                cv2.imshow(camera.viewfinder, frame)  # pyright: ignore
                cv2.waitKey(1)

                if caption is not None:
                    self.ctx_label.update(caption)
                # Update the data being shown to the user.
                self.checks.update_cell_at(
                    Coordinate(0, 1), "✅" if not violations_found else "❌"
                )
                self.checks.update_cell_at(
                    Coordinate(1, 1), "✅" if img_stable else "⌛"
                )
                self.checks.update_cell_at(Coordinate(2, 1), "✅" if data else "❌")

    def camera_added(self, camera):
        self.notify(f"Camera found {camera.name}!")
        if hasattr(self, "camera"):
            return

        self.camera = camera
        self.session.loop.create_task(self.camera_loop(camera))

    def __init__(self, session: EosSession):
        super().__init__()
        self.session = session
        self.session.on(self.camera_added)

    def compose(self) -> ComposeResult:
        # Create a log display as a ScrollView to allow scrolling
        self.input_field_title = Input(placeholder="Type a conext here: ")
        self.input_field_date = Input(placeholder="What date is this?")

        self.objects = DataTable()
        self.objects.add_columns("Label", "Box Size", "Certainty")

        self.checks = DataTable()
        self.checks.add_columns("Check", "passing", "meta")
        self.checks.add_row("Edge Violations", "❌")
        self.checks.add_row("Stable", "❌", 0.0)
        self.checks.add_row("Frame Data", "❌")

        self.history = DataTable()
        self.ctx_label = Label("")

        with Vertical():
            yield Header(name="Film Scanner")
            with Horizontal():
                with Vertical():
                    yield self.history

                with Vertical():
                    yield self.checks
                    yield self.objects

            yield self.ctx_label
            yield self.input_field_title
            yield self.input_field_date

            yield Footer()

    async def take_photo_and_record(self):
        try:
            image = await self.camera.snap()
            self.notify("Photo Acquired!")

            # Now we want to write that data through
        except Exception as e:
            self.notify(f"Error: {e}", severity="error")

    def on_key(self, event: Key) -> None:
        if event.key == "ctrl+space":
            self.session.loop.create_task(self.take_photo_and_record())

    def on_exit(self) -> None:
        # This method is called when the app is about to exit
        print("App is exiting! Performing cleanup...")
        # Add any cleanup code here
        self.session.connected = False
