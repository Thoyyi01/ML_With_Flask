import numpy as np 
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)
print("5th element on 2nd row",arr[1,4])
print("4th element on 1nd row",arr[0,2])
print("_______________________________________")
array = np.arange(50).reshape(5,10)
print(array)
print("_______________________________________")
a = np.array([[1,2,3],[5,6,7]])
print(a)
print("_______________________________________")
m = np.array([[1,2,3],[5,6,7],[2,4,6],[3,5,7]])
print(m)
n = np.array([[2,4,6],[8,10,12],[1,3,5],[7,9,11]])
print(n)
print("_______________________________________")
print(m*n)
print("_______________________________________")
import numpy as np
ar = np.array([1,2,3,4,5,6,7,8,9,10])
#print(ar[2]+ar[3])
print(ar[0]+ar[1])
#print(ar[5]+ar[7])
print("_______________________________________")
b=np.array([1,2,3,4,5,6])
print(b[1:6:2])
print("_______________________________________")
import pandas as pd

data = {
    "Brand": ["Toyota", "Honda", "Ford", "Chevrolet", "BMW"],
    "Model": ["Camry", "Civic", "F-150", "Malibu", "X5"],
    "Year": [2020, 2019, 2021, 2018, 2022],
    "Price ($)": [24000, 22000, 29000, 21000, 60000]
}

cars_df = pd.DataFrame(data)
print(cars_df)
