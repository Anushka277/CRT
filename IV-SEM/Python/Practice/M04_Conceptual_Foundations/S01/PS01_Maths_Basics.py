#GCD(Traditional Method)
'''
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
a = int(input())
b = int(input())
print(gcd(a, b))
'''
#sol 1

'''
a = int(input())
b = int(input())
min_val= min(a,b)
gcd = 1
for i in range(1,min_val):
    if a%i == 0 and b%i==0:
        gcd = i
print(gcd)  
'''   

'''
#solution 2
while b!=0:
    a, b = b, a % b
print(a)
'''

#sol3
'''
import math
a = int(input())
b = int(input())
print(math.gcd(a, b))
'''
#lcm of two numbers(traditional method)
'''
a = int(input())
b = int(input())
x,y = a,b
while y !=0:
    a, b = y, x % y
gcd = x
lcm = (a*b)//gcd
print(lcm)
'''

#perfect numbers
n = int(input())
s = 0
for i in range(1,n//2+1):
    if n%1==0:
        s+=1
print("perfect no." if n==s else "not perfect no.")         




