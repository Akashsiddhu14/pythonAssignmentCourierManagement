from util.implementation import DbConnection
class CourierCompany(DbConnection):
    def init(self):
        self.CompanyName=''
        self.CourierDetails=''
        self.EmployeeDetails=''
        self.LocationDetails=''
    def create_table(self):
        create_str = '''
            CREATE TABLE IF NOT EXISTS CourierCompany (
                CompanyName VARCHAR(255),
                CourierDetails VARCHAR(255),
                EmployeeDetails VARCHAR(255),
                LocationDetails VARCHAR(255)
            )
        '''
        self.open()
        self.s.execute(create_str)
        self.close()
        print('Courier Company table created successfully')

obj=CourierCompany()
obj.create_table()