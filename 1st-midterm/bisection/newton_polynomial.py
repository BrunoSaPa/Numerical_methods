import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


#points
x0 = -2; f0 = -5
x1 = 0; f1 = 3
x2 = 2; f2 = 1
x3 = 4; f3 = 5

# divided differences

fx0x1 = (f1-f0)/(x1-x0)
fx1x2 = (f2-f1)/(x2-x1)
fx2x3 = (f3-f2)/(x3-x2)

print('f[x0, x1]= ',fx0x1)
print('f[x1, x2]= ',fx1x2)
print('f[x2, x3]= ',fx2x3)

fx0x1x2 = (fx1x2 - fx0x1)/(x2-x0)
fx1x2x3 = (fx2x3 - fx1x2)/(x3-x1)

print('f[x0, x1, x2]= ',fx0x1x2)
print('f[x1, x2, x3]= ',fx1x2x3)



fx0x1x2x3 = (fx1x2x3-fx0x1x2)/(x3-x0)

print('f[x0, x1, x2, x3]= ',fx0x1x2x3)


#newton coeficients

a0 = f0
a1 = 4
a2 = -5/sp.S(4)
a3 = 1/sp.S(3)


x = sp.symbols('x')
P1 = a0 + a1*(x-x0)
P2 = P1 + a2*(x-x0)*(x-x1)
P3 = P2 + a3*(x-x0)*(x-x1)*(x-x2)

P1 = P1.expand()
P2 = P2.expand()
P3 = P3.expand()

sp.pprint(P1)
sp.pprint(P2)
sp.pprint(P3)

