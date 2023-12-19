from util.implementation import DbConnection
class Payment(DbConnection):
    def init(self):
        self.PaymentID=''
        self.CourierID=''
        self.Amount=''
        self.PaymentDate=''

    def create_table(self):
        #CHECK THE DATA TYPE
        create_str = '''
            CREATE TABLE IF NOT EXISTS Payment (
                PaymentID INT,
                CourierID INT,
                Amount VARCHAR(255), 
                PaymentDate DATE
            )
        '''
        self.open()
        self.s.execute(create_str)
        self.close()
        print('Payment table created successfully')

obj=Payment()
obj.create_table()