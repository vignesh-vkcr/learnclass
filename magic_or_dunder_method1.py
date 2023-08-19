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

    #def __str__(self):
    #    pass

    



emp1=Employee("Corey","Anderson",1000)
emp2=Employee("Bill","Loferson",1250) 

print(emp1) #try print this without __repr__. to know what __repr__ doing.




