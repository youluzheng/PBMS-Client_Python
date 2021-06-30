import pyperclip
from PIL import ImageGrab
from PIL import Image
import logger
import image_tool

log = logger.Logger("clipboard_listen")


def read_clipBoard() -> str:
    """ 获取粘贴板图片转换为Base64编码 """

    image = ImageGrab.grabclipboard()
    if isinstance(image, Image.Image):
        return image_tool.image_to_base64(image)
    else:
        log.warn("粘贴板中未找到图片!")


def write_clipboard(result: str) -> None:
    pyperclip.copy(result)
