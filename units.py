from unum.units import *
from unum import Unum
import numpy as np

# This is to initialize Unum units. Nothing else.

# common AES/US Customary units
lb = Unum.unit('lb', 0.4535924 * kg)
ft = Unum.unit('ft', 0.3048 * m)
inch = Unum.unit('inch', 1 / 12 * ft)
yd = Unum.unit('yd', 3 * ft)
lbmol = Unum.unit('lbmol', 1 * mol * lb / g)
gal = Unum.unit('gal', 3.785412 * L)
lbf = Unum.unit('lbf', 32.174049 * ft * lb / s ** 2)
grain = Unum.unit('grain', lb / 7000)
slug = Unum.unit('slug', 32.1740486 * lb)
floz = Unum.unit('floz', gal / 128)
quart = Unum.unit('quart', gal / 4)
pint = Unum.unit('pint', gal / 8)
cup = Unum.unit('cup', gal / 16)
teaspoon = Unum.unit('teaspoon', gal / 768)
tablespoon = Unum.unit('tablespoon', gal / 256)
ton = Unum.unit('ton', 2000 * lb)
ounce = Unum.unit('ounce', lb / 16)

# pressure
kPa = Unum.unit('kPa', 1000 * Pa)
MPa = Unum.unit('MPa', 1e6 * Pa)
torr = Unum.unit('torr', 101325 / 760 * Pa)
psi = Unum.unit('psi', 101325 / 14.7 * Pa)
atm = Unum.unit('atm', 101325 * Pa)

# energy
cal = Unum.unit('cal', 4.184 * J)  # thermal calorie
kcal = Unum.unit('kcal', 1000 * cal)
erg = Unum.unit('erg', 1e-7 * J)
BTU = Unum.unit('BTU', 1.054350e3 * J)
kJ = Unum.unit('kJ', 1000 * J)
hp = Unum.unit('hp', 550 * lbf * ft / s)
kW = Unum.unit('kW', 1000 * W)
MW = Unum.unit('MW', 1000000 * W)

# viscosity
poise = Unum.unit('poise', 0.1 * Pa * s)
cP = Unum.unit('cP', 0.01 * poise)
μP = Unum.unit('μP', 1e-6 * poise)

# temperature
Rankine = Unum.unit('Rankine', 5 / 9 * K)

# time
minute = Unum.unit('minute', 60 * s)
hr = Unum.unit('hr', 60 * minute)
day = Unum.unit('day', 24 * hr)
year = Unum.unit('year', 365.25 * day)
week = Unum.unit('week', 7 * day)
month = Unum.unit('month', year / 12)

# rotational velocity
rpm = Unum.unit('rpm', 2 * np.pi * rad / minute)

# misc
lightyear = Unum.unit('lightyear', 9460660000000000 * m)
acre = Unum.unit('acre', m ** 2 / 4046.8564224)
hectare = Unum.unit('hectare', 10000 * m ** 2)
mL = Unum.unit('mL', 1 * cm ** 3)
metricton = Unum.unit('metricton', 1000 * kg)
carrat = Unum.unit('carrat', 0.2 * g)
amu = Unum.unit('amu', g / 6.022136652e23)
kWh = Unum.unit('kWh', kW * hr)
USD = Unum.unit('$')


def FtoK(Tf):
    """Returns with units"""
    Tr = (Tf + 459.67) * Rankine
    return Tr.asUnit(K)


def KtoF(TK):
    """Returns w/o units"""
    try:
        TK = TK.asNumber(K)
    except:
        pass
    Tr = TK * 1.8
    return Tr - 459.67
