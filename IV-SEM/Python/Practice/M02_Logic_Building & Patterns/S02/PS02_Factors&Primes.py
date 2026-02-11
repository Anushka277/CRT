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
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")