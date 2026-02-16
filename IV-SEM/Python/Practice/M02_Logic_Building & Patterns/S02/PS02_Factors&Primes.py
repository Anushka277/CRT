'''Read a number from the user and print all the factors of that number.
input: 12
output: 1 2 3 4 6 12'''

'''
#accepting input from user
num = int(input("Enter a number: "))
for i in range(1, num + 1): 
    if num % i == 0:
        print(i, end=" ")


num = int(input("Enter a number: "))
for i in range(1, num//2 + 1):
    if num % i == 0:
        print(i, end=" ")   
print(num)
'''


'''Read a number from the user and count the given numbers of factors for the given number.
'''
'''
num = int(input("Enter a number: "))
count = 0       
for i in range(1, num + 1): 
    if num % i == 0:
        count += 1
print(count)
'''


'''Read a number from the user and check whether the given number is prime or not.'''
'''
#one way
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

#another way
num = int(input("Enter a number: "))
counter = 0
for i in range(2,num//2+1):
    if num % i == 0:
        counter += 1
print("prime" if counter == 0 else "not prime")
'''



'''read a number from the user and print all the prime numbers between 1 to that number.(in a simple way)'''
'''start = int(input())
end = int(input())
if start == 1:
    start = 2
for num in range(start, end + 1):
   counter = 0
   for i in range(2, num//2 + 1):
       if num % i == 0:
           counter += 1
    if counter == 0:
           print(num, end=" ")   
'''


'''read a number from the user and print factorial of that number.'''
'''
# all
num = int(input("Enter a number: "))
factorial = 1           
for i in range(1, num + 1):
    factorial *= i
print(factorial)

#no fact for -ve
if num < 0:
    print("Factorial does not exist for negative numbers")          
elif num == 0:
    print(1)
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(factorial)            
'''



'''read a number from the user and print the gcd of two numbers.'''

'''
num = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))  
while num2:
    num, num2 = num2, num % num2
print("GCD is", num)

#only for python
import math
print(math.gcd(num,num2))
'''

