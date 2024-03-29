import numpy as np 
import matplotlib.pyplot as plt 

input_len=50

input = np.arange(0,input_len)
output = np.empty(input_len, dtype=object)

def mm_fib(n):
    return (np.matrix([[2,1],[1,1]])**(n//2))[0,(n+1)%2]

for i in range(input_len):
    output[i]= mm_fib(i)

print(output)

plt.plot(input, output, 
		color = 'red', marker = "o") 
		
plt.title("Fibonacci numbers") 
plt.xlabel("Input") 
plt.ylabel("Output") 
plt.show() 
