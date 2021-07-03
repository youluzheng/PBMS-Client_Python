import keyboard_listen
import clipboard_listen
import upload


def main():
    image = clipboard_listen.read_clipBoard()
    if image is None:
        return
    ret = upload.upload(image)
    clipboard_listen.write_clipboard(ret)


if __name__ == "__main__":
    keyboard_listen.add_keyboard_listen(main)
