#!/bin/python
import os
import sys
import json
import re

reload(sys)
sys.setdefaultencoding('utf8')

src_file=sys.argv[1]
res_file=sys.argv[2]

urls=[]

with open(src_file, "r") as lines:
    strs = lines.readlines()
for str in strs:
    str = str[7:].replace('"', '')
    htmls = str.split(',')
    for html in htmls:
        if html.endswith("html") or html.endswith("htm"):
            if html.find('v.ifeng.com') == -1 and html.find('search') == -1 and html.find('yc.ifeng.com') == -1 and html.find('index') == -1:
                html = html.strip().strip('\\n')
                if html.find('http') == -1:
                    html = "http:%s" % html
                urls.append(html)

for url in urls:
    with open(res_file, 'a+') as line:
        line.write("{\"html\": \"" + url + "\"}\n") 
