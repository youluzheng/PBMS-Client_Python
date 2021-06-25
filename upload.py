import sys
import re
import requests

file = sys.argv[1]

# 返回类型，支持"url"和"markdown"两种类型
ret_type = "url"

# 协议类型
schema = "http"

# 服务器ip地址
host = "127.0.0.1"

# 服务器端口
port = "9001"

# 上传路径，如test1/test2
path = ''

url = schema + "://" + host + ":" + port + "/image?path=" + path

files = [
    ('image', open(file, 'rb'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data={}, files=files)

if response.status_code != 201:
    print(response.text)
else:
    if ret_type == "url":
        ret = re.search(r"\((.*)\)", response.text)
        print(ret.group(1))
    elif ret_type == "markdown":
        print(response.text)
    else:
        print("返回类型设置错误，只支持'url'和'markdown'两种类型")
