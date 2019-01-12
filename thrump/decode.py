# -*- coding: utf-8 -*-
import sys

reload(sys) 
sys.setdefaultencoding('utf8')

ori_file_path=sys.argv[1]
res_file_path=sys.argv[2]
with open(ori_file_path, "r") as lines:
	strs = lines.readlines()
for string in strs:
	#with open(res_file_path, "a+", encoding="utf-8") as f:
	with open(res_file_path, "a+") as f:
		f.write(str(string.encode('utf-8').decode('unicode_escape')))
