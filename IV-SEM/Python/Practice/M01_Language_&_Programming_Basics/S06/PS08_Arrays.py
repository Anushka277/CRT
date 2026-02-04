'''
Arrays: collection of items stored at contiguous memory locations.
Numpy array: a powerful n-dimensional array object provided by the NumPy library in Python.
'''
import numpy as np
arr = np.array([10,20,30,40,50])
print("Array elements: ",arr)
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.sum(arr))
print(np.zeros(5))
print(np.ones(8))
print("Even numbers are:",np.arange(2,10,2))
print("Odd numbers are:",np.arange(1,10,2))

n = int(input("Enter size of array: "))
ele = list(map(int,input("Enter elements: ").split()))
print("Array elements are:",np.array(ele))