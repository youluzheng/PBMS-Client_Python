import threading
import keyboard
import configparser
import logger

log = logger.Logger("keyboard_listen")

cp = configparser.ConfigParser()
cp.read("config.ini")

log.info("正在初始化快捷键配置...")

try:
    options = dict(cp.items("Hotkeys"))
except configparser.NoSectionError:
    log.error("Hotkeys配置模块未找到")
    exit(1)

# 上传快捷键
upload_key = options.get("upload_key")

if not upload_key:
    log.error("[Hotkeys]->upload_key配置项未找到")
    exit(1)
else:
    log.info("初始化上传快捷键:" + upload_key)

# 退出快捷键
exit_key = options.get("exit_key")

if not exit_key:
    log.error("[Hotkeys]->exit_key配置项未找到")
    exit(1)
else:
    log.info("初始化退出快捷键:" + exit_key)

log.info("快捷键配置初始化完成!")


def add_keyboard_listen(callback, args=()):
    keyboard.add_hotkey(upload_key, callback, args=args)
    keyboard.wait(exit_key)
