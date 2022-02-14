import sympy as sp

x, y = sp.symbols('x y')

expr = sp.integrate(sp.sin(x)/(x**x))
sp.pprint(sp.simplify(expr))
