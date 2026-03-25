'''
Optimization Basics:
Optimization is the process of finding the best solution to a problem, often by minimizing or maximizing a function. In machine learning, optimization is used to find the best parameters for a model that minimizes the loss function.
it is the process of modifying the code to get more efficient.
efficient:
--> to reduce time complexity
--> to reduce space complexity
-->to reduce memory usage
--> to avoidunnessary operations
Real world examples of optimization:
1) Finding the shortest path in a navigation system.
2) Scheduling tasks in a way that minimizes total time.

Brute force --> step by step execution,easy to implement for less input.
optimal solution --> reduced time and space complexity.
   '''
a = [10, 20, 30, 40, 50]
target = 30 
for i in range(len(a)):
    if a[i] == target:
        print("Element found" )
        break

a = [10, 20, 30, 40, 50]
if 30 in a:
    print("Element found")

#write a python code to print the sum of elements in list
a = [1, 2, 3, 4, 5]
total = 0   
for num in a:
    total += num
print("Sum of elements:", total)

#two sum
a = [2, 7, 11, 15]
target = 9
d={}
for i in range(len(a)):
    res = target - a[i]
    if res in d:
       print([d[res],i])
    d[a[i]]=i

'''
Common ways to get Optimization:
1)reducing the time complexity optimization(ex:O(n^2) to O(n))
2) hashing(use set/dict)
3) using built in functions
4)avoiding unnecessary operations
5)list comprehension optimization'''

a=[]
for i in range(10):
    a.append(i*i)
print(a)

a=[i*i for i in range(10)]
print(a)

#write the code to print the max element using for loop?
n = [3, 5, 2, 8, 1]
max_num = n[0]
for num in n:
    if num > max_num:
        max_num = num
print("Maximum element:", max_num)
