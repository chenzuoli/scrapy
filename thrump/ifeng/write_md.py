#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import json
import datetime
import re

reload(sys)
sys.setdefaultencoding('utf8')

# src_file is the scrapyed file, need etl
# etl_file is the result file
src_file = sys.argv[1]
etl_file = sys.argv[2]
print src_file
print etl_file
with open(src_file, 'r') as f:
	lines=f.readlines()

# etl data
for line in lines:
	# 移除空行，并将同一个json串({}间)合并到一行
	if line == '\n':
                continue
        ifin = '}' in line
        if ifin == False:
                line=line.strip('\n')
        # replace blank char and '>' and '>>' to empty string
        newline=line.replace('[\s]', '').replace('>', '').replace('>>', '')

	with open(etl_file, 'a+') as f:
		f.write(newline)

# write md file
with open(etl_file, 'r') as f:
	lines = f.readlines()
pwd = os.getcwd()
father_path = os.path.abspath(os.path.dirname(pwd)+os.path.sep+".") + os.path.sep + "md"
for line in lines:
	try:
		jsonline = json.loads(line, strict=False)
                if len(jsonline["content"]) <= 7:
                    continue
		title=jsonline["title"].replace(r'\s', '').replace("%", "").replace("%", "").replace("_凤凰网", "").replace("凤凰网", "").replace("凤凰游戏", "").replace("凤凰科技", "").replace("凤凰网科技", "")
                sub_title = re.sub('\s','',title)
                author = jsonline["author"]
                publish_time = jsonline["publish_time"].replace("年","-").replace("月","-").replace("日","-")
		md_file = father_path + "/" + sub_title + ".md"
		# write md header
		with open(md_file, 'a+') as header:
			header.write("---\n")
			header.write("title: " + sub_title + "\n")
                        if author == None:
			        header.write("author: " + str(author) + "\n")
                        else:
                                header.write("author: wetech\n")
			if publish_time == None:
                         	header.write("date: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")
			else:
                                header.write("date: " + str(publish_time) + "\n")
			header.write("tags: \n")
			header.write("categories: \n")
			header.write("---\n")
                        if len(jsonline["content"]) >=4:
			    header.write(jsonline["content"][6] + "\n")
                        else:
                            header.write("read detail...")
			header.write("<!-- more -->\n")
		# write the article
		with open(md_file, 'a+') as md:
                        for i in range(len(jsonline["content"])):
                            segment=jsonline["content"][i]
                            if segment == "打开微信，点击底部的“发现”，" or segment == "使用“扫一扫”即可将网页分享至朋友圈。" or segment == "第一财经" or segment == "APP" or segment == "日报微博" or segment == "微信服务号" or segment == "微信订阅号" or segment == "用微信扫描二维码" or segment == "分享至好友和朋友圈":
                                md.write("")
                            else:
                                md.write(jsonline["content"][i]+ "\n")
                            if len(jsonline["img"]) > i:
                                md.write("<img align=\"center\" border=\"0\" src=\"" + jsonline["img"][i] + "\" />\n")
	except BaseException, e:
		print e
