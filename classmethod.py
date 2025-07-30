classmethod
'''class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(f"Student name: {self.name}")
        print(f"Student Marks: {self.marks}")
name=input("Name:")
marks=int(input("Marks:"))
s=student(name,marks)
s.display()'''
#Implementation of classmethod
'''class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @classmethod  
    def input(cls):
       name=str(input("Name:"))  
       marks=int(input("Marks:"))
       return cls(name,marks)        
    def display(self):
        print(f"Student name: {self.name}")
        print(f"Student Marks: {self.marks}")
stu=student.input()
stu.display()'''
"""Write a code to illustrate a product with its prize by normal instance and calculate the product Tax rate by 10% in a classmethod and print the total amount to be paid....."""
'''class product:
    tax_rate=0.10
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def finalprice(self):
        total=self.price * (1+product.tax_rate)
        print(f"Final price of {self.name} is Rs.{total:.2f}")
    @classmethod
    def settax(cls,rate):
        cls.tax_rate=rate/100
name=str(input("Enter the product name:"))
price=float(input("Enter to the base prize:"))
rate=int(input("Enter the tax_rate in %:"))
product.settax(rate)
item=product(name,price)
item.finalprice()'''
#Basic math operation using classmethod
#Simple math Complex evaluation
'''class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    @classmethod
    def input(cls):
        a=int(input("Enter the value of a:"))
        b=int(input("Enter the value of b:"))
        return cls(a,b)
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
c=Calculator.input()
print("Addition result:",c.add())
print("Subctration result:",c.sub())
print("Multiplication result:",c.mul())
print("Division result:",c.div())'''
#Above Program in the Simpler way
'''class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    @classmethod
    def input(cls):
        a=int(input("Enter the value of a:"))
        b=int(input("Enter the value of b:"))
        return cls(a,b)
    def op(self):
        print("Addition result:",self.a + self.b)
        print("Subctration result:",self.a - self.b)
        print("Multiplication result:",self.a * self.b)
        print("Division result:",self.a / self.b)
c=Calculator.input()
c.op()'''
#Static Methods
"""static method @static method"""
'''class Student:
    gender= 'Male'
    def __init__(s,name):
        s.name=name
    def display(s):
        print(f"Name: {s.name}")
    @classmethod
    def getname(cls):
        return cls.gender
    @staticmethod
    def resident(type_of_resident):
        if type_of_resident.lower()=='Indian':
            return "The person is Indian"
        else:
            return "The person is not Indian"
name=str(input("Enter the name:"))
type=input("Enter the resident or non-resident:")
s=Student(name)
s.display()
print("Student_gender:",Student.getname())
print(s.resident(type))'''
'''class op:
    @staticmethod
    def add(x,y):
        return x+y
x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))    
print("Sum:",op.add())'''
'''class op:
    @staticmethod
    def operate(x,y):
        print("Sum:"x+y)
        print("Diff:"x-y)
x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
op.operate(x,y)'''
class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a + self.b
    @staticmethod
    def input(cls):
        a=int(input("Enter the value of a:"))
        b=int(input("Enter the value of b:"))
        return cls(a,b)
    @staticmethod
    def mul(x,y):
        return x*y
c=Calc.input()
print("Addition-Instance",c.add())
x=int(input("Enter the value of MUl:"))
y=int(input("Enter the value of another number:"))
print("Mul-Static",c.mul(x,y))