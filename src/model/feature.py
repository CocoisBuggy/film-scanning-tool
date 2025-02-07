import io

import cv2
import numpy as np
import torch
from PIL import Image
from transformers import DetrFeatureExtractor, DetrForObjectDetection

model_name = "facebook/detr-resnet-50"
feature_extractor = DetrFeatureExtractor.from_pretrained(model_name)
model = DetrForObjectDetection.from_pretrained(model_name).to("cuda")


def detect_objects_and_draw_boxes(image_bytes, model_name="facebook/detr-resnet-50"):
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

    inputs = feature_extractor(images=image, return_tensors="pt")
    # Forward pass through the model
    with torch.no_grad():
        outputs = model(**inputs)

    # Post-process the outputs
    target_sizes = torch.tensor(
        [image.size[::-1]]
    )  # Reverse image size (height, width)

    post_processed_outputs = feature_extractor.post_process_object_detection(
        outputs, target_sizes=target_sizes, threshold=0.8
    )

    # Get bounding boxes, labels, and scores
    boxes = post_processed_outputs[0]["boxes"].detach().numpy()
    labels = post_processed_outputs[0]["labels"].detach().numpy()
    scores = post_processed_outputs[0]["scores"].detach().numpy()

    # Convert PIL Image to OpenCV format
    open_cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Draw bounding boxes and labels
    for box, label, score in zip(boxes, labels, scores):
        xmin, ymin, xmax, ymax = box
        xmin, ymin, xmax, ymax = int(xmin), int(ymin), int(xmax), int(ymax)

        cv2.rectangle(
            open_cv_image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2
        )  # Green box
        label_text = model.config.id2label[label]  # Get class name
        cv2.putText(
            open_cv_image,
            f"{label_text} {score:.2f}",
            (xmin, ymin - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2,
        )

    return open_cv_image
