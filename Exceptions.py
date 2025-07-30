# Exceptional Handlers
"""sample:def add(a,b):
    return(a+b)
add(a,b)"""
"""sample:a=int(input("a:"))
b=int(input())
c=a+b
print(c)
o/p: a:presed unwanted key
Error:....."""
#Program to handle Zero division Error
"""num=int(input("Numerator:"))
deno=int(input("Denominator:"))
try:
    quo=num/deno
    print("Quotient:",quo)
except ZeroDivisionError:
    print("Denominator can't be a Zero.........check!!!!!")"""
#Program to handle multiple exceptions
"""try:
    num=int(input("Enter:"))
    print(num**3)
except(KeyboardInterrupt):
    print("You shold have entered data wit out interupting the compiler")
except(ValueError):
    print("Enter the number only")
print("Program terminaed")
print("BYE!!!!!")"""
#Program on handling mutiple Exceptions in an Single Line
"""try:
    num=int(input("Enter:"))
    print(num**3)
except(KeyboardInterrupt,ValueError,TypeError):
    print("Check Before Entering the data")
print("Program terminaed")
print("BYE!!!!!")"""
#Using else statement with the exception Handling
"""try:
    file=open('file1.txt')
    str=file.readlines()
    print(str)
except IOError:
    print("Error occured due to the input")
except ValueError:
    print("Couldnot convert to integer")
else:
    print("Program Executed Successfully.")"""
#Using rasie
"""try:
    num=100
    print(num**4)
    raise ValueError
except:
    print("Exception Occurred ...............")"""
#Re-rase an Exception
"""try:
    raise NameError
except:
    print("Re-rasing an Exception!!!")
    raise """
'''MMimp Code is to nitiate the process of exeption'''
try:
    raise Exception('Vijay','EEE')
except Exception as erorrObj:
    print(type(erorrObj))
    print(erorrObj.args)
    arg1,arg2=erorrObj.args
    print("2nd argument",arg2)
    print("1st argument",arg1)