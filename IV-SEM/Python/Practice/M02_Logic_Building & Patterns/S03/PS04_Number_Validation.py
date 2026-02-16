'''Armstrong Number: A number is called an Armstrong number if it is equal to the sum of its own digits each raised to the power of the number of digits. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153. Write a Python program to check if a given number is an Armstrong number or not.
input: 153
output: Armstrong number.

input: 24
output: not an Armstrong number.'''

n = int(input())
count = len(str(n))
s = 0
for digit in str(n):
    s += int(digit) ** count
print("Armstrong number" if s == n else "not an Armstrong number")    