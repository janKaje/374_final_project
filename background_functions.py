from scipy.optimize import fsolve
from numpy import pi
from units import *

# This module contains more trivial and low-level functions and variables that are constant throughout other functions.


# From problem statement
rhoWater = 62.3 * lb / ft ** 3
muWater = 6.733e-4 * lb / ft / s

# PVC roughness
# from https://www.pipeflow.com/pipe-pressure-drop-calculations/pipe-roughness
# confirmed by https://www.engineeringtoolbox.com/surface-roughness-ventilation-ducts-d_209.html
# and https://engineerexcel.com/relative-roughness/
epsilon = 0.0015 * mm

grav = 9.81 * m / s ** 2

gasconst = 8.31446261815324 * J / mol / K

# KLs:
branch_tee = 2
straight_tee = 0.9
toilet = 14 + 0.9 + 0.2  # every toilet comes with a bend and valve so it's all just grouped together for simplicity
sink = 10 + 0.9 + 0.2  # same here
bend = 0.9
valve = 0.2


# Friction and head loss finders

def friction(epsilon, diameter, Re):
    """Returns Darcy friction factor at given parameters.
    Tries the Colebrook equation first, then switches to Haaland if necessary."""
    try:
        return Colebrook(epsilon, diameter, Re)
    except Exception or RuntimeWarning as ex:
        print(f"Haaland eqn used instead of Colebrook due to error when calculating friction")
        print(f"Epsilon: {epsilon}")
        print(f"Diameter: {diameter}")
        print(f"Reynolds number: {Re}")
        print(ex)
        return Haaland(epsilon, diameter, Re)


def Colebrook(epsilon, diameter, Re):
    """Returns the Darcy friction factor according to the Colebrook equation."""
    if Re.asNumber() == 0:
        return 0  # if Re is 0, rest of code will break.
    solverr = lambda f: (f ** -0.5) - (
            -2 * np.log10(epsilon.asNumber(mm) / 3.7 / diameter.asNumber(mm) + 2.51 / Re.asNumber() / f ** 0.5))
    try:
        return fsolve(solverr, 0.00001)[0]
    except Exception or RuntimeWarning as ex:
        print(solverr(0.00001))
        raise ex


def Haaland(epsilon, diameter, Re):
    """Returns the Darcy friction factor according to the Haaland equation."""
    if Re.asNumber() == 0:
        return 0
    return (-1.8 * np.log10(6.9 / Re.asNumber() + (epsilon.asNumber(mm) / 3.7 / diameter.asNumber(mm)) ** 1.11)) ** -2


def hLtotal(f, L, D, KLs, v):
    """Computes the total head loss for the given parameters."""
    try:
        return v ** 2 / 2 / (9.81 * m / s ** 2) * (f * L / D + sum(KLs))
    except Exception as ex:
        print(f)
        print(L)
        print(D)
        print(KLs)
        print(v)
        raise ex


# Functions to calculate required head along each pipe
# See diagram for corresponding pipes to numbers
# Same as in help.py but diameter is an input to all
# And adds separate pipes for ends of floor pipes

def hl1(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 20 * ft, d, [], v) + 20 * ft


def hl2(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 3 * ft, d, [branch_tee], v)


def hl3(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, toilet], v) + 4 * ft


def hl4(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 3 * ft, d, [straight_tee], v)


def hl5(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, toilet], v) + 4 * ft


def hl6(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 3 * ft, d, [straight_tee], v)


def hl7(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, toilet], v) + 4 * ft


def hl8(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 7.5 * ft, d, [straight_tee, bend * 2], v)


def hl9(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, sink], v) + 4 * ft


def hl10(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 3 * ft, d, [straight_tee], v)


def hl11(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, sink], v) + 4 * ft


def hl12(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 3 * ft, d, [straight_tee], v)


def hl13(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 20 * ft, d, [straight_tee], v) + 20 * ft


def hl24(flow, d):  # yeah I know there's a random 24 right here, sorry it's confusing

    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 3 * ft, d, [bend], v)


def hl14(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, toilet], v) + 4 * ft


def hl15(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 3 * ft, d, [straight_tee], v)


def hl16(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, toilet], v) + 4 * ft


def hl17(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 3 * ft, d, [straight_tee], v)


def hl18(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, toilet], v) + 4 * ft


def hl19(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 7.5 * ft, d, [straight_tee, bend * 2], v)


def hl20(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, sink], v) + 4 * ft


def hl21(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 3 * ft, d, [straight_tee], v)


def hl22(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, sink], v) + 4 * ft


def hl23(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 3 * ft, d, [straight_tee], v)


def hl25(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [bend, sink], v) + 4 * ft


def hl26(flow, d):
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [bend, sink], v) + 4 * ft


# Pump curve functions
def pump_curve_A(flow):
    """Returns supplied head at that flow for pump A"""
    return (60 - 0.03 / (gal / minute) ** 2 * flow ** 2) * ft


def pump_curve_B(flow):
    """Returns supplied head at that flow for pump B"""
    return (40 - 0.02 / (gal / minute) ** 2 * flow ** 2) * ft


def pump_curve_C(flow):
    """Returns supplied head at that flow for pump C"""
    return (20 - 0.01 / (gal / minute) ** 2 * flow ** 2) * ft
