from util.implementation import DbConnection
class Courier(DbConnection):
    def init(self):
        self.CourierID =''
        self.SenderName =''
        self.SenderAddress =''
        self.ReceiverName =''
        self.ReceiverAddress =''
        self.Weight =''
        self.Status = ''
        self.TrackingNumber = ''
        self.DeliveryDate = ''
        self.UserId = ''
    def create_table(self):
        create_str = '''
            CREATE TABLE IF NOT EXISTS Courier (
                CourierID INT PRIMARY KEY,
                SenderName VARCHAR(255),
                SenderAddress TEXT,
                ReceiverName VARCHAR(255),
                ReceiverAddress TEXT,
                Weight FLOAT NOT NULL,
                Status VARCHAR(255),
                TrackingNumber VARCHAR(255) UNIQUE,
                Password VARCHAR(255),
                DeliveryDate DATE,
                UserId INT
            )
        '''
        self.open()
        self.s.execute(create_str)
        self.close()
        print('Courier table created successfully')

obj=Courier()
obj.create_table()