Constants:
* avagadro's number: N_A
* boltzman constant: k_B
* universal gas constant: R = N_A * k_B
* gravitational constant: G


Models:
* coordinate reference system (CRS): WGS84 is used by GPS
* atmospheric model: ISA is used by aviation
  * https://en.wikipedia.org/wiki/International_Standard_Atmosphere
  * standard gravitational acceleration: g
  * specific gas constant of dry air: R_dry
* specific gas constants

Inputs:
* position (lat/lon/alt), referenced to CRS

Notes:
* elevation (elev): distance above MSL that the terrain is at
* altitude (Alt): distance above MSL that the aircraft is
* height (H): distance above terrain (H = alt - elev)
* flight level (FL): altitude based on an atmospheric model

* FL is "geopotential altitude": an altitude based on the assumption that the force of gravity is constant
* "goemetric altitude": altitude as measured by a ruler (or GPS).

https://wahiduddin.net/calc/refs/measures_of_altitude_mahoney.html

Data Types:
* Simulation:
    * Vehicle:
        * Balloon: burst parameters, mass
        * Parachute: mass, coefficient of drag, area
        * Payload: mass
    * Position: X, Y, Z
    * Atmospheric Model
    * Constants
    
    

* Vehicle: Balloon, Parachute
* Simulation

Simulator(atmospheric_model, vehicle):
  * ascent rate
      
  * derive the descent rate