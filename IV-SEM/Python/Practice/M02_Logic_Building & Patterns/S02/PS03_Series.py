#fibonacci series:

n=int(input())
f1,f2 = 0,1
for i in range(n):
    print(f1,end=" ")
    f1,f2 = f2,f1+f2


#using lists
n = int(input())
fib = [0,1] 
for i in range(2,n):
    fib.append(fib[i-1]+fib[i-2])
print(fib[:n])

'''Power of number series
2      
=> 2 4 8 .....'''
