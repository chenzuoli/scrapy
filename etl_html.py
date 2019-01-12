# -*- coding: utf-8 -*-
import sys
import json

reload(sys) 
sys.setdefaultencoding('utf8')

ori_file_path=sys.argv[1]
res_file_path=sys.argv[2]
with open(ori_file_path, "r") as lines:
	strs = lines.readlines()
for string in strs:
	json_dict=json.loads(string)
	html=json_dict['html']
	with open(res_file_path, "a+") as f:
		f.write(string)
