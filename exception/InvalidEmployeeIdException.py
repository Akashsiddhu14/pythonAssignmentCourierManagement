class InvalidEmployeeIdException(Exception):
    def __init__(self,message="Invalid employee ID"):
        self.message=message
        super().__init__(self.message)

class Employee:
    def __init__(self,employee_id,name,email,contact_number,role,salary):
        self.EmployeeID=employee_id
        self.Name=name
        self.Email=email
        self.ContactNumber=contact_number
        self.Role=role
        self.Salary=salary

def get_employee_by_id(employee_list,employee_id):
    for employee in employee_list:
        if employee.EmployeeID==employee_id:
            return employee
    raise InvalidEmployeeIdException()


employee_list=[Employee(201, "John Doe","john@example.com","1234567890","Manager",50000.00),
                Employee(202,"Jane Smith","jane@example.com","9876543210","Developer",60000.00)]
class EmployeeException:
    def RaiseException(self):
        try:
            employee_id_to_find=int(input("Enter employee_id"))
            found_employee=get_employee_by_id(employee_list,employee_id_to_find)
            print(f"Employee found: {found_employee.Name}")
        except InvalidEmployeeIdException:
            print("Invalid employee ID. Employee not found.")
obj8=EmployeeException()
obj8.RaiseException()