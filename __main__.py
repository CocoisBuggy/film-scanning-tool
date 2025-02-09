import asyncio
import logging

from src.cli.app import EosApp
from src.core.camera import Camera
from src.core.session import EosSession
from src.model.feature import detect_objects_and_draw_boxes

log = logging.getLogger(__name__)


async def main():
    logging.getLogger("watchdog").setLevel(logging.CRITICAL)
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="film.log",
    )

    with EosSession() as session:
        app = EosApp(session)
        session.loop.create_task(session.run())
        await app.run_async()


if __name__ == "__main__":
    asyncio.run(main())
