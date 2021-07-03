import logger
import pyperclip
from PIL import ImageGrab
from PIL import Image
from io import BytesIO

log = logger.Logger("clipboard_listen")


def read_clipBoard() -> bytes:
    """ 获取粘贴板图片返回bytes数据， 如果图片不存在返回None """

    image = ImageGrab.grabclipboard()
    if isinstance(image, Image.Image):
        output_buffer = BytesIO()
        image.save(output_buffer, format='png')
        image_date = output_buffer.getvalue()
        output_buffer.close()
        return image_date
    else:
        log.warn("粘贴板中未找到图片!")


def write_clipboard(result: str) -> None:
    pyperclip.copy(result)
