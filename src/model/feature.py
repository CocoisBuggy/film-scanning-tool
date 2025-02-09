import io

import cv2
import numpy as np
import torch
from cv2.typing import MatLike
from PIL import Image
from transformers import DetrFeatureExtractor, DetrForObjectDetection

model_name = "facebook/detr-resnet-50"
feature_extractor = DetrFeatureExtractor.from_pretrained(model_name)
model = DetrForObjectDetection.from_pretrained(model_name).to("cuda")


def detect_objects_and_draw_boxes(
    image_bytes,
) -> tuple[MatLike, list[tuple[tuple[int, int, int, int], str, float]]]:
    """
    Detects objects in an image using a pre-trained DETR model, draws bounding boxes
    and labels around the detected objects, and displays the image using OpenCV.

    Args:
        image_path (str): The path to the image file.
        model_name (str, optional): The name of the pre-trained DETR model to use.
                                     Defaults to "facebook/detr-resnet-50". You can explore other models.

    Returns:
        None. Displays the image with bounding boxes using cv2.imshow().
    """

    try:
        # Decode bytes to PIL Image
        image = Image.open(io.BytesIO(image_bytes))  # Use io.BytesIO
    except Exception as e:  # Catch potential decoding errors
        print(f"Error decoding image bytes: {e}")
        return

    inputs = feature_extractor(images=image, return_tensors="pt").to("cuda")
    # Forward pass through the model
    with torch.no_grad():
        with torch.amp.autocast("cuda"):
            outputs = model(**inputs)

    # Post-process the output
    # Reverse image size (height, width)s
    target_sizes = torch.tensor([image.size[::-1]])

    post_processed_outputs = feature_extractor.post_process_object_detection(
        outputs,
        target_sizes=target_sizes,
        threshold=0.8,
    )

    # Get bounding boxes, labels, and scores
    boxes = post_processed_outputs[0]["boxes"].detach().cpu().numpy()
    scores = post_processed_outputs[0]["scores"].detach().cpu().numpy()
    labels = [
        model.config.id2label[label]
        for label in post_processed_outputs[0]["labels"].detach().cpu().numpy()
    ]

    # Convert PIL Image to OpenCV format
    open_cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Draw bounding boxes and labels
    for box, label, score in zip(boxes, labels, scores):
        xmin, ymin, xmax, ymax = box
        xmin, ymin, xmax, ymax = int(xmin), int(ymin), int(xmax), int(ymax)

        cv2.rectangle(
            open_cv_image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2
        )  # Green box

        cv2.putText(
            open_cv_image,
            f"{label} {score:.2f}",
            (xmin, ymin - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2,
        )

    return open_cv_image, list(zip(boxes, labels, scores))
