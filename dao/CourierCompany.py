from util.implementation import DbConnection

class CourierCompany(DbConnection):

    def init(self):
        self.CompanyName=''
        self.CourierDetails=''
        self.EmployeeDetails=''
        self.LocationDetails=''

    def setter(self):
        self.CompanyName=input('Enter Company Name:')
        self.CourierDetails=input('Enter Courier Details:')
        self.EmployeeDetails=input('Enter Employee Details:')
        self.LocationDetails=input('Enter Location Details:')
        data=[(self.CompanyName,self.CourierDetails,self.EmployeeDetails,self.LocationDetails)]
        insert_str='''INSERT INTO CourierCompany(CompanyName,CourierDetails,EmployeeDetails,LocationDetails) VALUES (%s,%s,%s,%s)'''
        self.open()
        self.s.executemany(insert_str,data)
        self.conn.commit()
        print('CourierCompany record inserted successfully..')
        self.close()

    def getter(self):
        self.open()
        select_str='''SELECT * FROM CourierCompany'''
        self.s.execute(select_str)
        records=self.s.fetchall()
        print('')
        print('Records in NewUserTable')
        for i in records:
            print(i)
        self.close()

    def update(self):
        self.getter()
        name=input('Enter CompanyName to be Updated: ')
        self.CourierDetails=input('Enter CourierDetails: ')
        self.EmployeeDetails=input('Enter EmployeeDetails: ')
        self.LocationDetails=input('Enter LocationDetails: ')

        update_str='''
            UPDATE CourierCompany
            SET CourierDetails=%s,EmployeeDetails=%s,LocationDetails=%s
            WHERE CompanyName=%s
        '''

        self.open()
        data=[(self.CourierDetails,self.EmployeeDetails,self.LocationDetails,name)]
        self.s.executemany(update_str,data)
        self.conn.commit()
        print('Record updated successfully..')
        self.close()

    def delete(self):
        CompanyName=input('Enter the CompanyName to be deleted: ')
        delete_str=f'DELETE FROM User WHERE CompanyName={CompanyName}'
        self.open()
        self.s.execute(delete_str)
        self.conn.commit()
        print('Record Deleted Successfully..')
        self.close()

#obj=CourierCompany()
#obj.setter()
#obj.getter()
#obj.update()
#obj.delete()