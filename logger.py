import logging
import configparser
import os

# 因为还没读取到配置文件，只能先用文件的方式打印日志到当前目录
if not os.path.exists("config.ini"):
    print("config.ini文件未找到，启动失败")
    exit(1)

cp = configparser.ConfigParser()
cp.read("config.ini", encoding="utf-8")

is_logger_exists = True

try:
    options = dict(cp.items("logger"))
except configparser.NoSectionError:
    is_logger_exists = False
    path = 'logs'
    file_name = 'output.log'
    level = 'INFO'
else:
    path = options.get("path")
    file_name = options.get("file_name")
    level = options.get("level")

level_list = ['DEBUG', 'debug', 'INFO', 'info',
              'WARNING', 'warning', 'ERROR', 'error']

if path is not None:
    path_temp = path
else:
    path_temp = 'logs'

# 如果不是当前目录
if path_temp != '' and path_temp != '.':
    if not os.path.exists(path_temp):
        os.makedirs(path_temp)

file_name_temp = file_name if file_name else 'output.log'

level_temp = level.upper() if level in level_list else 'INFO'

if path_temp == '':
    log_file_full_path = file_name_temp
else:
    log_file_full_path = path_temp + '/' + file_name_temp


class Logger:
    def __init__(self, module: str):
        self.logger = logging.getLogger(module)
        self.logger.setLevel(level_temp)
        fmt = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] %(message)s',
            '%Y-%m-%d %H:%M:%S'
        )

        # 设置文件日志
        fh = logging.FileHandler(log_file_full_path)
        fh.setFormatter(fmt)
        fh.setLevel(level_temp)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)


log = Logger("logger")

log.info("正在初始化日志配置...")

if not is_logger_exists:
    log.warn("[logger]配置项未找到, 使用默认配置初始化日志设置")

if path != path_temp:
    log.warn("[logger]->path配置项未找到, 默认设置为logs目录")
else:
    if path == '' or path == '.':
        log.info("初始化日志目录:当前目录")
    else:
        log.info("初始化日志目录:" + path)


if file_name != file_name_temp:
    log.warn("[logger]->file_name配置项未找到，默认设置为output.log")
else:
    log.info("初始化日志文件名称:" + file_name)

if level.upper() != level_temp:
    if level:
        log.warn("level配置项无法识别:" + level + "，默认设置为INFO")
    else:
        log.warn("[logger]->level配置项未找到，默认设置为INFO")
else:
    log.info("初始化日志级别:" + level_temp)

log.info("日志初始化配置完成!")
