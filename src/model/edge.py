import logging
import math

import cv2
import numpy as np
from cv2.typing import MatLike, Point
from skimage.draw import line

log = logging.getLogger(__name__)


def path_straightness(path: list[Point], tolerance: float = 10.0):
    """
    Returns True if the list of points is approximately collinear.

    Args:
        points (List[Point]): List of points to check.
        tolerance (float): Maximum allowable perpendicular distance from the line.
                           Points further than this distance from the base line
                           will cause the function to return False.
    """

    if len(path) < 2:
        return True

    print(path)

    # Find the first two distinct points.
    p0 = path[0]
    p1 = path[-1]

    # Define the vector from p0 to p1.
    dx = p1[0] - p0[0]
    dy = p1[1] - p0[1]

    # Precompute the norm of the direction vector.
    norm = math.hypot(dx, dy)
    if norm == 0:
        return True  # Redundant check; p0 and p1 should be distinct.

    # Check each point's distance from the line defined by p0 and p1.
    for p in path:
        # Perpendicular distance from point p to the line through p0 and p1.
        distance = abs(dy * (p[0] - p0[0]) - dx * (p[1] - p0[1])) / norm

        # if the distance is larger than the tolerance, we consider this to be a nonlinear
        # line - fuzzy.
        if distance > tolerance:
            return False

    return True


def draw_border_lines(
    img: MatLike,
    threshold_value=5,
    sample_interval=10,
    line_color=(0, 0, 255),  # Red in BGR
    line_thickness=1,
    draw_scanlines=True,
):
    """
    For each sampled point along the four image borders, trace a line toward (0,0)
    relative to the centroid of the image.
    and draw a red line from the border point to the last pixel that is black
    (or near-black) before encountering a non-black pixel.

    Parameters:
      image_path (str): Path to the image file.
      threshold_value (int): Maximum pixel value (in grayscale) to consider as black.
      sample_interval (int): Number of pixels to skip between samples along each border.
      line_color (tuple): BGR color for the line.
      line_thickness (int): Thickness of the drawn line.
    """
    # Load image in color and create a grayscale version for checking

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape

    def trace_line_to_nonblack(x: int, y: int):
        # Use skimage.draw.line: note that it expects (row, col)
        rr, cc = line(y, x, h // 2, w // 2)
        # The generated line includes the starting point and goes to (0,0)
        last_black = None

        for r, c in zip(rr, cc):
            # Check boundaries (should be fine, but just in case)
            if r < 0 or r >= h or c < 0 or c >= w:
                break
            # If the pixel is black (or near black) in the grayscale image...
            if int(gray[r, c]) <= threshold_value:
                last_black = (c, r)  # (x, y) for drawing in OpenCV
            else:
                # Found a non-black pixel: stop tracing
                break
        return last_black

    def process_points(points):
        edge_termination_points: list[Point] = []

        for x, y in points:
            # Only consider border points that are black (or near black) initially.
            # since there is nowhere to go if the first sample location is already valid.
            if int(gray[y, x]) > threshold_value:
                continue

            end_point = trace_line_to_nonblack(x, y)

            if end_point is not None and end_point != (x, y):
                if draw_scanlines:
                    cv2.line(
                        img, (x, y), end_point, line_color, thickness=line_thickness
                    )
                edge_termination_points.append(end_point)

        return edge_termination_points

    # Collect sample points along each of the four borders
    top_points = [(x, 0) for x in range(0, w, sample_interval)]
    bottom_points = [(x, h - 1) for x in range(0, w, sample_interval)]
    left_points = [(0, y) for y in range(0, h, sample_interval)]
    right_points = [(w - 1, y) for y in range(0, h, sample_interval)]

    # Process each set of points
    top_points = process_points(top_points)
    bottom_points = process_points(bottom_points)
    left_points = process_points(left_points)
    right_points = process_points(right_points)

    violations = []

    for stack in [top_points, bottom_points, left_points, right_points]:
        colinear = path_straightness(stack)
        for idx, point in enumerate(stack):
            if idx == 0:
                continue

            cv2.line(
                img,
                stack[idx - 1],
                point,
                (255, 0, 0) if not colinear else (0, 0, 255),
                thickness=line_thickness * 2,
            )
