import asyncio
import io
import logging
from itertools import cycle

import cv2
import numpy as np
from cv2.typing import MatLike
from PIL import Image
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.coordinate import Coordinate
from textual.events import Key
from textual.widgets import Button, DataTable, Footer, Header, Input, Label

from src.cli.app import App
from src.core.camera import Camera
from src.core.session import EosSession
from src.model.correlation import compare_images
from src.model.edge import data_in_frame_center, draw_border_lines
from src.model.feature import detect_objects_and_draw_boxes

type Box = tuple[float, float, float]

log = logging.getLogger(__name__)


class EosApp(App):
    BINDINGS = [
        Binding(key="ctrl+q", action="quit", description="Quit the app"),
        Binding(key="delete", action="delete", description="Delete the last context"),
        Binding(key="ctrl+space", action="📷", description="Take a photo"),
    ]

    async def camera_loop(self, camera: Camera):
        """ """
        async with camera:
            # By observing the change of this, we can determine when a frame has categorically changed.
            key_items: list[tuple[Box, str, float]] = []
            previous_frame: MatLike | None = None
            scores: list[float] = []
            img_stable = False
            data = False

            async for image in camera.live_view_stream():
                pil_image = Image.open(io.BytesIO(image))
                frame = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
                objects, data, violations_found = await asyncio.gather(
                    detect_objects_and_draw_boxes(pil_image, frame),
                    data_in_frame_center(frame),
                    draw_border_lines(frame),
                )

                cv2.imshow(camera.viewfinder, frame)  # pyright: ignore
                cv2.waitKey(1)

                # remove rows and add new data
                self.objects.clear()
                objects = [
                    (abs(b[2] - b[0]) * abs(b[3] - b[1]), label, score)
                    for b, label, score in objects
                ]
                # sort from big box to small box
                objects.sort(key=lambda x: (x[2], x[0]), reverse=True)

                for box, label, score in objects:
                    self.objects.add_row(label, box, score)

                if previous_frame is not None:
                    score = compare_images(previous_frame, frame)
                    scores.append(score)
                    if len(scores) > 20:
                        scores.pop(0)

                img_stable = sum(scores[-4:]) >= 0.95 * 4
                previous_frame = frame

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
