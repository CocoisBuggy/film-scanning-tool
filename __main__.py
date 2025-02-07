import asyncio
import logging

import cv2
import matplotlib.pyplot as plt  # For visualization
import numpy as np

from src.core.camera import Camera
from src.core.session import EosSession


async def camera_loop(camera: Camera):
    with camera:
        async for image in camera.stream():
            with open("test.jpg", "wb") as f:
                f.write(image)

            nparr = np.frombuffer(image, np.uint8)
            # Decode the numpy array into an image
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            cv2.imshow(camera.viewfinder, frame)

            key = cv2.waitKey(1)  # Check for key presses while updating.
            print(key)
            if key == ord("q"):  # If 'q' is pressed
                print("Quitting")
                break


async def main():
    logging.basicConfig(
        level=logging.DEBUG,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    log = logging.getLogger(__name__)

    with EosSession() as session:

        @session.on
        def camera_added(camera):
            log.info(f"discovered camera {camera.name} {camera.port}")
            session.loop.create_task(camera_loop(camera))

        await session.run()


if __name__ == "__main__":
    asyncio.run(main())
