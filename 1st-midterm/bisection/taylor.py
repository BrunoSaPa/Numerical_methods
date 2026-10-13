import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from math import factorial

##function to approximate

x = sp.symbols("x")
f = sp.sin(x) + sp.cos(2*x)
x0 = 0
N = 3 
P = 0

xlim = [-2,2] # to graph the approximation

for k in range(N+1):
    Pk = (f.diff(x,k).subs(x,x0)/factorial(k)) * (x-x0)**k
    P = P + Pk
    
sp.pprint(P)

xnum = np.linspace(xlim[0], xlim[1],500)
fnum = sp.lambdify(x,f)
Pnum = sp.lambdify(x, P)


fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(1,1,1)

ax.plot(xnum,fnum(xnum),'b',label='$f(x)$')
ax.plot(xnum,Pnum(xnum),'r',label='$P(x)$')
ax.plot(x0,Pnum(x0),'k.',ms=10,label='_nolegend_')




ax.grid(True)
