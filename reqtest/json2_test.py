# -*- coding: utf-8 -*-
'''
@Time    : 2021/2/6 14:25
@Author  : zxd
'''
import requests
import json
payload = {
    "yoyo" : True,
    "json" : False,
    "python" : "7611"
    }
print(type(payload))
n_payload=json.dumps(payload)
print(n_payload)
