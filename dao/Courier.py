from util.implementation import DbConnection

class Courier(DbConnection):

    def init(self):
        self.courierID=''
        self.senderName=''
        self.senderAddress=''
        self.receiverName=''
        self.receiverAddress=''
        self.weight=''
        self.status= ''
        self.trackingNumber= ''
        self.deliveryDate= ''
        self.userId= ''

    def setter(self):
        self.courierID=int(input('Enter CourierID:'))
        self.senderName=input('Enter SenderName:')
        self.senderAddress=input('Enter SenderAddress:')
        self.receiverName=input('Enter ReceiverName:')
        self.receiverAddress=input('Enter ReceiverAddress:')
        self.weight=float(input('Enter Weight:'))
        self.status=input('Enter Status:')
        self.trackingNumber=int(input('Enter TrackingNumber:'))
        self.deliveryDate= input('Enter deliveryDate:')
        self.userId= int(input('Enter userId:'))
        data=[(self.courierID,self.senderName,self.senderAddress,self.receiverName,self.receiverAddress,self.weight,self.status,self.trackingNumber,self.deliveryDate,self.userId)]
        insert_str='''INSERT INTO Courier(courierID,senderName,senderaddress,receivername,receiveraddress,weight,status,trackingnumber,deliverydate,userId) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        self.open()
        self.s.executemany(insert_str,data)
        self.conn.commit()
        print('Courier record inserted successfully..')
        self.close()

    def getter(self):
        self.open()
        select_str='''SELECT * FROM Courier'''
        self.s.execute(select_str)
        records=self.s.fetchall()
        print('')
        print('Records in New Courier Table')
        for i in records:
            print(i)
        self.close()

    def update(self):
        self.getter()
        ID=int(input('Enter courierID to be Updated: '))
        self.senderName = input('Enter SenderName:')
        self.senderAddress = input('Enter SenderAddress:')
        self.receiverName = input('Enter ReceiverName:')
        self.receiverAddress = input('Enter ReceiverAddress:')
        self.weight = float(input('Enter Weight:'))
        self.status = input('Enter Status:')
        self.trackingNumber = int(input('Enter TrackingNumber:'))
        self.deliveryDate = input('Enter DeliveryDate:')
        self.userId = int(input('Enter UserId:'))

        update_str='''
            UPDATE Courier
            SET senderName=%s,senderAddress=%s,receiverName=%s,receiverAddress=%s,weight=%s,status=%s,trackingNumber=%s,deliveryDate=%s,userId=%s
            WHERE courierID=%s
        '''

        self.open()
        data=[(self.senderName,self.senderAddress,self.receiverName,self.receiverAddress,self.weight,self.status,self.trackingNumber,self.deliveryDate,self.userId,ID)]
        self.s.executemany(update_str,data)
        self.conn.commit()
        print('Record updated successfully..')
        self.close()

    def delete(self):
        courierID=int(input('Enter the courierID to be deleted: '))
        delete_str=f'DELETE FROM Courier WHERE courierID={courierID}'
        self.open()
        self.s.execute(delete_str)
        self.conn.commit()
        print('Record Deleted Successfully..')
        self.close()
#obj=Courier()
#obj.setter()
#obj.getter()
#obj.update()
#obj.delete()