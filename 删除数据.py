import pymysql

# 1.连接MySQL
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd="123456", charset='utf8', db='jslgjava1')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 2.发送指令（ *** 千万不要用字符串格式化去做SQL的拼接，安全隐患SQL注入***）
cursor.execute("delete from b_user where uid=%s",[13,])
conn.commit()

# 3.关闭
cursor.close()
conn.close()
