import numpy as np
import pandas as pd

mat = np.arange(0,15).reshape(5,3)
# df = pd.DataFrame(data = mat, index = ['1st', '2nd', '3rd', '4th', '5th'], columns=['A', 'B', 'C'])
df = pd.DataFrame(data = mat, index = ['1st 2nd 3rd 4th 5th'.split()], columns=['A B C'.split()])

df1 = pd.read_csv('G:\Workspace\workspace\Python\salaries.csv')

print(mat)
print(df)
print(df1)  

np.random.seed(10)
print(np.random.randint(1,100,(100,5)))