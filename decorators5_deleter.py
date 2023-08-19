class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last=last
    
    @property #by using property decorator, we can avoid parentheses while calling
    def email(self):
        if self.first!=None and self.last!=None:
            return self.first+'.'+self.last+'@company.com'
        else:
            return None
    
    @property
    def fullname(self):
        if self.first!=None and self.last!=None:
            return self.first+' '+self.last
        else:
            return None
    
    @fullname.setter
    def fullname(self, name):
        first,last=name.split(' ')
        self.first=first
        self.last=last

    @fullname.deleter
    def fullname(self):
        print('Name Deleted!')
        self.first=None
        self.last=None


emp1=Employee("Corey","Anderson")

print(emp1.first) 
print(emp1.last) 
print(emp1.fullname)
print(emp1.email)
print("----------------------------------------")

del emp1.fullname
print(emp1.first) 
print(emp1.last)
print(emp1.fullname)
print(emp1.email)