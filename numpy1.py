import numpy
arr =numpy.array([1, 2, 3, 4, 5])
print(arr)

#1D ARRAY
arr1 =numpy.array(42)
print(arr1)

arr2 = numpy.array([1, 2, 3, 4, 5])
print(arr2)

#2D ARRAY
arr3 = numpy.array([[1, 2, 3],[4, 5, 6]])
print(arr3)
print('arr3 shape:',arr3.shape)
print(arr3[0, 2])

#3D ARRAY
arr4 = numpy.array([[[1, 2, 3],[4, 5, 6]],[[7, 8, 9],[10, 11, 12]]])
print(arr4)
print(arr4[0, 1, 2]) #access [set,row,column]
#Reshape Array
newarr = arr4.reshape(4, 3)
print('newarr',newarr)

#Find Diamension
print(arr4.ndim)

#Higher Diamension Array
arr5 = numpy.array([1, 2, 3, 4, 5])
print(arr5[0]) #access

#Array Slicing
arr6 = numpy.array([1, 2, 3, 4, 5, 6])
print('slice array:',arr6[2:5:2])
print(arr6.dtype)

#split
myarr0 = numpy.array_split(arr6,2)
print('split', myarr0)

#iterarting Array
arr7 = numpy.array([1, 2, 3])
for x in arr:
    print('iterx:',x)

#concatinate
myarr1 = numpy.array([1, 2, 3])
myarr2 = numpy.array([4, 5, 6])
myarr3 = numpy.concatenate((myarr1, myarr2))
print(myarr3)

#Searchig
mysearch = numpy.array([1, 2, 3, 4, 5, 6])
myx = numpy.where(mysearch == 4)
print('my x search:', myx)
myx1 = numpy.where(mysearch % 2 == 0)
print('myx1:', myx1)

#Sorting 
mysort1 = numpy.array([3, 2, 0, 6, 7])
mysort = numpy.sort(mysort1)
print('mysort:',mysort)

#Filter
myfilter1 = numpy.array([11, 12, 13, 14])
myfilter_arr = myfilter1 > 12
print(myfilter_arr)

myfilter = myfilter1[[True, False, False, True]]
print(myfilter)

#Random Function:
from numpy import random
x = random.randint(100)
print(x)

x1 = random.randint(100, size=5)
print(x1)

#choice
x2 = random.choice([3, 5, 7, 9])
print(x2)

#print(type(arr))
#print(numpy.version)