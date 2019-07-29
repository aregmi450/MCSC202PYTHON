# A ball is thrown vertically up in the air from a height h 0 above the ground at an initial
# velocity v 0 . Its subsequent height h and velocity v are given by the equations
# h = ho + vo t− gt^2
# v = vo − gt
# where g = 9.8 is the acceleration due to gravity in m/s 2 . Write a script that finds the
# height h and velocity v at a time t after the ball is thrown. Start the script by setting h 0 =
# 1.2 (meters) and v 0 = 5.4 (m/s) and have your script print out the values of height and
# velocity.
# Then use the script to find the height and velocity after 0.5 seconds.
# Then modify your script to find them after 2.0 seconds.

def getHeightAndVelocity(timePeriod):
   g=9.8
   ho=1.2
   vo=5.4
   h=ho+(vo*timePeriod)-(0.5*g*timePeriod*timePeriod)
   v=vo-(g*timePeriod)
   return {
      "height":h,
      "velocity":v
   }

print('Height at t=0.5   =>', getHeightAndVelocity(0.5)['height'])
print('Velocity at t=0.5 =>', getHeightAndVelocity(0.5)['velocity'])
print('Height at t=2.0   =>', getHeightAndVelocity(2.0)['height'])
print('Velocity at t=2.o =>', getHeightAndVelocity(2.0)['velocity'])

