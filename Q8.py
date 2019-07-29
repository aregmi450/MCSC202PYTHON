# Write a program to calculate the factorial of a positive integer input by the user.
# (a) Write the factorial function using a Python while loop.
# (b) Write the factorial function using a Python for loop.
# Check your programs to make sure they work for 0,1, 2, 3, 4,5

def factWithWhile(n):
   fact=1
   while(n):
      fact*=n
      n=n-1
   return fact

def factWithFor(n):
   fact=1
   for i in range(1,n+1):
      fact*=i
   return fact

print('Enter number for factorial :')
n = int(input())
print('Factorial with while :', factWithWhile(n))
print('Factorial with for :', factWithFor(n))
