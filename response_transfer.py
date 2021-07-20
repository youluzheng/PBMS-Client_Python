import re
import logger
import configparser

log = logger.Logger('response_transfer')

log.info('正在初始化相应配置...')
cp = configparser.ConfigParser()
cp.read("config.ini", encoding="utf-8")

try:
    options = dict(cp.items("response"))
except configparser.NoSectionError:
    log.warn('[response]配置项未找到, 使用默认配置初始化')
    return_type = 'markdown'
    log.info('初始化返回类型:markdown')
else:
    return_type_list = ['url', 'markdown']
    return_type = options.get("return_type")
    if return_type is None:
        log.warn('[response]->return_type配置项未找到, 默认设置markdown')
    elif return_type not in return_type_list:
        log.warn('[response]->return_type无法识别配置项' +
                 return_type + ', 默认设置markdown')
        return_type = 'markdown'
    else:
        log.info('初始化返回类型:' + return_type)

log.info('相应配置完成!')


def transfer(ret) -> str:
    if return_type == "url":
        ret = re.search(r"\((.*)\)", ret)
        return ret.group(1)
    return ret
