import numpy
from numpy import random

#Permutation and shuffle
arr = numpy.array([1, 2, 3, 4, 5])
myshuffle = random.shuffle(arr)
print('myshuffle:',arr)
print('Permutation:',random.permutation(arr))

#Normal Gaussian Distribution
print('myrandom:',random.normal(size=(2,3)))

#Bionomial Distribution 
x = random.binomial(n=10, p=0.5, size=10)
print('binomial:',x)

#Data Distribution
#x1 = random.choice([3, 5, 7, 9], p=0.3, size=100)

#Poission Distributation
x3= random.poisson(lam=2, size=10)
print('poisson:',x3)

#Uniform Distribution
x4 = random.uniform(size=(2,3))
print('uniform:',x4)

#Logistic Distribution
x5 = random.logistic(loc=1, scale=2, size=(2,3))
print('logistic:',x5)

#MultiDiamentional Array Distribution
x6 = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print('multinomial:',x6)

#chi-squre Distribution 
x7= random.chisquare(df=2, size=(2,1))
print('chisquare:',x7)

#rayleigh distribution
x8 = random.rayleigh(scale=2, size=(2,3))
print('rayleigh:',x8)

#exponential distribution
x9= random.exponential(scale=2, size=(2,3))
print('random:',x9)

#Pareto Distribution
x10 = random.pareto(a=2,size=(2,3))
print('pareto:',x10)

#zipf 
x11= random.zipf(a=2, size=(2,3))
print('zipf:',x11)