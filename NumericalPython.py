import numpy as np

arr = np.array([
    [20, 32, 65, 89, 41],
    [12, 34, 76, 89, 44],
    [23, 43, 45, 66, 12],
    [30, 35, 45, 50, 40],
    [80, 75, 70, 60, 85]
])
data = np.array([1,5,4,7,5,2,6,99,52,12])
print(data)
print(np.min(data)) 
print(np.max(data))
print(np.sum(data)) #Math operations
print(np.mean(data))
print(np.std(data))
print(data[:3])
print(data[-3:]) # seiling
print(data[2:7])
print(np.sort(data))

# Filtering 
print(data[data>10])
print(data[data%2==0])
print(arr[arr>70])
arr[arr<40]= 0
uptarr = arr
print(uptarr)
print(np.sum(uptarr,axis = 1)) #when axis = 1 //row sum
print(np.sum( uptarr,axis = 0)) #when axis = 0 //col sum
print(np.mean( uptarr,axis=1)) #for row
print(np.mean( uptarr,axis=0)) #for col
print(np.max( uptarr,axis=1)) #for row maximn
print(np.max( uptarr,axis=0)) #for col maximun

# Re-shaping 
from numpy import *
newArr =arange(1,17)
print(newArr) #array created
reshape = reshape(newArr,(2,8))
print(reshape)

#Generate random matrix
import numpy as mp
matrix = mp.random.randint(1,101, size = (5,5))
print(matrix)





print(arr.shape) # Will return (size of (row,col))