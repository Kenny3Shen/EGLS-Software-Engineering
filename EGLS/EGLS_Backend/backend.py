import pymysql


class MySQL:
    def __init__(self, sql, database='User'):
        self.database = database
        self.sql = sql
        self.result = None

    def exe(self):
        con = pymysql.connect(host="localhost", user="root", password="123456", database=self.database)
        cursor = con.cursor()
        cursor.execute(self.sql)
        self.result = cursor.fetchall()
        con.commit()
        cursor.close()
        con.close()

    def getData(self) -> tuple:
        return self.result
