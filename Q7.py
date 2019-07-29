# Write a program to tell the nature of the roots and values of the roots of a quadratic
# equation ax 2 + bx + c = 0, a ≠ 0.

print ('Enter value of a : ')
a=float(input())
print ('Enter value of b : ')
b=float(input())
print ('Enter value of c : ')
c=float(input())

det = (b*b) - (4*a*c)
if(det==0):
   print ('Real and equal roots')
elif(det>0):
   print('Real and unequal root')
else:
   print('Imaginary roots')