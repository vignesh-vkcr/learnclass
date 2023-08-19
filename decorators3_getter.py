class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last=last
    
    @property #by using property decorator, we can avoid parentheses while calling
    def email(self):
        return self.first+'.'+self.last+'@company.com'
    
    @property
    def fullname(self):
        return self.first+' '+self.last


emp1=Employee("Corey","Anderson")
emp2=Employee("Bill","Loferson")

print(emp1.first)
print(emp1.email) # no parentheses
print(emp1.fullname) # no parentheses
print("----------------------------------------")

emp1.first='Jimmy'
print(emp1.first) 
print(emp1.email) # no parentheses
print("----------------------------------------")

