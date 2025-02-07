import asyncio
import logging

import cv2
import matplotlib.pyplot as plt  # For visualization
import numpy as np

from src.core.camera import Camera
from src.core.session import EosSession
from src.model.feature import detect_objects_and_draw_boxes

log = logging.getLogger(__name__)


async def camera_loop(camera: Camera):
    async with camera:
        async for image in camera.stream():
            frame = detect_objects_and_draw_boxes(image)
            cv2.imshow(camera.viewfinder, frame)

            key = cv2.waitKey(1)  # Check for key presses while updating.
            if key == ord("q"):  # If 'q' is pressed
                log.debug("cv2 recieved a quit signal")
                break


async def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    with EosSession() as session:

        @session.on
        def camera_added(camera):
            log.info(f"discovered camera {camera.name} {camera.port}")
            session.loop.create_task(camera_loop(camera))

        await session.run()


if __name__ == "__main__":
    asyncio.run(main())
