from dao.Employee import Employee
from dao.Courier import Courier
from dao.CourierCompany import CourierCompany
from dao.Location import Location
from dao.Payment import Payment
from dao.User import User
from util.implementation import DbConnection
try:
    conn=DbConnection()
    conn.open()
    obj=Employee()
    #obj.getter()
    #obj.setter()
    #obj.update()
    #obj.delete()

    obj_1=Courier()
    #obj_1.getter()
    #obj_1.setter()
    #obj_1.update()
    #obj_1.delete()

    obj_2=CourierCompany()
    obj_2.getter()
    # obj_2.setter()
    # obj_2.update()
    # obj_2.delete()

    obj_3=Location()
    #obj_3.getter()
    #obj_3.setter()
    #obj_3.update()
    #obj_3.delete()

    obj_4=Payment()
    #obj_4.getter()
    #obj_4.setter()
    #obj_4.update()
    #obj_4.delete()

    obj_5=User()
    #obj_5.getter()
    #obj_5.setter()
    #obj_5.update()
    #obj_5.delete()


except Exception as e:
    print(e)
finally:
    conn.close()