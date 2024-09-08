r"""
# OGRePy: An Object-Oriented General Relativity Package for Python
v1.1.0 (2024-09-08)

By **Barak Shoshany**\
Email: <baraksh@gmail.com>\
Website: <https://baraksh.com/>\
GitHub: <https://github.com/bshoshany>

GitHub repository: <https://github.com/bshoshany/OGRePy>\
PyPi project: <https://pypi.org/project/OGRePy/>

Based on the Mathematica package [OGRe](https://github.com/bshoshany/OGRe) by Barak Shoshany.

Copyright (c) 2024 [Barak Shoshany](https://baraksh.com/). Licensed under the [MIT license](https://github.com/bshoshany/OGRePy/blob/master/LICENSE.txt).

If you use this package in published software or research, please provide a link to [the GitHub repository](https://github.com/bshoshany/OGRePy) in the source code and documentation.
"""

from sympy import Symbol

from ._core import sym

# SymPy symbols for all English and Greek letters, both lowercase and uppercase. Note that lambda is replaced with "lamda" since lambda is a reserved keyword in Python. The OGRePy definitions, based on OGRePy's `sym()` function, differ from `sympy.abc` in several ways:
# 1. All symbols are explicitly assumed to be real.
# 2. Uppercase Greek letters are also included (for some reason they are missing from `sympy.abc`).
# 3. The symbols also include type annotations.

a: Symbol = sym("a")
b: Symbol = sym("b")
c: Symbol = sym("c")
d: Symbol = sym("d")
e: Symbol = sym("e")
f: Symbol = sym("f")
g: Symbol = sym("g")
h: Symbol = sym("h")
i: Symbol = sym("i")
j: Symbol = sym("j")
k: Symbol = sym("k")
l: Symbol = sym("l")
m: Symbol = sym("m")
n: Symbol = sym("n")
o: Symbol = sym("o")
p: Symbol = sym("p")
q: Symbol = sym("q")
r: Symbol = sym("r")
s: Symbol = sym("s")
t: Symbol = sym("t")
u: Symbol = sym("u")
v: Symbol = sym("v")
w: Symbol = sym("w")
x: Symbol = sym("x")
y: Symbol = sym("y")
z: Symbol = sym("z")

A: Symbol = sym("A")
B: Symbol = sym("B")
C: Symbol = sym("C")
D: Symbol = sym("D")
E: Symbol = sym("E")
F: Symbol = sym("F")
G: Symbol = sym("G")
H: Symbol = sym("H")
I: Symbol = sym("I")
J: Symbol = sym("J")
K: Symbol = sym("K")
L: Symbol = sym("L")
M: Symbol = sym("M")
N: Symbol = sym("N")
O: Symbol = sym("O")
P: Symbol = sym("P")
Q: Symbol = sym("Q")
R: Symbol = sym("R")
S: Symbol = sym("S")
T: Symbol = sym("T")
U: Symbol = sym("U")
V: Symbol = sym("V")
W: Symbol = sym("W")
X: Symbol = sym("X")
Y: Symbol = sym("Y")
Z: Symbol = sym("Z")

alpha: Symbol = sym("alpha")
beta: Symbol = sym("beta")
gamma: Symbol = sym("gamma")
delta: Symbol = sym("delta")
epsilon: Symbol = sym("epsilon")
zeta: Symbol = sym("zeta")
eta: Symbol = sym("eta")
theta: Symbol = sym("theta")
iota: Symbol = sym("iota")
kappa: Symbol = sym("kappa")
lamda: Symbol = sym("lamda")
mu: Symbol = sym("mu")
nu: Symbol = sym("nu")
xi: Symbol = sym("xi")
omicron: Symbol = sym("omicron")
pi: Symbol = sym("pi")
rho: Symbol = sym("rho")
sigma: Symbol = sym("sigma")
tau: Symbol = sym("tau")
upsilon: Symbol = sym("upsilon")
phi: Symbol = sym("phi")
chi: Symbol = sym("chi")
psi: Symbol = sym("psi")
omega: Symbol = sym("omega")

Alpha: Symbol = sym("Alpha")
Beta: Symbol = sym("Beta")
Gamma: Symbol = sym("Gamma")
Delta: Symbol = sym("Delta")
Epsilon: Symbol = sym("Epsilon")
Zeta: Symbol = sym("Zeta")
Eta: Symbol = sym("Eta")
Theta: Symbol = sym("Theta")
Iota: Symbol = sym("Iota")
Kappa: Symbol = sym("Kappa")
Lamda: Symbol = sym("Lamda")
Mu: Symbol = sym("Mu")
Nu: Symbol = sym("Nu")
Xi: Symbol = sym("Xi")
Omicron: Symbol = sym("Omicron")
Pi: Symbol = sym("Pi")
Rho: Symbol = sym("Rho")
Sigma: Symbol = sym("Sigma")
Tau: Symbol = sym("Tau")
Upsilon: Symbol = sym("Upsilon")
Phi: Symbol = sym("Phi")
Chi: Symbol = sym("Chi")
Psi: Symbol = sym("Psi")
Omega: Symbol = sym("Omega")
