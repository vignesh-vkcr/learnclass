#classmethod
#common to all instants of the class

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



emp1=Employee("Corey","Anderson",1000)
emp2=Employee("Bill","Loferson",1250) 

emp_str_l = ' John-Doe-70000'
emp_str_2= 'Steve-Smith-30000'
emp_str_3= 'Jane-Doe-90000'

# first, last, pay = emp_str_l.split('-')
# new_emp1=Employee(first,last,pay)

new_emp1=Employee.from_string(emp_str_l)

print(new_emp1.email)
print(new_emp1.pay)