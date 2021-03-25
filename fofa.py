# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/9 20:02
@Auth ： Ye0kr1n
@File ：fofa.py
@IDE ：PyCharm
@mail:1005406456@qq.com
"""
import base64
import json
import requests
from urllib3 import disable_warnings

disable_warnings()
uname="1005406456@qq.com"
api_key="*******************************"
searchtext="text"
ip_addr=""
res_text=""
fofa_url="https://fofa.so/api/v1/search/all?email="+uname+"&key="+api_key+"&qbase64="+base64.b64encode(searchtext)+"&size=100"
response_body=json.loads(requests.get(fofa_url).text)
#print  response_body
res_body=response_body["results"]
print(res_body)