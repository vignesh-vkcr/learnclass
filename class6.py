#static method
# method connected to class but not connected instants of the class

class Employee:
    raise_amount=1.04
    No_of_emps=0
    def __init__(self,first,last,pay):
        self.first = first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'

        Employee.No_of_emps+=1
    def fullname(self):
        return self.first+' '+self.last
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)
    
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount=amount

    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return Employee(first,last,pay)
    
    @staticmethod
    def is_workday(day):
        #self, cls not required.
        if day.weekday()==5 or day.weekday()==6:
            return False
        else:
            return True




emp1=Employee("Corey","Anderson",1000)
emp2=Employee("Bill","Loferson",1250) 


import datetime

my_date=datetime.date(2016,7,11)

print(Employee.is_workday(my_date))

print(emp1.is_workday(my_date))

