'''x,y = list(map(int,input().split()))
print(x,end=" ")
print(y)
print(x,y,sep=" @ ")
'''
'''
read a number of input from the user and display no. of digits in that number
input: 1234
output: 4
'''
num = input()
count = 0
for i in num:
    count += 1
print("Number of digits:", count)
