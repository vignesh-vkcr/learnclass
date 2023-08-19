#magic/dunder methods

#__init__ is one dunder/magic/special method

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

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)

    def __str__(self):
       #__str__ required __repr__ to work
       return '{}-{}'.format(self.fullname(),self.email)
    
    def __add__(self,other):
        return self.pay+other.pay
    
    def __len__(self):
        return len(self.fullname())

    



emp1=Employee("Corey","Anderson",1000)
emp2=Employee("Bill","Loferson",1250) 

print(1+2)
print(int.__add__(1,2))
print("----------------------------------------")

print('a'+'b')
print(str.__add__('a','b'))
print("----------------------------------------")

#using above example, we are going to create dunder method to add employees salaries

print(emp1+emp2) # try this without __add__ dunder method
print("----------------------------------------")

print(len('test'))
print('test'.__len__())
print("----------------------------------------")

#using above example, we are going to create dunder method to find length of employee full name
print(len(emp1)) # try this without __len__ dunder method
print("----------------------------------------")