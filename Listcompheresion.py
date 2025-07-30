'''List comprehension...input Version..
Manual Input:[5,7,4,3]
for i in range(11):
    num=int(input())
    v=append.num
    print(i,end=' ')'''
#step-by-step input of LC
"""nums=[int(input(f"Enter the number {i+1}:")) for i in range(1,5)]
print(nums)"""
'''n=[int(x) for x in input("Enter 5 numbers with space").split()[:5]]
print(n)'''
#nested LC... loop within loop in a single:LC
'''n=int(input("Enter the table size n:"))
table=[[i*j for j in range(1,n+1)]for i in range(1,n+1)]
print("Tables of Math ")
for row in table:
    print(row)'''
'''Create a nXn matrix with manual input numbers ny input seperated spaces
print all the rows in LC only'''
n=input("Enter 9 numbers with space").split()
if len(n)!=9:
    print("Enter exactly 9 numbers:")
else:
    num=[int(x) for x in n]
    matrix=[[num[i*3+j]for j in range(3)] for i in range(3)]
    for r in matrix:
        print(r)'''
#Transpose of a matrix
'''n=input("Enter 9 numbers with space").split()
if len(n)!=9:
    print("Enter exactly 9 numbers:")
else:
    num=[int(x) for x in n]
    matrix=[[num[i*3+j]for j in range(3)] for i in range(3)]
    transpose=[[matrix[i][j] for i in range(3)]for j in range(3)]
    for r in matrix:
        print(r)
    for r in transpose:
        print(r)'''"""
 Mostly asked interview question
[[1,2,3],[1,4,6],[2,4,6]]
flatten n/n array"""
'''n=int(input("Enter the value of nXn size:"))
num=[int(x) for x in input("Enter numbers").split()[:n*n]]
matrix=[[num[i*n+j] for j in range(n)]for i in range(n)]
for k in matrix:
    print(k)
flat=[k for r in matrix for k in r]
print(flat)'''
#Code to consider a LC: to calculate square of 16 values as nXn matrix and print the list of squares in each row:
'''I/p:3=9values
1 2 3 
4 5 6
7 8 9
o/P:[1,4,9]
[16,25,36][49,64,81]'''
'''n=int(input("Enter the value of nXn size:"))
num=[int(x) for x in input("Enter numbers").split()[:n*n]]
matrix=[[num[i*n+j]**2 for j in range(n)]for i in range(n)]
for k in matrix:
    print(k)
flat=[k for r in matrix for k in r]
print(flat)'''
"""I/p:
1 2 3 
4 5 6
7 8 9
O/p: 
0 2 0
4 0 6
0 8 0"""
'''n=int(input("Enter the value of nXn size:"))
num=[int(x) for x in input("Enter numbers").split()[:n*n]]
matrix=[[num[i*n+j] if num[i*n+j]%2==0 else 0 for j in range(n)]for i in range(n)]
for k in matrix:
    print(k)
flat=[k for r in matrix for k in r]
print(flat)'''
'''n=int(input("Enter the value of nXn size:"))
num=[int(x) for x in input("Enter numbers").split()[:n*n]]
matrix=[[num[i*n+j] if num[i*n+j]%2!=0 else 0 for j in range(n)]for i in range(n)]
for k in matrix:
    print(k)
flat=[k for r in matrix for k in r]
print(flat)'''
"""print oddd for value "1" even for value "0""""
n=int(input("Enter the value of nXn size:"))
num=[int(x) for x in input("Enter numbers").split()[:n*n]]
#matrix=[[num[i*n+j] if num[i*n+j]%2!=0 else 0 for j in range(n)]for i in range(n)]
matrix = [["1" if num[i*n+j]%2!=0 else "0" for j in range(n)] for i in range(n)]
for k in matrix:
    print(k)
flat=[k for r in matrix for k in r]
print(flat)
