import base64
from PIL import Image
from io import BytesIO
import re


def image_to_base64(image: Image.Image) -> str:
    output_buffer = BytesIO()
    image.save(output_buffer, format='png')
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str


def base64_to_image(base64_str: str) -> Image:
    base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    image = Image.open(image_data)
    return image
