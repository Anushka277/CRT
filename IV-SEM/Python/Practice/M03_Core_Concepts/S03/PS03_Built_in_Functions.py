#1) Find the largest number (using max())
'''
numbers = [3, 5, 1, 9, 2]
largest_number = max(numbers)   
print("The largest number is:", largest_number)
'''
#2) check Palindrome (using reversed() & join())
'''
s = iput("Enter a string: ")
reversed_s = ''.join(reversed(s))
if s == reversed_s:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
'''

#3)Count even numbera(using fliter())
'''
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  
print("Even numbers:", even_numbers)
print(len(even_numbers))
'''

#4) remove all the duplicates from a list (using set())
'''
a = [1, 2, 3, 2, 4, 1, 5]
print(set(a))
'''

#5)sum of digits(using sum())
'''
n = 12345
res = sum(int(digit) for digit in str(n))
print(res)
'''

#6) Sort words alphabetically (using sorted())
'''
a = ["banana", "apple", "cherry", "date"]
print(sorted(a))
'''

#7) Find the common elements (using set())
'''
a= [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8] 
res = set(a) & set(b)
print(res)
print(tuple(res))
'''
#8) Index with value (using enumerate())
'''
n = ["a", "b", "c", "d"]
for index, value in enumerate(n):
    print(index, value)
'''

#9) pair two lists (using zip())
'''
n = [1, 2, 3]
m = ['a', 'b', 'c'] 
res = list(zip(n, m))
print(res)
'''

#10)find second largest number (using sorted())
b = [3, 5, 1, 9, 2]
b.sort()
print(b[-2])