import pymysql

#打开数据库连接
db = pymysql.connect(
    "mysql.datahunter.cn",   #数据库主机地址
    "test",                  #数据库主机名
    "Dh!7Test8",             #数据库密码
    "test"                   #数据库名
)

#使用cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

#SQL语句
sql = "select * from lina03"

#执行SQL语句
cursor.execute(sql)

#获取所有记录列表
result = cursor.fetchall()

#循环输出结果
for x in result:
    x = x[2]
    print(x)

#关闭数据库连接
db.close()



