class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
    def fullname(self):
        return self.first+' '+self.last


emp1=Employee("Corey","Anderson",1000)
emp2=Employee("Bill","Loferson",1250)

print(emp1.first)
print(emp1.email)

print(emp1.fullname())
#or
print(Employee.fullname(emp1))