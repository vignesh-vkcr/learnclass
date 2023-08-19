#inheritances
# 

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

class Developer(Employee):
    raise_amount=1.10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        #or you can following
        #Employee.__init__(self,first,last,pay)

        self.prog_lang=prog_lang
    
class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def rem_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->',emp.fullname())



emp1=Employee("Corey","Anderson",1000)
emp2=Employee("Bill","Loferson",1250) 

dev1=Developer("Wan","Hanson",2000,'Python')
dev2=Developer("Philipi","Brandon",1900,'Python')

mgr1=Manager('Sue','Smith',90000,[dev1])

print(mgr1.email)
print('--------------------')

mgr1.print_emp()
print('--------------------')

mgr1.add_emp(dev2)
mgr1.add_emp(emp1)

mgr1.print_emp()
print('--------------------')

mgr1.rem_emp(dev1)

mgr1.print_emp()
print('--------------------')