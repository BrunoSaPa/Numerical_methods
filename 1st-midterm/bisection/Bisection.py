#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 19:33:01 2026

@author: brunosanchezpadilla
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parameters

a0 = 23
b0 = 28
tol = 1e-6

f = lambda x: x*np.sin(x) - 1

max_iter = 30

xmin = -30
xmax = 30

#bisection
#get_ck = lambda ak,bk: 0.5*(ak+bk)
#posicion falsa
get_ck = lambda ak,bk: bk - f(bk)*((bk-ak)/(f(bk)-f(ak)))

Data = np.empty((0,6))

ak = a0
bk = b0

for k in range(max_iter):
    ck = get_ck(ak,bk)
    fak = f(ak)
    fbk =f(bk)
    fck = f(ck)
    
    data = np.array([[ak,bk,ck,fak,fbk,fck]])
    Data = np.concatenate(([Data,data]),axis=0)
    
    if abs(fak) <= tol:
        print(" a0 es una solucion")
        break
    elif abs(fbk) <= tol:
        print ("b0 es una solución")
        break
    elif abs(fck) <=tol:
        print("Solucion en " + str(k+1)+" iteraciones")
        break
    elif fak*fck < 0:
        bk = ck
    elif fbk*fck < 0:
        ak =ck
    elif fak*fbk > 0:
        print("Rango de inicio invalido")
        break
    
Data_df = pd.DataFrame(data = Data, columns=["a","b","c","fa","fb","fc"])

# graficación

fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(1,1,1)

x = np.linspace(xmin,xmax,500)
ax.plot(x,f(x), label="ecuacion")
ax.plot([xmin,xmax],[0,0],"k", label = "_nolegend_")
ax.plot(Data[-1,2],Data[-1,5], marker='o',mec='r', mfc='r', label='sol = ' + str(Data[-1,2]))

ax.legend()
ax.set_xlim([xmin,xmax])
ax.set_xlabel('x')
ax.set_ylabel('y')




