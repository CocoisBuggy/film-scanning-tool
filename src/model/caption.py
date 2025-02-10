import asyncio
import io
import logging

from PIL import Image
from PIL.ImageFile import ImageFile
from transformers import BlipForConditionalGeneration, BlipProcessor

device = "cuda"
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
).to(device)


log = logging.getLogger(__name__)


async def get_caption_for_image(image_data: ImageFile):
    def inference():
        image = image_data.convert("RGB")
        # Process image and generate caption
        inputs = processor(images=image, return_tensors="pt").to(device)
        out = model.generate(**inputs)

        # Decode and print caption
        caption = processor.decode(out[0], skip_special_tokens=True)
        return caption

    return await asyncio.to_thread(inference)
