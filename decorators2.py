class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last=last
    
    def email(self):
        return self.first+'.'+self.last+'@company.com'

    def fullname(self):
        return self.first+' '+self.last


emp1=Employee("Corey","Anderson")
emp2=Employee("Bill","Loferson")

print(emp1.first)
print(emp1.email())
print(emp1.fullname())
print("----------------------------------------")

emp1.first='Jimmy'
print(emp1.first) 
print(emp1.email()) 
print("----------------------------------------")

# now email is also updated. But need to use parentheses to call email.
# there is a option to call method without parentheses. for that refer 'decorators3.py)

