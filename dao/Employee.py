from util.implementation import DbConnection

class Employee(DbConnection):

    def init(self):
        self.EmployeeID=''
        self.EmployeeName=''
        self.Email=''
        self.ContactNumber=''
        self.RoleString=''
        self.Salary=''

    def setter(self):
        self.EmployeeID=int(input('Enter EmployeeID:'))
        self.EmployeeName=input('Enter EmployeeName:')
        self.Email=input('Enter Email:')
        self.ContactNumber=int(input('Enter ContactNumber:'))
        self.RoleString=input('Enter RoleString:')
        self.Salary=input('Enter Salary:')
        data=[(self.EmployeeID,self.EmployeeName,self.Email,self.ContactNumber,self.RoleString,self.Salary)]
        insert_str='''INSERT INTO Employee(EmployeeID,EmployeeName,Email,ContactNumber,RoleString,Salary) VALUES (%s,%s,%s,%s,%s,%s)'''
        self.open()
        self.s.executemany(insert_str,data)
        self.conn.commit()
        print('Employee record inserted successfully..')
        self.close()

    def getter(self):
        self.open()
        select_str='''SELECT * FROM Employee'''
        self.s.execute(select_str)
        records=self.s.fetchall()
        print('')
        print('Records in New Employee Table')
        for i in records:
            print(i)
        self.close()

    def update(self):
        self.getter()
        ID=int(input('Enter EmployeeID to be Updated: '))
        self.EmployeeName=input('Enter EmployeeName: ')
        self.Email=input('Enter Email: ')
        self.ContactNumber=int(input('Enter ContactNumber: '))
        self.RoleString=input('Enter RoleString: ')
        self.Salary=input('Enter Salary: ')

        update_str='''
            UPDATE Employee
            SET EmployeeName=%s,Email=%s,ContactNumber=%s,RoleString=%s,Salary=%s 
            WHERE EmployeeID=%s
        '''

        self.open()
        data=[(self.EmployeeName,self.Email,self.ContactNumber,self.RoleString,self.Salary,ID)]
        self.s.executemany(update_str,data)
        self.conn.commit()
        print('Record updated successfully..')
        self.close()

    def delete(self):
        EmployeeID=int(input('Enter the EmployeeID to be deleted: '))
        delete_str=f'DELETE FROM User WHERE EmployeeID={EmployeeID}'
        self.open()
        self.s.execute(delete_str)
        self.conn.commit()
        print('Record Deleted Successfully..')
        self.close()
#obj=Employee()
#obj.setter()
#obj.getter()
#obj.update()
#obj.delete()