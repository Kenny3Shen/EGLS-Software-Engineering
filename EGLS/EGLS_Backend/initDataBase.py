import pymysql

initDB = '''
    CREATE DATABASE user
'''

create_userdata = '''
    CREATE TABLE userdata
    (
        username varchar(32) PRIMARY KET NOT NULL,
        password varchar(128) NOT NULL
    )ENGINE=InnoDB
'''
con = pymysql.connect(host="localhost", user="shen", password="123456")
cursor = con.cursor()
cursor.execute(initDB)
cursor.execute(create_userdata)
con.commit()
cursor.close()
con.close()
