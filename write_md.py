#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import json
import datetime

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
		jsonline = json.loads(line)
		title=jsonline["title"].replace("凤凰", "").replace(r'\s', '')
		md_file = father_path + "/" + title + ".md"
		# write md header
		with open(md_file, 'a+') as header:
			header.write("---\n")
			header.write("title: " + title + "\n")
			header.write("date: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")
			header.write("tags: \n")
			header.write("categories: \n")
			header.write("---\n")
			header.write(jsonline["content"][0] + "\n")
			header.write("<!-- more -->\n")
		# write the article
		with open(md_file, 'a+') as md:
			for segment in jsonline["content"]:
				md.write(segment + "\n")	
	except BaseException, e:
		print(e)
