import logging
import configparser
import os

# 因为还没读取到配置文件，只能先用文件的方式打印日志到当前目录
if not os.path.exists("config.ini"):
    with open('output.log', 'a', encoding='utf-8') as f:
        f.writelines("config.ini文件未找到!\n")
        exit(1)

cp = configparser.ConfigParser()
cp.read("config.ini")

try:
    options = dict(cp.items("logger"))
except configparser.NoSectionError:
    with open('output.log', 'a', encoding='utf-8') as f:
        f.writelines("[logger]配置项未找到!\n")
        exit(1)


path = options.get("path")
file_name = options.get("file_name")
level = options.get("level")

level_list = ['DEBUG', 'debug', 'INFO', 'info',
              'WARNING', 'warning', 'ERROR', 'error']


class Logger:
    def __init__(self, module: str):
        self.logger = logging.getLogger(module)
        self.logger.setLevel(level.upper() if level in level_list else 'INFO')
        fmt = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s', '%Y-%m-%d %H:%M:%S')

        # 如果配置文件中没有path配置项
        path_temp = path if path else ''
        # 如果配置文件中没有file_name配置项
        file_name_temp = file_name if file_name else 'output.log'
        # 设置文件日志
        fh = logging.FileHandler(
            file_name_temp if path_temp == '' else path_temp + '/' + file_name_temp)
        fh.setFormatter(fmt)
        fh.setLevel(level.upper() if level in level_list else 'INFO')
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)


__log = Logger("logger")

if path is None:
    __log.warn("[logger]->path配置项未找到, 默认设置为当前目录")

# 如果设置为当前目录，特殊处理
if path == '' or path == '.':
    __log.info("设置日志目录:当前目录")

else:
    __log.info("设置日志目录:" + path)
    if not os.path.exists(path):
        __log.warn(path + "目录不存在, 正在创建中...")
        os.makedirs(path)
        __log.info(path + "目录创建完成!")

if file_name is None:
    __log.warn("[logger]->file_name配置项未找到，默认设置为output.log")

__log.info("设置日志文件名:" + file_name)

if level is None:
    __log.warn("[logger]->level配置项未找到，默认设置为INFO")

if level not in level_list:
    __log.warn("[logger]->level，" + level + "无法识别，默认设置为INFO")

__log.info("设置日志级别:" + level)
