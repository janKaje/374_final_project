from scipy.optimize import fsolve

from units import *

# from problem statement
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


def friction(epsilon, diameter, Re):
    try:
        return Colebrook(epsilon, diameter, Re)
    except Exception as ex:
        print(f"Haaland eqn used instead of Colebrook due to error when calculating friction")
        print(f"Epsilon: {epsilon}")
        print(f"Diameter: {diameter}")
        print(f"Reynolds number: {Re}")
        return Haaland(epsilon, diameter, Re)


def Colebrook(epsilon, diameter, Re):
    if Re.asNumber() == 0:
        return 0
    solverr = lambda f: (f ** -0.5) - (
                -2 * np.log10(epsilon.asNumber(mm) / 3.7 / diameter.asNumber(mm) + 2.51 / Re.asNumber() / f ** 0.5))
    try:
        return fsolve(solverr, 0.00001)[0]
    except Exception as ex:
        print(solverr(0.00001))
        raise ex


def Haaland(epsilon, diameter, Re):
    if Re == 0:
        return 0
    return (-1.8 * np.log10(6.9 / Re.asNumber() + (epsilon.asNumber(mm) / 3.7 / diameter.asNumber(mm)) ** 1.11)) ** -2


def hLtotal(f, L, D, KLs, v):
    try:
        return v ** 2 / 2 / (9.81 * m / s ** 2) * (f * L / D + sum(KLs))
    except Exception as ex:
        print(f)
        print(L)
        print(D)
        print(KLs)
        print(v)
        raise ex
