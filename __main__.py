import asyncio
import logging

from src.core.session import EosSession


async def main():
    logging.basicConfig(
        level=logging.DEBUG,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    with EosSession() as session:

        @session.on
        def camera_added(camera):
            print(camera)

        await session.run()


if __name__ == "__main__":
    asyncio.run(main())
