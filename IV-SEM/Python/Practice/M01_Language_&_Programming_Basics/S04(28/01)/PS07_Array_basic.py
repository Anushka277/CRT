'''
# mutable and immutable types in Python
Mutable types: list, set, dictionary, array
Immutable types: int, float, string, tuple
#homogeneouse and heterogeneous types
Homogeneous types: array(means same type)
Heterogeneous types: list, tuple, set, dictionary(means different types)
'''

'''
import array
arr = array.array('i',[12,45,78])
print(arr,type(arr))
arr.append(10)
arr.append(20)
print(arr)
arr.append(12.50)
'''

'''
list:
1.use[] to declare/create a list
2.list is mutable
3.list allows duplicate elements
4.list is heterogeneous
5.list allows indexing and slicing
'''

li = [12,25.4,6.5j,"hello",True,12,25.4]
print(li,type(li))
print(li[3])      #indexing
print(li[3:7:1])    #slicing
print(li[::-1])
print(len(li))
li.append(100)
print(li)   #add element at the end
li.insert(2,"world")
print(li)   #add element at specific index
li.remove(25.4)
print(li)   #removes first occurrence of element
li.insert(12,"python")
print(li)
li.insert(-6,"java")
print(li)