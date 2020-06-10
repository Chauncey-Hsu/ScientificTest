# 导入MySQL驱动:
import mysql.connector

# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='root', password='MyNewPass', database='test')

cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user_python (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user_python (id, name) values (%s, %s)', ['3', 'Sophie'])
print(cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user_python')
# cursor.execute('select * from user_python where id = %s', ('1',))
values = cursor.fetchall()
print(values)

# 关闭Cursor和Connection:
cursor.close()
conn.close()

for item in values:
    print(item[0], item[1])
