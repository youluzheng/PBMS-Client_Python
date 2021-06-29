import keyboard
import configparser

cp = configparser.ConfigParser()
cp.read("config.ini")

options = dict(cp.items("Hotkeys"))

# 上传快捷键
upload_key = options.get("upload_key")

# 推出快捷键
exit_key = options.get("exit_key")


def add_keyboard_listen(callback, args=()):

    keyboard.add_hotkey(str(upload_key), callback, args=args)
    keyboard.wait(exit_key)


if __name__ == "__main__":
    def test(str):
        print(str)

    add_keyboard_listen(test, ('aaa', ))
