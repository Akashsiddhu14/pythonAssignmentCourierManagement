from util.implementation import DbConnection
class Employee(DbConnection):
    def init(self):
        self.EmployeeID=''
        self.EmployeeName=''
        self.Email=''
        self.ContactNumber=''
        self.RoleString=''
        self.Salary=''

    def create_table(self):
        create_str = '''
            CREATE TABLE IF NOT EXISTS Employee (
                EmployeeID INT PRIMARY KEY,
                EmployeeName VARCHAR(255),
                Email VARCHAR(255) UNIQUE,
                ContactNumber VARCHAR(20),
                RoleString VARCHAR(255),
                Salary VARCHAR(20)
            )
        '''
        self.open()
        self.s.execute(create_str)
        self.close()
        print('Employee table created successfully')

obj=Employee()
obj.create_table()