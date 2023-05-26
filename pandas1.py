#1D Array
from dis import dis
import pandas as pd 
x = [3, 4, 5, 6, 7, 8]
var = pd.Series(x)
print(type(var))
print(var)

#data frames
var1 = pd.DataFrame({'a':[1, 2, 3, 4, 5], 's':[1, 2, 3, 4, 5]})
print(type(var1))
print(var1)

var1['b'] = var1['a'] + var1['s']
print('result on addition ,substraction and multi')
print(var1['b'])

var1['c'] = var1['a'] - var1['s']
print(var1['c'])

#Insert data
var1.insert(1, "python", var1['a'])
#print(var1)

var1['ani'] = var1["a"][:3]
#print(var1)

#delete or pop
var1.pop('c')
del var1['python']
print(var1)

#CSV File
dis ={'pri':[1, 2, 3, 4, 5], 'aniket':[1, 2, 3, 4, 5]}
d= pd.DataFrame(dis)
d.to_csv("mycsvfile")
#d.to_csv("test", index=False,header=[1, 2, 3])

#read csv_file
csv_1 = pd.read_csv("C:\Users\ANIRUDDHA\Desktop\New folder\mycsvfile.csv")
print(csv_1)