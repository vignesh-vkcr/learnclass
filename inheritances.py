#inheritances
# 

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

class Developer(Employee):
    # Developer class now have all of the personalities of the Employee class
    # Also developer class have the following unique options
    # Developer also the Employee with specialised in developing
    raise_amount=1.10
    



emp1=Employee("Corey","Anderson",1000)
emp2=Employee("Bill","Loferson",1250) 

dev1=Developer("Wan","Hanson",2000)

# print(help(Developer))

print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)

print(dev1.raise_amount) # take raise amount from Developer class. Developer class inherts Emploee class. Still 1st priority to its own objects.
print(emp1.raise_amount) # take raise amount from Employee class