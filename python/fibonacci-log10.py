import numpy as np 
import matplotlib.pyplot as plt 
import math 

# We are creating an array containing n = 10 elements 
# for getting the first 10 Fibonacci numbers 
a = np.arange(1, 10) 
output_log10 = np.arange(1, 10) 
lengthA = len(a) 

# splitting of terms for easiness 
sqrtFive = np.sqrt(5) 
alpha = (1 + sqrtFive) / 2
beta = (1 - sqrtFive) / 2

# Implementation of formula 
# np.rint is used for rounding off to an integer 
Fn = np.rint(((alpha ** a) - (beta ** a)) / (sqrtFive)) 
print('Fn values',Fn)

m=0

for k in Fn:
    output_log10[m]=math.log10(k)
    print('Log base 10 of {} is {}'.format(k, math.log10(k)))
    m=m+1

print(output_log10)
#output_log10=math.log10(Fn)

print("The first {} numbers of Fibonacci series are {} . ".format(lengthA, Fn)) 

# red for numpy.log() 
plt.plot(a, Fn, 
		color = 'red', marker = "o") 
		
plt.title("Fibonacci") 
plt.xlabel("Input") 
plt.ylabel("Output") 
plt.show() 
