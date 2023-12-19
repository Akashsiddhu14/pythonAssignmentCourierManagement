from util.implementation import DbConnection
class Location(DbConnection):
    def init(self):
        self.LocationID=''
        self.LocationName=''
        self.Address=''

    def create_table(self):
        create_str = '''
            CREATE TABLE IF NOT EXISTS Location (
                LocationID INT PRIMARY KEY,
                LocationName VARCHAR(255),
                Address VARCHAR(255)
            )
        '''
        self.open()
        self.s.execute(create_str)
        self.close()
        print('Location table created successfully')

obj=Location()
obj.create_table()