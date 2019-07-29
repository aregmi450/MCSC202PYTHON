# Plot the functions y = sin x and y = cos x for −2π ≤ x ≤ 2π on the same plot. Plot
# y = sin x in the color red and y = cos x in the color blue and include a legend to label
# the two curves. Place the legend within the plot, but such that it does not cover either of
# the sine or cosine traces.

import numpy as np
import matplotlib.pyplot as plt

def plot2():
   x = np.linspace(-2*np.pi, 2*np.pi, 100)
   plt.plot(x, np.sin(x), label='sinx', color='red')
   plt.plot(x, np.cos(x), label='cosx', color='blue')
   plt.xlabel('x axis')
   plt.ylabel('y axis')
   plt.legend()
   plt.show()

plot2()