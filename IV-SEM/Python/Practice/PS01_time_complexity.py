'''
time complexity is a measure of the amount of time an algorithm takes to complete as a function of the size of the input. It is often expressed using Big O notation, which describes the upper bound of the growth rate of an algorithm.
Common time complexities include:
- O(1): Constant time complexity - the algorithm takes the same amount of time regardless of the size of the input.
- O(n): Linear time complexity - the algorithm's time grows linearly with the size of
-O(n log n) , O(n^2) , O(2^n) , O(n!) etc are other common time complexities that describe different growth rates of algorithms.'''
#O(1) => constant time complexity
'''
li = [10, 20, 30, 40, 50]
print(li[2]) #O(1)
li.append(60) #O(1)
'''
#O(n) => linear time complexity
'''
li.insert(0,100) #O(n)
'''
#O(n log n) => logarithmic time complexity
'''
empty_list = []
for i in range(10):
    empty_list.append(i)
empty_list.sort() #O(n log n)
'''
#O(n^2) => quadratic time complexity
'''

'''
def Linear_search(li,target):
    for i in range(len(li)):
        if li[i]==target:
            return i
    return -1

Linear_search([12,45,78,69,32,49],12) #1=>best case=>O(1)
Linear_search([12,45,78,69,32,49],49) #6=>worst case=>O(n)
Linear_search([12,45,78,69,32,49],100) #6     