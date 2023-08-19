class Employee:
    raise_amount=1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
    def fullname(self):
        return self.first+' '+self.last
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)


emp1=Employee("Corey","Anderson",1000)
emp2=Employee("Bill","Loferson",1250)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

print(emp1.raise_amount)
print(Employee.raise_amount)

print(emp1.__dict__)
print(Employee.__dict__)

emp1.raise_amount=1.05
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)

print(emp1.__dict__)