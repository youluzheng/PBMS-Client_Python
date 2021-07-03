import configparser
import logger
import requests
import response_transfer
import uuid

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


def __name_generator() -> str:
    uid = str(uuid.uuid4())
    suid = ''.join(uid.split('-'))
    file_name = suid + ".png"
    return file_name


def upload(image) -> str:
    file_name = __name_generator()
    ret = requests.post(url, files=[('image', (file_name, image))])
    if ret.status_code == 201:
        log.info("上传成功!")
        log.debug(ret.text)
        return response_transfer.transfer(ret.text)
    else:
        log.warn(ret.text)
        return '上传失败, 具体信息请查看日志'
