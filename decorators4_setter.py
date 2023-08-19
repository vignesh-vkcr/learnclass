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
    
    @fullname.setter
    def fullname(self, name):
        first,last=name.split(' ')
        self.first=first
        self.last=last



emp1=Employee("Corey","Anderson")

emp1.fullname='David Miller' 

# here I changed fullname. it does not affect the first and last name.
# But for me this need to update both first and last name too
# In this situations, we can use setters

print(emp1.first) 
print(emp1.last) 
print(emp1.email) # no parentheses
print("----------------------------------------")

