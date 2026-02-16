'''Armstrong Number: A number is called an Armstrong number if it is equal to the sum of its own digits each raised to the power of the number of digits. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153. Write a Python program to check if a given number is an Armstrong number or not.
input: 153
output: Armstrong number.

input: 24
output: not an Armstrong number.'''

'''n = int(input())
count = len(str(n))
s = 0
for digit in str(n):
    s += int(digit) ** count
print("Armstrong number" if s == n else "not an Armstrong number")    
'''

# perfect number 
'''perfect number: A number is called a perfect number if it is equal to the sum of its proper divisors (excluding itself). For example, 6 is a perfect number because its proper divisors are 1, 2, and 3, and their sum is 6. Write a Python program to check if a given number is a perfect number or not.
input: 6
output: perfect number
6 ====>1,2,3
1+2+3 = 6'''

'''
n = int(input())
sum = 0
for i in range(1,n):
    if n%i == 0:
        sum += i
if sum == n:
    print("Perfect number")
else:
    print("not a perfect number")
'''


#strong number
'''strong number:
input: 123
output: not a strong number

Explanation: 1! + 2! + 3! = 1 + 2 + 6 = 9'''

def factorial(n):
    if n<0:
        return "no factorial for -ve"
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1,n+1):
            fact = fact * i
        return fact
    
n = int(input())
sum = 0
for digit in str(n):
    sum += factorial(int(digit))
        


