from __future__ import (absolute_import,division,print_function,unicode_literals)

#当你urllib.urlopen一个 https 的时候会验证一次 SSL 证书 ，当目标使用的是自签名的证书时就会爆出该错误消息。所以要采用这个方法
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

try:
	from urllib.request import urlopen
except ImportError:
	print('import false')

import json

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response = urlopen(json_url)
req = response.read()

with open('./btc_close_2017_urllib.json','wb') as f:
	f.write(req)

file_urllib = json.loads(req)
print(file_urllib)

'''
import requests

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)

with open(filename,'wb') as f:
	f.write(req.text)

file_requests = req.json()
'''