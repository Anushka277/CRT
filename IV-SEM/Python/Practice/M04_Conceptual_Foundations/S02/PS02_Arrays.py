#Reverse the array element
'''
input:[12,45,36,78]
output:[78,36,45,12]
'''

#sol 2
res1 = [li[i] for i in range(-1,stop,-1)]
print(res1)


#sol 3
li = [12,45,36,78]
res2 = []
for ele in li:
    res2 = [ele] +res2
print(res2)


#check if the given array is sorted or not 
'''
nums = [12,45,78,96,100]
True

nums = [121,36,78,200]
False
'''


