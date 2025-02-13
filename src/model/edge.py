import asyncio
import logging

import cv2
import numpy as np
from cv2.typing import MatLike, Point

log = logging.getLogger(__name__)


def cast_ray_cv(
    img: MatLike,
    start: Point,
    direction: Point,
    threshold: int,
    cast_distance=100,
) -> Point | None:
    """
    Cast a ray in a given direction until a non-black pixel is found.

    :param image_path: Path to the image file
    :param start: (x, y) start position
    :param direction: (dx, dy) direction to move
    :return: (x, y) of first non-black pixel or None if none found
    """
    x, y = start
    dx, dy = direction
    translation = 0

    while translation < cast_distance:
        log.debug(y, x)
        r, g, b, _ = img[y, x]
        luminosity = 0.299 * r + 0.587 * g + 0.114 * b

        if luminosity > threshold:
            if translation < 5:
                return

            return (x, y)

        x += dx
        y += dy
        translation += 1

    return x, y


def _draw_border_lines(img: MatLike, threshold=50, sample_density=40):
    """
    My simple heuristic algorithm for determining if there is some bad edge to a
    given candidate image.
    """
    gray_img = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)

    height, width, _ = gray_img.shape
    width_step = width // sample_density
    height_step = height // sample_density

    for ax in range(-1, 2):
        for ay in range(-1, 2):
            # we want the four cardinal directions.
            if abs(ax) == abs(ay):
                continue

            # ax and ay give us our scan directions and which edge we are to examine.
            for sample in range(1, sample_density):
                # when we ray-cast, the x/y is determined by first checking which direction we are
                # traversing.
                x, y = 0, 0
                if abs(ax):
                    # we are either going forward or backward along the x axis,
                    # meaning that the y axis will change with the sample and the
                    # x axis will either be the left or right edge.
                    x = 0 if ax == -1 else width
                    y = sample * height_step
                    if y == 0:
                        continue  # no reason to traverse the edge
                else:
                    # we are moving up or down along the y-axis
                    x = sample * width_step
                    y = 0 if ay == -1 else height
                    if x == 0:
                        continue

                ray = cast_ray_cv(gray_img, (x, y), (ax, ay), threshold)

                if ray is not None:
                    cv2.line(img, (y, x), ray, (0, 0, 255), 1)


def _data_in_frame_center(frame: MatLike, threshold=10):
    height, width, _ = frame.shape

    box_height: int = int(height // 1.5)
    box_width: int = int(width // 2)

    # Compute the top-left corner for centering.
    start_x: int = (width - box_width) // 2
    start_y: int = (height - box_height) // 2

    # Extract the central region
    central_box = frame[start_y : start_y + box_height, start_x : start_x + box_width]

    proportion_near_black = np.mean(np.less(central_box, threshold))
    passing = proportion_near_black < 0.7

    if not passing:
        cv2.rectangle(
            frame,
            (start_x, start_y),
            (start_x + box_width, start_y + box_height),
            (255, 0, 0),
            2,
        )

        cv2.putText(
            frame,
            "No data detected",
            (start_x + 5, start_y + 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 0, 0),
            2,
        )

    return passing


async def data_in_frame_center(frame: MatLike, **kwargs):
    return await asyncio.to_thread(_data_in_frame_center, frame, **kwargs)


async def draw_border_lines(frame: MatLike, **kwargs):
    return await asyncio.to_thread(_draw_border_lines, frame, **kwargs)
