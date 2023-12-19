from util.implementation import DbConnection

class Payment(DbConnection):

    def init(self):
        self.PaymentID=''
        self.CourierID=''
        self.Amount=''
        self.PaymentDate=''

    def setter(self):
        self.PaymentID=int(input('Enter PaymentID:'))
        self.CourierID=int(input('Enter CourierID:'))
        self.Amount=input('Enter Amount:')
        self.PaymentDate=input('Enter PaymentDate:')
        data=[(self.PaymentID,self.CourierID,self.Amount,self.PaymentDate)]
        insert_str='''INSERT INTO Payment(PaymentID,CourierID,Amount,PaymentDate) VALUES (%s,%s,%s,%s)'''
        self.open()
        self.s.executemany(insert_str,data)
        self.conn.commit()
        print('Payment record inserted successfully..')
        self.close()

    def getter(self):
        self.open()
        select_str='''SELECT * FROM Payment'''
        self.s.execute(select_str)
        records=self.s.fetchall()
        print('')
        print('Records in New Payment Table')
        for i in records:
            print(i)
        self.close()

    def update(self):
        self.getter()
        ID=int(input('Enter PaymentID to be Updated: '))
        self.CourierID=int(input('Enter CourierID: '))
        self.Amount=input('Enter Amount: ')
        self.PaymentDate=input('Enter PaymentDate: ')

        update_str='''
            UPDATE Payment
            SET CourierID=%s,Amount=%s,PaymentDate=%s
            WHERE PaymentID=%s
        '''

        self.open()
        data=[(self.CourierID,self.Amount,self.PaymentDate,ID)]
        self.s.executemany(update_str,data)
        self.conn.commit()
        print('Record updated successfully..')
        self.close()

    def delete(self):
        PaymentID=int(input('Enter the PaymentID to be deleted: '))
        delete_str=f'DELETE FROM User WHERE PaymentID={PaymentID}'
        self.open()
        self.s.execute(delete_str)
        self.conn.commit()
        print('Record Deleted Successfully..')
        self.close()
#obj=Payment()
#obj.setter()
#obj.getter()
#obj.update()
#obj.delete()