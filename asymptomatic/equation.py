from dataclasses import dataclass
from pylatex.base_classes.containers import Container, Environment
from pylatex.package import Package
from pylatex.utils import dumps_list
from sympy import *

# TODO: This could be submitted to PyLatex as a pull request.
class Align(Environment):
    """Class that represents an aligned equation environment."""

    #: Align environment cause compile errors when they do not contain items.
    #: This is why it is omitted fully if they are empty.
    omit_if_empty = True
    packages = [Package('amsmath')]

    def __init__(self, numbering=True, escape=False):
        """
        Parameters
        ----------
        numbering : bool
            Whether to number equations
        escape : bool
            if True, will escape strings
        """
        self.numbering = numbering
        self.escape = escape
        if not numbering:
            self._star_latex_name = True
        super().__init__()

def align(*args):
    environment = Align()
    environment.extend(args)
    return environment

class Line(Container):
    """Represents a single line in an amsmath environment, such as align."""
    def __init__(self):
        self.escape = False
        super().__init__()

    def append(self, item):
        super().append(item)
        return self

    def extend(self, other):
        super().extend(other)
        return self

    def text(self, text: str):
        return self.extend(['',f"\\text{{{text}}}"])

    def dumps(self):
        line = dumps_list(self, escape=False, token='&') + '\\\\\n'
        return line.replace('=', '&=')

class ExprStack(Line):
    """A wrapper around sympy's Eq expression which can be manipulated and annotaed with comments."""
    expr: Expr
    # TODO: Is there a better name than "prev"?    
    prev: 'ExprStack'

    def __init__(self, expr, prev=None):
        self, '_repr_attributes_override', []
        super().__init__()

        self.expr = expr
        self.prev = prev
        
        self.append(f"{latex(self.expr)}")

    def replace(self, query, value) -> 'ExprStack':
        replaced = self.expr.replace(query, value)
        comment = latex(Eq(query, value))
        return ExprStack(replaced, prev=self).append(comment)

    def solve(self, solve_for, **args):
        solutions = solve(self.expr, solve_for, **args)
        if len(solutions) < 0 or len(solutions) > 1:
            raise ArithmeticError(f"Expected a single solution, but found {len(solutions)}.")
        eq = Eq(solve_for, solutions[0], evaluate=False)
        return ExprStack(eq, prev=self)

    def dumps(self):
        if self.prev is not None:
            return self.prev.dumps() + super().dumps()
        else:
            return super().dumps()

def equation(lhs, rhs):
    return ExprStack(Eq(lhs, rhs)).extend(['',''])

# def _equality_div(equality, expr):
#     """
#     Monkey patch to allow both sides of an equation to be divided by an expr.
#     """
#     lhs = equality.lhs / expr
#     rhs = equality.rhs / expr
#     return Eq(lhs, rhs).simplify()

# def _equality_isolate(equality: Equality, expr):
#     """
#     Monkey patch for algebraically solving an equation such that the given expr remains on the lhs.
#     """
#     solutions = solve(equality, expr)
#     if len(solutions) < 0 or len(solutions) > 1:
#         raise ArithmeticError(f"Expected a single solution of the express: {equality}")
#     return Eq(expr, solutions[0])

# Equality.__truediv__ = _equality_div
# Equality.solve = _equality_isolate

# class EquationGroup(object):
#     """A collection of related equations that are grouped together for display."""
#     equations: list[Equation]

#     def __init__(self, lhs, rhs, comment=None):
#         self.equations = [Equation(Eq(lhs, rhs), comment)]

#     def replace(self, query:Expr, value:Expr, comment:str = None):
#         """Replaces from the last equation in this group the query expression with a new expression, appends the result."""
#         last = self.equations[-1]
#         new_eq = last.eq.replace(query, value)
#         comment = comment or latex(Eq(query, value))
#         next = Equation(new_eq, comment)
#         self.equations.append(next)
#         return self

#     def _repr_latex_(self):
#         header = "\\begin{align}"
#         equations_latex = [e._repr_latex_() for e in self.equations]
#         footer = "\\end{align}"
#         return header + "\\\\".join(equations_latex) + footer
