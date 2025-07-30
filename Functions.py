'''#User-defined Function
def hi():
    print("HI")
hi()
#user-defined Function with Arguments/Parameters
def summate(a,b):
    print("Sum of Two numbers:",a+b)
a=int(input("enter the value of a:"))
b=int(input("Enter the value Of b:"))
summate(a,b)
def summate(x,y):
    print("Sum of Two numbers:",x+y)
a=int(input("enter the value of a:"))
b=int(input("Enter the value Of b:"))
summate(a,b)
#user-defined Function with Arguments and return Values
def summate(a,b):
    return a+b
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
#print(summate(a,b))
result=summate(a,b)
print(result)     
#Default arguments
def sample(base,expo=2):
    return base ** expo
num=int(input("Enter the value of base"))
print(sample(num))
#print(sample(num,3))
#Multiple Return values for single values
def operate(a,b):
    return a+b,a-b,a*b
a=int(input("Enter a:"))
b=int(input("Enter b:"))
sum,diff,mul=operate(a,b)
print("SUM:",sum)
print("Subtract:",diff)
print("Multiply:",mul)
#Anoumous Function lambda
#SYNTAX=lambda var: operation/output operation
num=int(input("Enter the value of num:"))
square=lambda num:num*num
print(square(num))
#Nested Functions
def hi():
    def hello():
        print("Inner Function")
    print("Outer Function")
    hello()
hi()
#Example for the Nested Functions
def num(a,b):
    def add(a,b):
        print("Addition of two numbers:",a+b)
    print("Subtrate the two numbers:",a-b)
    add(5,5)
num(5,5)
#Eg-2
def operation(a,b):
    def add():
        return a+b
    def sub():
        return a-b
    print("Addition:",add())
    print("Subtract:",sub())
a=int(input("a:"))
b=int(input("b:"))
operation(a,b)'''
'''Write a program to calculate the factorial and power of given numbers by creation the nested loop with in loop where a = 5 and b = 3
calculate the factorial for a
calculate power for 5**3
Output: 
factorial = 120
power = 125'''
'''def calculate(a,b):
    def fact(a):
        res=1
        for i in range(1,a+1):
            res*=i
        return res
    def pow(a,b):
        return a**b
    print("Factorial:",fact(a))
    print("Power:",pow(a,b))
a=int(input("a:"))
b=int(input("b:"))
calculate(a,b)'''
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
def superfact(n):
    if n==1:
        return 1
    return fact(n)*superfact(n-1)
num=int(input("Enter the num:"))
print("Factorial",fact(num))
print("Factorial:",superfact(num))