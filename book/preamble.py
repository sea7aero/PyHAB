"""
This python module is intended to be included in each notebook and defines a bunch of common things for all of them.
"""
import numpy as np

from matplotlib import pyplot as plt
import seaborn as sns
sns.set_theme()

import pint
units = pint.UnitRegistry()
units.setup_matplotlib()

from symple import *

symbol_table = SymbolTable()

A = symbol_table.define('A', 'Area', positive=True)
C_d = symbol_table.define('C_d', 'Coefficient of drag')
D = symbol_table.define('D', 'Diameter', positive=True)
F = symbol_table.define('F', 'Force')
F_d = symbol_table.define('F_d', 'Force of drag')
F_g = symbol_table.define('F_g', 'Force of gravity')
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
v = symbol_table.define('v', 'Velocity')

rho = symbol_table.define('rho', 'Density')
