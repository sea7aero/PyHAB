from dataclasses import dataclass
from sympy import *

@dataclass(order=True, frozen=True)
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

