#Implement Euler’s method to approximate the solution 𝑦(𝑥) of the differential equation 𝑑𝑦/𝑑𝑥 = 𝑥^2 + 𝑥, 𝑦 (0) = 1 on the interval [0, 2] by diving it into 20- equal sub-intervals. 
import numpy as np
def f(x,y):
 return x** 2 + x
print("x", "\t\t", "y")
lower = 0
upper = 2
n = 20
h = (upper-lower)/n
x = np.arange(lower,upper,h)
y = np.zeros(len(x))
for i in range (0,len(x)):
    y[i] = y[i-1]+h * f(x[i-1],y[i-1])
print (round(x[i],5), "\t\t", round (y[i],5))
print ("\nEuler Method:" + str(y))


