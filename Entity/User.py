#create the same python packages for all class
from util.implementation import DbConnection
class User(DbConnection):
    def init(self):
        self.UserID=''
        self.Name=''
        self.Email=''
        self.Password=''
        self.ContactNumber=''
        self.Address=''

    def create_table(self):
        create_str = '''
            CREATE TABLE IF NOT EXISTS User (
                UserID INT PRIMARY KEY,
                Name VARCHAR(255),
                Email VARCHAR(255) UNIQUE,
                Password VARCHAR(255),
                ContactNumber VARCHAR(20),
                Address TEXT
            )
        '''
        self.open()
        self.s.execute(create_str)
        self.close()
        print('User table created successfully')

obj=User()
obj.create_table()