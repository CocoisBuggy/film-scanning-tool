import asyncio
import logging
import math

import cv2
import numpy as np
from cv2.typing import MatLike, Point
from skimage.draw import line

log = logging.getLogger(__name__)


def _draw_border_lines(img: MatLike, threshold=10, tolerance=5):
    """
    Detect if there is black border (overflow) by comparing the content's bounding box to the image edges.

    Parameters:
      img: Input image (BGR or grayscale).
      threshold: Pixel intensity threshold for determining non-black content.
      tolerance: Number of pixels allowed for a border to be considered "flush" with the image edge.

    Returns:
      A tuple (has_border, bbox) where:
         - has_border is True if the content's bounding box does not extend to the image edges.
         - bbox is (x, y, w, h) of the detected content region.
    """
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img

    # Create a binary image: content=255, near-black background=0.
    _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    # Find external contours.
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        return (False, None)  # No content detected.

    # Assume the largest contour is the content.
    content_contour = max(contours, key=cv2.contourArea)

    # Compute the bounding rectangle of the content.
    x, y, w, h = cv2.boundingRect(content_contour)
    bbox = (x, y, w, h)

    H, W = gray.shape
    # Check each edge: if the content does not reach the image's edge (within tolerance),
    # then there is a black border.
    left_gap = x
    top_gap = y
    right_gap = W - (x + w)
    bottom_gap = H - (y + h)

    has_border = (
        left_gap > tolerance
        or top_gap > tolerance
        or right_gap > tolerance
        or bottom_gap > tolerance
    )

    if has_border:
        cv2.drawContours(img, [content_contour], -1, (0, 0, 255), 2)

    return has_border


def _data_in_frame_center(frame: MatLike, threshold=10):
    height, width, _ = frame.shape
    box_width: int = int(width // 2)

    # Compute the top-left corner for centering.
    start_x: int = (width - box_width) // 2
    start_y: int = 0

    # Extract the central region
    central_box = frame[start_y : start_y + height, start_x : start_x + box_width]

    proportion_near_black = np.mean(np.less(central_box, threshold))
    passing = proportion_near_black < 0.5

    if not passing:
        cv2.rectangle(
            frame,
            (start_x, start_y),
            (start_x + box_width, start_y + height),
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


async def data_in_frame_center(frame: MatLike, threshold=10):
    return await asyncio.to_thread(_data_in_frame_center, frame, threshold=threshold)


async def draw_border_lines(frame: MatLike, threshold=10, tolerance=5):
    return await asyncio.to_thread(
        _draw_border_lines,
        frame,
        threshold=threshold,
        tolerance=tolerance,
    )
