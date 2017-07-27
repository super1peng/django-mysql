# -*- coding:utf-8 -*-
import MySQLdb
# ----------------------------
# 错误码
# 正常返回 code : 200
# 数据连接失败 code : 400
# 请求参数有误 code : 401
# ----------------------------

# 连接MySQL db
def connect_db(db):
    try:
        conn = MySQLdb.connect(host="10.9.8.*",
                             port=3306,
                             user="monitor",
                             passwd="monitor1",
                             db=db,
                             charset="utf8")
    except Exception, e:
        conn = 400
    return conn



# 请求MySQL获取数据
def get_data(db, sql):
    conn = connect_db(db)
    if conn == 400:
        return conn
    else:
        try:
            cur = conn.cursor()
            cur.execute(sql)
            data = cur.fetchall()
            cur.close()
            conn.commit()
            conn.close()
            return data
        except Exception, e:
            return 401