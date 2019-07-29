# Implement Runge-Kutta 2nd order method to approximate the solution 𝑦(𝑥) of the differential equation 𝑑𝑦/𝑑𝑥 = 𝑥2 + 𝑥, 𝑦(0) = 1 on the interval [0, 2] by diving it into 10-equal sub-intervals.
import numpy as np
def f(x,y):
    return x**2 + x
print ("x" + "\t\t", "y")
lower = 0
upper = 2
n = 10
h = (upper-lower)/n
x = np.arange(lower,upper,h)
y = np.zeros(len(x))
for i in range (1, len(x)):
    k1 = h*f(x[i-1], y[i-1])
    k2 = h *f(x[i-1], y[i-1] + k1)
    y[i] = y[i-1] + 0.5 * (k1+k2)
    print (round(x[i],5), "\t\t", round(y[i],5))
