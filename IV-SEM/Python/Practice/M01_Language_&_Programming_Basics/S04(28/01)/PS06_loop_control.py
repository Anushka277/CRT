'''break and continue statements in loops
break statement: used to exit a loop prematurely when a certain condition is met.
continue statement: used to skip the current iteration of a loop and move to the next iteration.
'''
'''#Example of break statement
for i in range(1,11):
    if i == 5:
        break
    print(i,end=" ")
'''
'''
for i in range(1,11):
    print(i,end=" ") 
    if i == 5:
        break   
        
 #example of continue statement
 for i in range(1,11):
    if i%2 == 0:
        continue
    print(i,end=" ")   

  '''
'''
  Password retry system(max 3 attempts)
  if password is correct show login successful
  else ask for password 3 times.
  once attempts are exhausted show account locked 
  '''
#using while loop 
print("\nUsing while loop:")
correct_password = "secure123"
max_attempts = 3
attempts = 0
while attempts < max_attempts:
    entered_password = input("Enter your password: ")
    if entered_password == correct_password:
        print("Login successful")
        break
    else:
        attempts += 1
        print("Incorrect password. Try again.")

if attempts == max_attempts:
    print("Account locked due to too many failed attempts.")

#using for loop
print("\nUsing for loop:")
p1  = "abcd@123"
for i in range(3):
    p2 = input("Enter your password: ")
    if p1 == p2:
        print("Login Successful")
        break
else:
    print("Account locked due to too many failed attempts.")