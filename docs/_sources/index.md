# PyHAB

PyHAB is a library for high altitude balloon (HAB) projects, collecting several useful resources
in one place including:

* An atmospheric model used to derive...
* An altitude burst calculator
* A descent rate calculator
* A flight simulation model

## Methodology

Part of the inspiration for creating this library is doing research for my first HAB project,
Graupel-1, and getting frustrated with finding papers lacking in example code, and example
code lacking in documentation and derivations.

This is a problem across computing field, in general, I find, and so this project is trying
something a bit new: *generate the code from the documentation*.

The [Jupyter](https://jupyter.org/) notebooks on this site not only serve as the documentation
for the library, but they are also used to derive the mathematical models used **and** generate
the code from those models directly.