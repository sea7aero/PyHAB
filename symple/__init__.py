"""
This python module is a quick proof of concept of an idea I have - demonstrated in this library -
for creating writing documentation first and generating code from it.  It extends the sympy library
to allow me to manipulate equations in code, and output the results as a document and also generate
code from the result.
"""

from sympy import *

from IPython.display import Math

from dataclasses import dataclass

@dataclass(order=True)
class SymbolInfo(object):
    name: str
    symbol: Symbol
    description: str

class SymbolTable(object):
    """
    Information about symbols used in 
    """
    def __init__(self):
        self.symbols = list()

    def define(self, name: str, description: str, **assumptions) -> Symbol:
        symbol = Symbol(name, **assumptions)
        self.symbols.append(SymbolInfo(name, symbol, description))
        return symbol
    
    def _repr_html_(self):
        header = "<table><tr><th>Symbol</th><th>Description</th></tr>"
        lines = [f"<tr><td>${latex(s.symbol)}$</td><td>{s.description}</td></tr>" for s in self.symbols]
        return header + "".join(lines)

    # def _repr_markdown_(self):
    #     header = "Symbol | Description\n-------|:-----------\n"
    #     lines = [f"${latex(s.symbol)}$ | {s.description}" for s in self.symbols]
    #     return header + "\n".join(lines)

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
    return Eq(expr, solutions[0])

Equality.__truediv__ = _equality_div
Equality.solve = _equality_isolate

@dataclass
class Equation(object):
    """A wrapper around sympy's Eq expression which can be annotaed with latex descriptions and labels."""
    eq: Eq

    

class ExpressionRegistry(object):
    """An expression registry is a heirarchical collection of expressions used in a text."""
    pass