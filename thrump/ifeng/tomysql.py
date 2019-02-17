#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import sys
import json
import uuid
import re

reload(sys)
sys.setdefaultencoding('utf8')

# 连接数据库
conn = mdb.connect(host='39.106.167.223', port=3306, user='root', passwd='HDEJjged819d.#bh', db='test', charset='utf8')

# 如果使用事务引擎，可以设置自动提交事务，或者在每次操作完成后手动提交事务conn.commit()
conn.autocommit(1)    # conn.autocommit(True) 

# 使用cursor()方法获取操作游标
cursor = conn.cursor()
# 因该模块底层其实是调用CAPI的，所以，需要先得到当前指向数据库的指针。

dbname = 'test'
file_path = sys.argv[1]

with open(file_path, 'r') as f:
    lines=f.readlines()

    conn.select_db(dbname)

    for line in lines:
        try:
            jsonline = json.loads(line, strict=False)
            title=jsonline["title"].replace(r'\s', '').replace("%", "").replace("_凤凰网", "").replace("凤凰网", "").replace("凤凰游戏", "").replace("凤凰科技", "").replace("凤凰网科技", "")
            sub_title = re.sub('\s','',title)
            author = jsonline["author"]
            html = jsonline["html"]
            publish_time = jsonline["publish_time"].replace("年","-").replace("月","-").replace("日","-")
            content = jsonline["content"]

            if publish_time.find("-") == -1:
                continue
            if len(content) == 0:
                continue

            #print "title: %s" % sub_title
            #print "author: %s" % author
            #print "html: %s" % html
            #print "publish_time: %s" % publish_time
            #print "content: %s" % content
            # 查询数据条目
            count = cursor.execute('SELECT * FROM articles WHERE title = "%s"' % sub_title)
            print 'select title %s total records: %d' % (sub_title,count)
            if count == 0:

                article = ""

                for i in range(len(jsonline["content"])):
                    #segment=str(jsonline["content"][i].encode('utf-8').decode('unicode_escape'))
                    segment=str(jsonline["content"][i].encode('utf-8'))
                    #print "########## segment: %s" % segment 
                    if segment == "打开微信，点击底部的“发现”，" or segment == "使用“扫一扫”即可将网页分享至朋友圈。" or segment == "第一财经" or segment == "APP" or segment == "日报微博" or segment == "微信服务号" or segment == "微信订阅号":
                        segment = "";
                    else:
                        segment = jsonline["content"][i] + "\n"
                    if len(jsonline["img"]) > i:
                        segment += "<img align=\"center\" border=\"0\" src=\"" + jsonline["img"][i] + "\" />\n"

                    article += segment

                sql = "INSERT INTO articles (title, content, html, publish_time, uid, aid) values ('%s','%s','%s','%s','%s','%s')" % (sub_title, article, html, publish_time, author, uuid.uuid1())
                print 'execute insert sql: %s' % sql
                cursor.execute(sql)
            # 如果没有设置自动提交事务，则这里需要手动提交一次
            conn.commit()
        except:
            import traceback
            traceback.print_exc()
            # 发生错误时会滚
            conn.rollback()
# 关闭游标连接
cursor.close()
# 关闭数据库连接
conn.close()
