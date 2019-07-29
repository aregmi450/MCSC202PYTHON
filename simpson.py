#Implement Simpson’s 1/3-rule to approximate the definite integral 𝐼 = root(1/2𝜋)*(e^x^2/2) [4,−4] by taking 50-equal divisions of the interval [−4, 4]. 
import numpy as np
import math as m
print ( "x"+ "\t\t" +"y")
def f(x):
    return (m.sqrt(1/(2*180)))*(m.exp(x*x/2))
lower = -4
upper = 4
sim = 0
n = 50
h = (upper-lower)/n
x = np.arange (lower, upper, h)
y = []
for i in range (len(x)):
    y.append(f(x[i]))
    print(round (x[i],4), "\t\t", round (y[i],4))
    
    sim =y[0] + y[-1]
    sim = sim + 4* sum (y[1:-1:2]) + 2* sum (y[2:len(y)-1:2])
    sim = (h/3)*sim

    