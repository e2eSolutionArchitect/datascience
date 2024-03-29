import numpy as np 
import matplotlib.pyplot as plt 

# We are creating an array containing n = 10 elements 
# for getting the first 10 Fibonacci numbers 
a = np.arange(1, 200) 
lengthA = len(a) 

# splitting of terms for easiness 
sqrtFive = np.sqrt(5) 
alpha = (1 + sqrtFive) / 2
beta = (1 - sqrtFive) / 2

# Implementation of formula 
# np.rint is used for rounding off to an integer 
Fn = np.rint(((alpha ** a) - (beta ** a)) / (sqrtFive)) 
print("The first {} numbers of Fibonacci series are {} . ".format(lengthA, Fn)) 

# red for numpy.log() 
plt.plot(a, Fn, 
		color = 'red', marker = "o") 
		
plt.title("Fibonacci") 
plt.xlabel("Input") 
plt.ylabel("Putput") 
plt.show() 


```
- Find the pattern of change in slope

```
