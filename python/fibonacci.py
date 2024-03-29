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


```
# Why does the series show a negative number when the input length is 50 
[0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269
 2178309 3524578 5702887 9227465 14930352 24157817 39088169 63245986
 102334155 165580141 267914296 433494437 701408733 1134903170 1836311903
 -1323752223 512559680 -811192543]

check the experiment in version 2
```
