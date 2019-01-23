#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# 连接数据库
conn = mdb.connect('39.106.167.223', 'root', 'HDEJjged819d.#bh')

# 如果使用事务引擎，可以设置自动提交事务，或者在每次操作完成后手动提交事务conn.commit()
conn.autocommit(1)    # conn.autocommit(True) 

# 使用cursor()方法获取操作游标
cursor = conn.cursor()
# 因该模块底层其实是调用CAPI的，所以，需要先得到当前指向数据库的指针。

dbname = 'website'
file_path = sys.argv[1]

with open(file_path, 'r') as f:
        lines=f.readlines()

try:

    conn.select_db(dbname)

    for line in lines:
        jsonline = json.loads(line, strict=False)
        title=jsonline["title"].replace(r'\s', '').replace("%", "")
        sub_title = re.sub('\s','',title)
        author = jsonline["author"]
        publish_time = jsonline["publish_time"]
        content = jsonline["content"]
        # 查询数据条目
        count = cursor.execute('SELECT * FROM articles WHERE title = %s' %title)
        print 'total records: %d' %count
        print 'total records:', cursor.rowcount
        if count == 0:


    value = [2,'John']
    cursor.execute('INSERT INTO test values(%s,%s)',value)



    # 如果没有设置自动提交事务，则这里需要手动提交一次
    conn.commit()
except:
    import traceback
    traceback.print_exc()
    # 发生错误时会滚
    conn.rollback()
finally:
    # 关闭游标连接
    cursor.close()
    # 关闭数据库连接
    conn.close()
