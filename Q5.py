# Plot the function y = 3x 2 for −3 ≤ x ≤ 3. Include enough points (say 100 points) so
# that the curve you plot appears smooth. Label the axes x and y.

import numpy as np
import matplotlib.pyplot as plt

def plot():
   arr=np.linspace(-3,3,100)
   y=[3*x*x for x in arr]
   plt.plot(arr,y)
   plt.xlabel('x-axis')
   plt.ylabel('y-axis')
   plt.show()

plot()
