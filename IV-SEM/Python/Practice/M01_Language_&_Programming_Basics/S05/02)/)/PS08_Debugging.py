'''
02/02/2026

'''

'''
find the bug(s) in the following code and fix them. is called debugging.
Types of errors:
1) Syntax errors: due to incorrect syntax(missing colon, wrong indentation, misspelled keywords)
--> eg: if x = 10 print(x)  # incorrect syntax
2) Logical errors: due to wrong logic
--> eg: finding average of 3 numbers but dividing by 2
3) Runtime errors: occur during program execution(dividing by zero, file not found)

Debugging techniques:

1) Print statements: inserting print statements to check variable values at different stages.
2) Using a debugger: step through code, inspect variables, set breakpoints.
3)try-except blocks: handle runtime errors gracefully.
4)using of pdb module: Python's built-in debugger for interactive debugging.

'''
'''
#print statements
a=int(input("Enter a"))
b=int(input("Enter b"))
c = a+b
print("value a is: ",a)
print("value b is: ",b)
print("Sum a is: ",c)
'''

'''
#using try-except block
try:
    a = int(input("Enter a: "))
    print(10/a)
except ZeroDivisionError:
    print("Can not divide by zero")
except ValueError:
    print("Invalid input.")        
'''


'''
 #using pdb module
 pdb-->python debugger
 Purpose:
 1)
 2)
 3)

 pdb commandes:
 1) n--> to get output in the next line
 2) p <variable_name> --> to print the value of variable
 3)l--> list nearby code
 4) c--> continue execution until next breakpoint
 5)s--> starts the function call
 6)r--> to return from the function
 7)h--> help command
 8) q--> quit the execution
'''   
import pdb
def add(a,b):
    pdb.set_trace()
    return a+b
a = int(input("Enter a"))
b = int(input("Enter b"))
print(add(a,b))