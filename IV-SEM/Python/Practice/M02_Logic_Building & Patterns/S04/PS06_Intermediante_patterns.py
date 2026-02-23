'''li=[1,2,3,4,5]
output: [2,4,6,8,10]'''


#using list comprehension
'''
li=[1,2,3,4,5]
li2=[i*2 for i in li]
print(li2)
'''

#using for loop
'''
li=[1,2,3,4,5]
res = []
for i in li:
    res.append(i*2)
print(res)
'''
#to filter even numbers from the list

#using for loop
'''
li = [1,2,3,4,5]
#output: [2,4]
res = []
for i in li:
    if i%2==0:
        res.append(i)
print(res)

#using list comprehension

print([i for i in li if i%2==0])
'''
#['a', 'b', 'c'] ==> "abc"

#using for loop
'''
li = ['a', 'b', 'c']
res = ""
for i in li:
    res += i
print(res)
'''
#using join method
'''
li = ['a', 'b', 'c']
print("".join(li))
'''
#Intermediante patterns

# 1. PYRAMID
'''
1.Pyramid
n = 4
output:
   *
  * *
 * * *
* * * *
'''
#CODE

#using for loops
'''
n = int(input())
for i in range(1,n+1):
    for j in range(1,n-i):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")  
    print()      
'''
#using list comprehension
'''    
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i) 
'''

# 2. INVERTED PYRAMID
'''
2. Inverted Pyramid
n=4
output:
* * * *
 * * *
  * *
   *
   '''
#CODE

'''
n = int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)
'''

#3.DIAMOND

'''
3. Diamond
n = 4
output:
    *
   * *
  * * *
 * * * *
  * * *
   * *
    *  
    '''
# CODE
  
'''
n = int(input())
for i in range(1,n+1):  
    print(" "*(n-i)+"* "*i)  
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)    
'''
# 4. NUMBER DIAMOND

'''
4. Number Diamond
n = 4
output:
   1
  1 2
 1 2 3
 1 2 3 4'''

#CODE
'''
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+" ".join([ str(j) for j in range(1,i+1)]))
'''
# 5. SINGLE NUMBER DIAMOND

'''
5. single number diamond
input : 4
output:
   1
  2 2
 3 3 3
4 4 4 4     
'''
#CODE
'''
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+" ".join([ str(i) for j in range(1,i+1)]))
'''

# 6. RIGHT ANGLED ALPHABETS
'''
6.right angled alphabets
input : 4
output:
A
B C
D E F
G H I J'''
# CODE
'''
n = int(input())
count = 1   
for i in range(1,n+1):
    print(" ".join([ chr(64+count+j) for j in range(i)]))
    count += i
'''
n = int(input())
val = 65
for i in range(n):
    for j in range(i+1):
        print(chr(val),end = " ")
        val += 1
    print()    