#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

rootdir = '/mnt/etl'
tomysqlscript = '/mnt/scrapy/thrump/tomysql.py'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(list)):
    path = os.path.join(rootdir,list[i])
    if os.path.isfile(path):
        os.system("python %s %s" % (tomysqlscript, path))
