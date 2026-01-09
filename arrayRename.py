# from array import array
# # arr = [10,20,0]
# # print(type(arr)) # This is List not Array


# # I learned how to declare empty array in python , adding values to it , searching through loops
# arr = array('i',[])#Empty array

# size = int(input("Enter the size of the array"))
# for i in range(0,size):
#     value = int(input("Enter the element"))
#     arr.append(value)

# print(arr)

# search = int(input("Enter the element to search"))
# index=0
# for s in arr:
#     if(s == search):
#       print(index)
#       break
     
#     index+=1

# #Next about numpy

from numpy import array, linspace
arr = linspace(1,3,5)
print(arr)

# 2-d array 

import numpy as mp
arr = mp.array([
    [1,51,2],
    [8,7,5]
])
print(arr.flatten()) 