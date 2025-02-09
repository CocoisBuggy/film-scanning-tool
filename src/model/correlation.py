import cv2
from cv2.typing import MatLike
from skimage.metrics import structural_similarity as ssim


def compare_images(previous: MatLike, current: MatLike):
    # Convert images to grayscale
    gray1 = cv2.cvtColor(previous, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(current, cv2.COLOR_BGR2GRAY)

    score, _ = ssim(gray1, gray2, full=True)
    return score
