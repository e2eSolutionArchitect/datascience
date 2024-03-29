import numpy as np 
import matplotlib.pyplot as plt 
import math 

# We are creating an array containing n = 10 elements 
# for getting the first 10 Fibonacci numbers 

input_number=100
a = np.arange(1, input_number) 
output_log10 = np.arange(1, input_number) 
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

#print(output_log10)

print("The first {} numbers of Fibonacci series are {} . ".format(lengthA, Fn)) 

# plt.plot(a, Fn,color = 'red', marker = "o") 

plt.plot(a, output_log10,color = 'red', marker = "o") 
		
plt.title("Fibonacci") 
plt.xlabel("Input") 
plt.ylabel("Output") 
plt.show() 
