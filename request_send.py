import configparser
import logger
import requests

log = logger.Logger("request_send")

log.info("正在初始化上传配置...")

cp = configparser.ConfigParser()
cp.read("config.ini")

try:
    options = dict(cp.items("request"))
except configparser.NoSectionError:
    log.error("[request]配置项未找到")
    exit(1)

schema_list = ['http', 'https', 'HTTP', 'HTTPS']
schema = options.get("schema")

if schema is None:
    log.error("[request]->schema配置项未找到")
    exit(1)
elif schema not in schema_list:
    log.error("[request]->schema无法识别" + schema + '配置项')
    exit(1)
else:
    log.info("初始化协议类型:" + schema)

host = options.get("host")
if host is None:
    log.error('[request]->host配置项未找到')
    exit(1)
else:
    log.info('初始化host:' + host)

port = options.get("port")

if port is None:
    if schema == 'http' or schema == 'HTTP':
        port = 80
    else:
        port = 443
    log.warn('[request]->port配置项未找到, 初始化默认配置:' + str(port))
else:
    log.info('初始化端口:' + port)

path = options.get("path")

if path is None:
    path = ''
    log.info('上传路径未配置, 默认为当前目录')
else:
    if path == '' or path == '.':
        log.info('初始化上传目录:当前目录')
    else:
        log.info('初始化上传目录:' + path)

log.info('上传配置初始化完成')

url = schema + "://" + host + ":" + str(port) + "/image?path=" + path


def send(file_name, image) -> str:
    ret = requests.post(url, files=[('image', (file_name, image))])
    log.info("上传成功!")
    log.debug(ret.text)
    return ret.text
