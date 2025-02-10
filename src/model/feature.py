import asyncio
import io

import cv2
import numpy as np
import torch
from cv2.typing import MatLike
from PIL import Image
from PIL.ImageFile import ImageFile
from transformers import DetrFeatureExtractor, DetrForObjectDetection

model_name = "facebook/detr-resnet-50"
feature_extractor = DetrFeatureExtractor.from_pretrained(model_name)
model = DetrForObjectDetection.from_pretrained(model_name).to("cuda")


def model_inference(inputs):
    with torch.no_grad():
        with torch.amp.autocast("cuda"):
            return model(**inputs)


async def run_inference(inputs):
    # Offload the synchronous model_inference to a worker thread.
    outputs = await asyncio.to_thread(model_inference, inputs)
    return outputs


async def features(images: ImageFile):
    def work():
        return feature_extractor(images=images, return_tensors="pt").to("cuda")

    return await asyncio.to_thread(work)


async def detect_objects_and_draw_boxes(
    image: ImageFile, frame: MatLike
) -> list[tuple[tuple[int, int, int, int], str, float]]:
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
    # Forward pass through the model
    outputs = await run_inference(await features(image))

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

    # Draw bounding boxes and labels
    for box, label, score in zip(boxes, labels, scores):
        xmin, ymin, xmax, ymax = box
        xmin, ymin, xmax, ymax = int(xmin), int(ymin), int(xmax), int(ymax)

        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)  # Green box

        cv2.putText(
            frame,
            f"{label} {score:.2f}",
            (xmin, ymin - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2,
        )

    return list(zip(boxes, labels, scores))
