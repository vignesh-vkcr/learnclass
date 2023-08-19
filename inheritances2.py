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
    



emp1=Employee("Corey","Anderson",1000)
emp2=Employee("Bill","Loferson",1250) 

dev1=Developer("Wan","Hanson",2000,'Python')

# print(help(Developer))

print(dev1.email)

print(dev1.prog_lang)