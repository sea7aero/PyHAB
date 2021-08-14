"""
This python module is a quick proof of concept of an idea I have - demonstrated in this library -
for creating writing documentation first and generating code from it.  It extends the sympy library
to create a simple DSL for manipulating equations in code, and generate code from the result.

Examples
--------

term_vel = align(
    Equation(F_g, F_d).comment("Terminal velocity is acheived when the force of gravity equals the drag force.")
    .replace(F_g, m * g)
    .replace(F_d, Rational(1/2) * rho * C_d * A * v**2)
    .solve(v)
)
"""
from .equation import *
from .symbol_table import *

# Monkey patch PyLatex so LatexObjects get displayed in Jupyter as latex.
from pylatex.base_classes import LatexObject
LatexObject._repr_latex_ = lambda self: self.dumps()