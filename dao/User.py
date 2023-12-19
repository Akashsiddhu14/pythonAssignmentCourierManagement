from util.implementation import DbConnection

class User(DbConnection):

    def init(self):
        self.userId=''
        self.name=''
        self.email=''
        self.password=''
        self.contactNumber=''
        self.address=''

    def setter(self):
        self.userId=int(input('Enter UserID:'))
        self.name=input('Enter Name:')
        self.email=input('Enter Email:')
        self.password=input('Enter Password:')
        self.contactNumber=input('Enter Contact Number:')
        self.address=input('Enter Address:')
        data=[(self.userId,self.name,self.email,self.password,self.contactNumber,self.address)]
        insert_str='''INSERT INTO User(UserID,Name,Email,Password,ContactNumber,Address) VALUES (%s,%s,%s,%s,%s,%s)'''
        self.open()
        self.s.executemany(insert_str,data)
        self.conn.commit()
        print('User record inserted successfully..')
        self.close()

    def getter(self):
        self.open()
        select_str='''SELECT * FROM User'''
        self.s.execute(select_str)
        records=self.s.fetchall()
        print('')
        print('Records in NewUserTable')
        for i in records:
            print(i)
        self.close()

    def update(self):
        self.getter()
        ID=int(input('Enter UserID to be Updated: '))
        self.name=input('Enter Name: ')
        self.email=input('Enter Email: ')
        self.password=input('Enter Password: ')
        self.contactNumber=input('Enter Contact Number: ')
        self.address=input('Enter Address: ')

        update_str='''
            UPDATE User
            SET Name=%s,Email=%s,Password=%s,ContactNumber=%s,Address=%s 
            WHERE UserID=%s
        '''

        self.open()
        data=[(self.name,self.email,self.password,self.contactNumber,self.address,ID)]
        self.s.executemany(update_str,data)
        self.conn.commit()
        print('Record updated successfully..')
        self.close()

    def delete(self):
        userId=int(input('Enter the UserID to be deleted: '))
        delete_str=f'DELETE FROM User WHERE UserID={userId}'
        self.open()
        self.s.execute(delete_str)
        self.conn.commit()
        print('Record Deleted Successfully..')
        self.close()
#obj=User()
#obj.setter()
#obj.getter()
#obj.update()
#obj.delete()2