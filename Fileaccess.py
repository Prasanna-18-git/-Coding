File Accessing
'''with open("file.txt",'r') as file:
    data=file.read()
    print("Access from out Source",data)'''
'''with open('file.txt','r') as file:
    data=file.read()
    print(data
with open('file.txt','a+') as file:
    lines=file.readlines()
print("Lines list:",lines))
with open('file.txt','r') as file:
    print(file.readline(20))'''
with open('file.txt','r') as file:
    data=file.read()
    print(data)
    print(file.closed)
    file.close()
    print(file.closed)