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


emp1=Employee("Corey","Anderson",1000)
emp2=Employee("Bill","Loferson",1250)

print(Employee.No_of_emps)

emp3=Employee("Wis","Lilly",3000)

print(Employee.No_of_emps)
