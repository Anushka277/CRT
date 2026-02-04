#loop is used to repeat a block of code multiple times until a certain condition is met.
'''
there are two main types of loops in Python:
1. for loop:
    Used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.
    syntax with range function:
        for i in range(start, stop, step):
            # code block to be executed
    syntax for iterable objects:
        for item in iterable: 
            # code block to be executed    
2. while loop:
    Repeats a block of code as long as a specified condition is true.
    syntax:
        while condition:
            # code block to be executed 
'''
# example using while loop:
'''counter = 0
while counter < 5:
    print("Hello, World!")
    counter += 1
'''
# write a program to print first n natural numbers using while loop in the same line
n = int(input())
count = 1
while count <= n:
    print(count, end=" ")
    count += 1  
# write a program to print first n natural numbers using while loop
n = int(input())
count = 1
while count <= n:
    print(count)
    count += 1
print()    
# write a program to print first n natural numbers using while loop in reverse order
#n = int(input())
j = n
while n >= 1:
    print(n, end=" ")
    n -= 1        
#display all the even numbers between start and stop using while loop  
start = int(input())  
stop = int(input())
while start <= stop:
    if start % 2 == 0:
        print(start, end=" ")
    start += 1