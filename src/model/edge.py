import asyncio
import logging
import math

import cv2
import numpy as np
from cv2.typing import MatLike, Point
from skimage.draw import line

log = logging.getLogger(__name__)


def cast_ray_cv(img: MatLike, start, direction, cast_distance=100):
    """
    Cast a ray in a given direction until a non-black pixel is found.

    :param image_path: Path to the image file
    :param start: (x, y) start position
    :param direction: (dx, dy) direction to move
    :return: (x, y) of first non-black pixel or None if none found
    """
    x, y = start
    dx, dy = direction

    while 0 <= x < cast_distance and 0 <= y < cast_distance:
        if int(img[y, x]) > 10:
            return (x, y)

        x += dx
        y += dy

    return None


def _draw_border_lines(img: MatLike, threshold=10, tolerance=5, sample_density=100):
    """
    My simple heuristic algorithm for determining if there is some bad edge to a
    given candidate image.
    """
    img = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)

    height, width, _ = img.shape
    width_step = width // sample_density
    height_step = height // sample_density

    for ax in range(-1, 1):
        for ay in range(-1, 1):
            # ax and ay give us our scan directions and which edge we are to examine.
            for sample in range(sample_density):
                # draw lines.
                x = width_step * sample * ax
                y = height_step * sample * ay
                ray = cast_ray_cv(img, (x, y), (ax, ay))
                if ray is not None:
                    cv2.line(img, (x, y), ray, (0, 0, 255), 2)


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


async def draw_border_lines(frame: MatLike, threshold=10, tolerance=5):
    return await asyncio.to_thread(
        _draw_border_lines,
        frame,
        threshold=threshold,
        tolerance=tolerance,
    )
