import numpy as np 
import matplotlib.pyplot as plt 

input = np.arange(1,12)
output = numpy.empty(11, dtype=object)

def mm_fib(n):
    return (numpy.matrix([[2,1],[1,1]])**(n//2))[0,(n+1)%2]

for i in range(11):
    output[i]= mm_fib(i)

print(output)

plt.plot(input, output, 
		color = 'red', marker = "o") 
		
plt.title("Fibonacci numbers") 
plt.xlabel("Input") 
plt.ylabel("Output") 
plt.show() 
