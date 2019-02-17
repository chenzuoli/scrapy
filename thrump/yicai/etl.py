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
for string in strs:
    decode_str=str(string.encode('utf-8').decode('unicode_escape'))
    print decode_str
    try:
        json_array=json.loads(decode_str)
        htmls=json_array["html"]
        print htmls
        for html in htmls:
            print html
            try:
                splits=html.split("/", 3)
                if len(splits) >= 3:
                    numberhtml=splits[2]
                    number=numberhtml.split(".")[0]
                    print "--------------" + str(number)
                    if number.isdigit(): 
                        urls.append("https://www.yicai.com/news/" + str(number) + ".html")
                #if re.match(r'.*/news/[0-9]+.html', html, 're.X'):
                #    urls.append(str(html).strip())
                #number=re.sub("\D", "", html)
                #if re.match(r'\d+', str(number), 're.X'):
                #    urls.append("https://yicai.com/news/" + str(number) + ".html")
            except Exception as ex:
                print ex
    except Exception as e:
        print e
    finally:
        print urls
for url in urls:
    with open(res_file, 'a+') as line:
        line.write("{\"html\": \"" + url + "\"}\n") 
