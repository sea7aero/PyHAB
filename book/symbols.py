from sympy import *
from sympy.core import symbol
import sympy.physics.units.systems.si as si

from dataclasses import dataclass

@dataclass(order=True)
class SymbolInfo(object):
    name: str
    symbol: Symbol
    description: str

class SymbolTable(object):
    def __init__(self):
        self.symbols = list()

    def define(self, name: str, description: str) -> Symbol:
        symbol = Symbol(name)
        self.symbols.append(SymbolInfo(name, symbol, description))
        return symbol
    
    def _repr_markdown_(self):
        header = "Symbol | Description\n-------|:-----------\n"
        lines = [f"${latex(s.symbol)}$ | {s.description}" for s in self.symbols]
        return header + "\n".join(lines)

symbol_table = SymbolTable()

A = symbol_table.define('A', 'Area')
F = symbol_table.define('F', 'Force')
g = symbol_table.define('g', 'Acceleration due to gravity')
H = symbol_table.define('H', 'Geopotential height')
h = symbol_table.define('h', 'Geometric height')
P = symbol_table.define('P', 'Pressure')
P_b = symbol_table.define('P_b', 'Pressure at the base of an atmospheric layer')
M = symbol_table.define('M', 'Molecular mass')
m = symbol_table.define('m', 'Mass')
n = symbol_table.define('n', 'Amount of substance')
R_universal = symbol_table.define('R^*', 'Universal gas constant')
R = symbol_table.define('R', 'Specific gas constant')
T = symbol_table.define('T', 'Thermodynamic temperature')
V = symbol_table.define('V', 'Volume')

rho = symbol_table.define('rho', 'Density')

def _equality_div(equality, expr):
    """
    Monkey patch to allow both sides of an equation to be divided by an expr.
    """
    lhs = equality.lhs / expr
    rhs = equality.rhs / expr
    return Eq(lhs, rhs).simplify()

def _equality_isolate(equality: Equality, expr):
    """
    Monkey patch for algebraically solving an equation such that the given expr remains on the lhs.
    """
    solutions = solve(equality, expr)
    if len(solutions) < 0 or len(solutions) > 1:
        raise ArithmeticError(f"Expected a single solution of the express: {equality}")
    solution = solutions[0]
    return Eq(expr, solution)

Equality.__truediv__ = _equality_div
Equality.solve = _equality_isolate