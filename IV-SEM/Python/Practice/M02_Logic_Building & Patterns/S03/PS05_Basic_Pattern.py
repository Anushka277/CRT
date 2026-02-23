'''input: 4
output:
* * * *
* * * *
* * * *
* * * *
'''
'''
n = int(input())
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
'''


'''input: 4
output:
*
* *
* * *
* * * *
'''

'''
n = int(input())
for i in range(n):  
    for j in range(i+1):
        print("*", end=" ")
    print()
'''

'''input: 4
output:
A
A B
A B C
A B C D'''    

'''
n = int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+j), end=" ")
    print()
'''

'''input: 4
output:
1
2 3
4 5 6
7 8 9 10 
'''
'''
n = int(input())
num = 1 
for i in range(n):
    for j in range(i+1):
        print(num, end=" ")
        num += 1
    print()
'''


'''
input : 4
output:
* * * *
*     *
*     *
* * * *
'''
'''
n = int(input())
for i in range(n):  
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
'''
Staircase in hackerank'''
n = int(input())
for i in range(n):
    for j in range(n):
        if j>=n-1-i:
            print("#", end="")
        else:
            print(" ", end="")
    print()