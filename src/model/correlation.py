import cv2
import numpy as np
from cv2.typing import MatLike
from skimage.metrics import structural_similarity as ssim


def compare_images(previous: MatLike, current: MatLike, threshold=0.75) -> float:
    # Convert images to grayscale
    img1 = cv2.cvtColor(previous, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(current, cv2.COLOR_BGR2GRAY)

    # ORB detector
    orb = cv2.ORB_create(nfeatures=500)

    # Find keypoints and descriptors
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # FLANN-based matcher
    index_params = dict(
        algorithm=6,  # FLANN_INDEX_LSH
        table_number=6,  # 12 is good for ORB
        key_size=12,  # 20 is good for ORB
        multi_probe_level=1,
    )

    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)  # pyright: ignore

    # Match descriptors
    matches = flann.knnMatch(des1, des2, k=2)

    # Apply ratio test to keep only good matches
    good_matches = [
        m
        for pair in matches
        if len(pair) == 2
        for m, n in [pair]
        if m.distance < threshold * n.distance
    ]

    # If too few matches, return low similarity
    if len(good_matches) < 10:
        return 0.0

    # Extract point coordinates
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    # Compute homography using RANSAC
    H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    # Compute match percentage
    match_ratio = np.divide(np.sum(mask), len(mask))

    return match_ratio
