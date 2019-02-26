#!/bin/python

import os
import sys
import json

reload(sys)
sys.setdefaultencoding('utf8')

list=["a","b","c","d"]
for i in range(len(list)):
    print i
    print list[i]
jsonline={"title": "100fen", "content": ["a", "b", "c", "d", "e", "f", "g"], "html": "https://www.yicai.com/news/100080579.html", "author": "yicai", "publish_time": "2018-12-16 18:35:38", "img": ["https://imgcdn.yicai.com/uppics/images/2018/12/65369b56e197129d772a0a6b576c7a6a.jpg", "1111111"]}
#jsonline = json.loads(str)
with open("md_file.md", 'a+') as md:
    for i in range(len(jsonline["content"])):
        print i
        md.write(jsonline["content"][i]+ "\n")
        if len(jsonline["img"]) > i:
            md.write(jsonline["img"][i] + "\n")
