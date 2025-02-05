import asyncio
import logging

import cv2
import numpy as np

from src.core.camera import Camera
from src.core.session import EosSession


async def camera_loop(camera: Camera):
    with camera:
        async for raw_bytes in camera.stream():
            print(raw_bytes)
            # Convert the raw bytes to a numpy array
            nparr = np.frombuffer(raw_bytes, np.uint8)
            # Decode the numpy array into an image
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            cv2.imshow(camera.viewfinder, frame)


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
