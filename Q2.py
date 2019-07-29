import math

def Q2():
   i = (2.0+math.exp(2.8))/(math.sqrt(13)-2.0)
   ii = (1-math.pow(1 + math.log(2),-3.5)) / (1+math.sqrt(5))
   iii = math.sin( (2-math.sqrt(2)) / (2+math.sqrt(2)) )
   return {
      "i": i,
      "ii": ii,
      "iii": iii
   }

print('Answer For Question i : ', Q2()['i'])
print('Answer For Question ii : ', Q2()['ii'])
print('Answer For Question iii : ', Q2()['iii'])