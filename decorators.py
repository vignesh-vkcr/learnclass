class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last=last
        self.email=first+'.'+last+'@company.com'

    def fullname(self):
        return self.first+' '+self.last


emp1=Employee("Corey","Anderson")
emp2=Employee("Bill","Loferson")

print(emp1.first)
print(emp1.email)
print(emp1.fullname())
print("----------------------------------------")

emp1.first='Jimmy'
print(emp1.first) # first name updated
print(emp1.email) # But email is not updated. 
print("----------------------------------------")

#in those situations, properties decorators helps. chk 'decorators2.py'

