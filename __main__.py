import asyncio
import logging

from src.core.session import EosSession


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

        await session.run()


if __name__ == "__main__":
    asyncio.run(main())
