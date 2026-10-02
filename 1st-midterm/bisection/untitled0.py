import sympy as sp

x,y,z = sp.symbols('x,y,z')

f1 = 3*x**2 + 2*y - 4
f2 = 2*x + 2*y - 3
f3 = 2*x - 4*sp.cos(z)

Xk = sp.Matrix([[-1],[3],[1]])


# jacobian matrix
J = sp.Matrix([
    [f1.diff(x),f1.diff(y),f1.diff(z)],
    [f2.diff(x),f2.diff(y),f2.diff(z)],
    [f3.diff(x),f3.diff(y),f3.diff(z)],
    ])

# equation vectors
F = sp.Matrix([[f1],[f2],[f3]])

Jk = J.subs({x:Xk[0,0], y:Xk[1,0], z:Xk[2,0]}).evalf(6)
Fk = F.subs({x:Xk[0,0], y:Xk[1,0], z:Xk[2,0]}).evalf(6)

Jinv_k = Jk.inv()
Xnext = Xk - Jinv_k*Fk

sp.pprint(Xnext)




