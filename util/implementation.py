#write a data base interation code here.
import mysql.connector as sql
class DbConnection:

    def open(self):
        try:
            self.conn = sql.connect(host='localhost',database='courier_management_system',user='root',password='akash1436')
            self.s = self.conn.cursor()
            print("Database is connected")
        except Exception as e:
            print(str(e) + "---Database is not Connected:--")

    def close(self):
        self.conn.close()
        print('Connection Close:')

obj=DbConnection()
obj.open()
obj.close()