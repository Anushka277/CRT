'''
Docstring for IV-SEM.Python.Practice.M02_Logic_Building_And_Patterns.S01.PS01_Digits_problems
sample input: 1234
sample output: 4

sample input : 455786
sample output: 6 

sample input: 45
sample output: 2
'''
'''n = int(input())
c = 0
while n>0:
    
    
    n = n//10
    c += 1
print(c)
print(len(str(n)))
'''
'''
n = int(input())
c = 0
while n>0:
    c += (n%10)
    n = n//10 
print(c)
print(sum(map(int, str(n))))
'''

'''
n = int(input())
even = odd = 0 
while n>0:
    if (n % 2) == 0:
        even += 1
    else:
        odd += 1
        n = n//10
print(even,odd)
'''


"digital root sum "
'''n  = int(input())
while n>9:
    s = 0
    while n>0:
        s += (n%10)
        n = n//10 
    n = s                   
print(n)
'''

"reverse of a number"
n = int(input())
rev = 0
while n>0:
    rev = (rev*10) + (n%10)
    n = n//10
print(rev)