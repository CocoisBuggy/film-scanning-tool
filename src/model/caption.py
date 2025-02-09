import io

from PIL import Image
from transformers import BlipForConditionalGeneration, BlipProcessor

device = "cuda"
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
).to(device)


def get_caption_for_image(image_data: bytes):
    image = Image.open(io.BytesIO(image_data)).convert("RGB")

    # Process image and generate caption
    inputs = processor(images=image, return_tensors="pt").to(device)
    out = model.generate(**inputs)

    # Decode and print caption
    caption = processor.decode(out[0], skip_special_tokens=True)
    print("Generated Caption:", caption)
