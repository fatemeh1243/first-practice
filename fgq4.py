def f_to_c(f):
   c = ( f * 9 / 5) + 32
   return c
def c_to_f(c):
   f = ( c - 32 ) * 9/5
   return f
f = float(input("pls enter farenheit:"))
c = float(input("pls enter celsious:"))
x = int(input("enter '1' u will see  to convert from f to c or '2' u will see  to convert from c to f: "))
if x == 1 :
   c = f_to_c(f)
   print("result you want is c ", c )
elif x == 2 :
   f = f_to_c(c)
   print("result you want is f ", f )
else:
   print("wrong choice")
