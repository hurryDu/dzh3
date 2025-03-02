import pymysql

# 1.连接MySQL
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd="123456", charset='utf8', db='jslgjava1')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 2.发送指令（ *** 千万不要用字符串格式化去做SQL的拼接，安全隐患SQL注入***）
sql = "select * from b_user"
cursor.execute(sql)
data_list=cursor.fetchall()
#print(data_list)
for row_dict in data_list:
    print(row_dict)

# 3.关闭
cursor.close()
conn.close()
