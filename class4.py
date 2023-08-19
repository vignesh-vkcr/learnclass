#classmethods and staticmethods

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


emp1=Employee("Corey","Anderson",1000)
emp2=Employee("Bill","Loferson",1250) 

Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

emp1.set_raise_amt(1.05)
# Above comment changes raise_amount for all employees. Eventhough we specified emp1.
# Reason is 'set_raise_amt' classmethod, which is common to all instents

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)