#!/usr/bin/env python3

import hashlib
import time
import requests
import json


c_dict ={}
c_dict['appKey'] = "13247257"
c_dict['timestamp'] = int(time.time())
c_dict['nonce'] = 12345
c_dict['cardId'] = "89860617040034613309"
secret = '2d21c91217794dc687100033cf2e47c9'


def str_encrypt(str):
	sha = hashlib.sha1(str.encode('utf-8'))
	encrypt = sha.hexdigest()
	return encrypt

def build_sign(c):
	l = sorted(list(c_dict.keys()))
	r = ''
	for i in l:
		r +=i
		r +=str(c[i])
	r = secret + r + secret
	return str_encrypt(r).upper()




sign = build_sign(c_dict)
c_dict['sign'] = sign


url = "http://m2mapi.sealan-tech.com/api/v1/card/getDetails?appKey={appKey}&timestamp={timestamp}&nonce={nonce}&cardId={cardId}&sign={sign}".format(**c_dict)



print(url)
r = requests.get(url)
print(r.content.decode('utf-8'))


