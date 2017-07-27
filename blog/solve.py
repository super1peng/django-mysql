#coding:utf-8

import json,MySQLdb

def TableToJson():

    try:
        # 创建 mysql 数据库连接对象
        conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123lxp',  db='first', port=3306, charset='utf8')

        # 创建 mysql 数据库游标对象
        cur = conn.cursor()

        # 编写 sql 语句
        sql = "SELECT * FROM temperature"

        # 执行 sql 语句
        cur.execute(sql)

        # 获取数据
        data = cur.fetchall()

        # 关闭 cursor
        cur.close()

        # 关闭 connection
        conn.close()

        # 对结果进行处理
 
        listdata = list(data)


    except:
        print 'Mysql connect fail !'
    
    
    
    return listdata





