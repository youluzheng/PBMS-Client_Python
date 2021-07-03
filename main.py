import clipboard_listen
import request_send

image = clipboard_listen.read_clipBoard()
if image is None:
    exit(1)
ret = request_send.send('aaa.png', image)
print(ret)
