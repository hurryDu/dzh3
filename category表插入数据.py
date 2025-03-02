import pymysql

#1.连接MySQL
conn=pymysql.connect(host="127.0.0.1",port=3306,user='root',password='123456',charset='utf8',db='gupiao')
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

# 2.发送指令
# cursor.execute("insert into b_user(uid,uname,upwd,usex,phone_number,id_number) values(28,'sss','123','n','123456','666666666666')")
# cursor.execute("insert into b_user(uname,upwd,usex,phone_number,id_number) values('mm','123','n','123456','666666666666')")

sql="insert into category(name,number) values(%s,%s)"
cursor.execute(sql,["川菜","35"])
conn.commit()
#3.关闭连接
cursor.close()
conn.close()