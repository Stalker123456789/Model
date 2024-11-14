import numpy as np
def multiply_array_elements(arr):
    result = np.prod(arr)
    return result
arr = np.array([5, 7, 3, 6, 9])
result = multiply_array_elements(arr)
print(result) 
