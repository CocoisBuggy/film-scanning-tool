import logging
from itertools import cycle

import cv2
from cv2.typing import MatLike
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import DataTable, Footer, Header, Input, Label

from src.cli.app import App
from src.core.camera import Camera
from src.core.session import EosSession
from src.model.correlation import compare_images
from src.model.edge import draw_border_lines
from src.model.feature import detect_objects_and_draw_boxes

type Box = tuple[float, float, float]


class EosApp(App):
    async def camera_loop(self, camera: Camera):
        """ """
        async with camera:
            # By observing the change of this, we can determine when a frame has categorically changed.
            key_items: list[tuple[Box, str, float]] = []
            previous_frame: MatLike | None = None
            scores: list[float] = []
            img_stable = False

            async for image in camera.live_view_stream():
                frame, objects = detect_objects_and_draw_boxes(image)
                edge_violations = draw_border_lines(frame)
                cv2.imshow(camera.viewfinder, frame)  # pyright: ignore
                cv2.waitKey(1)  # Check for key presses while updating.

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

    def camera_added(self, camera):
        self.notify(f"Camera found {camera.name}!")
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
        self.history = DataTable()
        self.ctx_label = Label("")

        with Vertical():
            yield Header()
            with Horizontal():
                with Vertical():
                    yield self.history

                with Vertical():
                    yield self.objects

            yield self.ctx_label

            yield self.input_field_title
            yield self.input_field_date
            yield Footer()

    def on_exit(self) -> None:
        # This method is called when the app is about to exit
        print("App is exiting! Performing cleanup...")
        # Add any cleanup code here
        self.session.connected = False
