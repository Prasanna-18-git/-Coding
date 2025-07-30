#Object-oriented Programming
"""class abc:
    value=9
obj1=abc()
print(obj1.value)"""
'''class abc():
    value1=9
    value2=10
    def display(self):
        print("This is a CLASS Method")
obj1=abc()
print(obj1.value1)
obj1.display()
obj1.display()
print(obj1.value2)'''
'''class abc():
    def __init__(self,value):
        print("This is a class method")
        self.value=value
        print("Accessing value in class is",value)
num=int(input(":"))
obj=abc(num)'''
#Example for init method
'''class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def hi(self):
        print(f"HELLO,I am {self.name} and I am {self.age} years old")
s=student('Prasanna',15)
s.hi()'''
#own created
'''class dog():
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def sleep(self):
        print(f"I am {self.name},i am {self.gender} and iam sleeping Zzzzzzz............")
    def bark(self):
        print(f"I am {self.name} iam barking for Food!!!!!!!!!")
d=dog('jule','Male')
d.sleep()
d=dog('chik','Female')
d.bark()'''
'''Write a Code to calculate the area of a circle by importing pi from math and create a class for circle with a constructor, while radius is considered as an arg calculate and return the value to the object'''
'''import math
class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
    def circumference(self):
        return 2*math.pi*r
r=int(input("Enter the r:"))
c=circle(r)
print(f"Area of circle:{c.area():.2f}")
print(f"circumference of circle: {c.circumference():.2f}")'''
"""Write a Code to find and print the factorial of a given number using a class called Math and register the given number in a constructor to calculate. return the value by passing to the main function"""
'''class Math:
    def __init__(self,n):
        self.n=n
    def fact(self):
        f=1
        for i in range(1,self.n+1):
            f*=i
        return f
n=int(input("Enter the n:"))
m=Math(n)
print("factorial",m.fact())'''
'''Write a Code to import the sqrt function and calculation the value by creating a class Squareroot and define a function for finding the root.  return the value to the main program'''
'''import math
class Squareroot:
    def __init__(self,r):
        self.r=r
    def  sqr(self):
        return math.sqrt(self.r)
r=int(input("Enter r:"))
s=Squareroot(r)
print(f"Squareroot:{s.sqr():.2f}")'''
#Instances Variables
'''Capgeminie interview question --->Write a Code to modify a mutable list using a class number for accumulating even/odd values into a list return the even list and odd list with last modified element'''
'''I/P:Eg:abc(11)
abc(22)
abc(33)'''
class number:
    even=[]
    odd=[]
    def __init__(self,n):
        self.n=n
        if n%2==0:
            number.even.append(n)
        else:
            number.odd.append(n)
n1=number(21)
n2=number(33)
n3=number(32)
n4=number(38)
n5=number(56)
n6=number(47)
print("Even list",number.even)
print("Odd list",number.odd)
