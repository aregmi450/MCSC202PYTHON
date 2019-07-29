# The position of a ball at time t dropped with zero initial velocity from a height h 0 is
# given by
# y = h 0 − 0.5gt 2
# 2
# where g = 9.8 m/s . Suppose h 0 = 10 m. Find the sequence of times when the ball
# passes each half meter assuming the ball is dropped at t = 0. Hint: Create a NumPy
# array for y that goes from 10 to 0 in increments of -0.5 using the arrange function.
# Solving the above equation for t, show that
#
# t = sqrt(2*(ho-y)) / g
#
# Using this equation and the array you created, find the sequence of times when the
# ball passes each half meter. Save your code as a Python script.
# Δy
# Recalling that the average velocity over an interval Δt is defined as v = Δt , find the
# average velocity for each time interval in the problem using NumPy arrays.
import numpy as np

g=9.8
ho=10
def calcTime(y):
   t=(np.sqrt(2*(ho-y)) / g)
   return t

arr=np.arange(10,0,-1)-0.5
y=np.array([round(float(calcTime(x)),3) for x in arr])
av=np.around(arr/y,3)

print('Each Half Meter : ', arr)
print('Sequence of time : ', y)
print('Average velocity : ', av)
