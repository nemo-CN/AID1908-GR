"""

"""
import pymysql

class Database:
    def __init__(self):
    # 连接数据库
    db= pymysql.connect(host='localhost',
                        port= 3306,
                        user ='root',
                        password ='123456',
                        database ='test',
                        charset ='utf8')

    # 生成游标对象（操作数据库，执行ssql语句）
    cur = self.db.cursor()

    # 执行各种多数据库的读写操作
    # 走～


    # 关闭游标和数据库连接
    def close(self):
        self.cur.close()
        self.db.close()

    def register(self,name,passwd):
        sql="select name from user where name=%s;"
        self.cur.execute(sql,[name])
        result = self.cur.fetchone()
        if result:
            print("存在")
            return
    try:
        sql="insert into user (name,passwd)values(%s,%s);"
        self.cur.execute(sql,[name,passwd])

if __name__ == '__main__':
