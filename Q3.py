# Create an array of 9 evenly spaced numbers going from 0 to 29 (inclusive) and give it the
# variable name r. Find the square of each element of the array (as simply as possible).
# Find twice the value of each element of the array in two different ways:
# (i)
# using addition and
# (ii) using multiplication.

import numpy as np

def Q3():
   arr = np.linspace(0,29,9)
   sqArr = [x**2 for x in arr]
   doubleArr = [2*x for x in arr]
   doubleArrAdd = [x+x for x in arr]

   return {
      "Array": arr,
      "SquaredArray": sqArr,
      "DoubledArray": doubleArr,
      "DoubleByAddition": doubleArrAdd
   }

print('Linearly spaced array : ', Q3()['Array'] )
print('Squared array : ', Q3()['SquaredArray'] )
print('Doubled Array : ', Q3()['DoubledArray'] )
print('Double By Addition : ', Q3()['DoubleByAddition'] )




