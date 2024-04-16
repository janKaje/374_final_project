from numpy import pi

from help import *


# Functions to calculate required head along each pipe
# See diagram for corresponding pipes to numbers

def hl1(flow):
    d = 1 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 20 * ft, d, [], v) + 20 * ft


def hl2(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 3 * ft, d, [branch_tee], v)


def hl3(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, toilet], v) + 4 * ft


def hl4(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 3 * ft, d, [straight_tee], v)


def hl5(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, toilet], v) + 4 * ft


def hl6(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 3 * ft, d, [straight_tee], v)


def hl7(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, toilet], v) + 4 * ft


def hl8(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 7.5 * ft, d, [straight_tee, bend * 2], v)


def hl9(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, sink], v) + 4 * ft


def hl10(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 3 * ft, d, [straight_tee], v)


def hl11(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, sink], v) + 4 * ft


def hl12(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 7 * ft, d, [straight_tee, bend, sink], v) + 4 * ft


def hl13(flow):
    d = 1 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 20 * ft, d, [straight_tee], v) + 20 * ft


def hl24(flow):  # yeah I know there's a random 24 right here, sorry it's confusing
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 3 * ft, d, [bend], v)


def hl14(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, toilet], v) + 4 * ft


def hl15(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 3 * ft, d, [straight_tee], v)


def hl16(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, toilet], v) + 4 * ft


def hl17(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 3 * ft, d, [straight_tee], v)


def hl18(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, toilet], v) + 4 * ft


def hl19(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 7.5 * ft, d, [straight_tee, bend * 2], v)


def hl20(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, sink], v) + 4 * ft


def hl21(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 3 * ft, d, [straight_tee], v)


def hl22(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 4 * ft, d, [branch_tee, sink], v) + 4 * ft


def hl23(flow):
    d = 0.75 * inch
    v = flow / (pi / 4 * d ** 2)
    return hLtotal(friction(epsilon, d, rhoWater * v * d / muWater), 7 * ft, d, [straight_tee, bend, sink], v) + 4 * ft


def pump_curve_A(flow):
    '''Returns supplied head at that flow for pump A'''
    return (60 - 0.03/(gal/minute)**2*flow**2)*ft


def solve_head_losses(flowrates):
    '''This function will be passed to the solver. Takes a 12-dimensional array of flowrates and outputs a 12-dimensional array of differences in head loss between pipes.'''
    # Transform array into more readable single variables and add units
    fl1, fl2, fl3, fl4, fl5, fl6, fl7, fl8, fl9, fl10, fl11, fl12 = [i * gal / minute for i in flowrates]
    totalflow = sum(flowrates)*gal/minute

    residuals = [
        # Top floor
        hl23(fl12) - hl22(fl11),
        hl21(fl12 + fl11) + hl22(fl11) - hl20(fl10),
        hl19(fl10 + fl11 + fl12) + hl20(fl10) - hl18(fl9),
        hl17(fl9 + fl10 + fl11 + fl12) + hl18(fl9) - hl16(fl8),
        hl15(fl8 + fl9 + fl10 + fl11 + fl12) + hl16(fl8) - hl14(fl7),

        # Bottom floor
        hl12(fl6) - hl11(fl5),
        hl10(fl5 + fl6) + hl11(fl5) - hl9(fl4),
        hl8(fl4 + fl5 + fl6) + hl9(fl4) - hl7(fl3),
        hl6(fl3 + fl4 + fl5 + fl6) + hl7(fl3) - hl5(fl2),
        hl4(fl2 + fl3 + fl4 + fl5 + fl6) + hl5(fl2) - hl3(fl1),

        # Split
        hl2(fl1 + fl2 + fl3 + fl4 + fl5 + fl6) + hl3(fl1) - hl13(fl7 + fl8 + fl9 + fl10 + fl11 + fl12) - hl24(
            fl7 + fl8 + fl9 + fl10 + fl11 + fl12) - hl14(fl7),

        # Pump
        hl1(totalflow) + hl2(fl1 + fl2 + fl3 + fl4 + fl5 + fl6) + hl3(fl1) - pump_curve_A(totalflow)*6
        # We know from assume_1_gpm_last_sink.py that we need minimum 6 A pumps and that those will be most cost-efficient
    ]

    residuals = [i.asNumber(ft) for i in residuals]

    return residuals


guess = [1 for i in range(12)]

flowrates = fsolve(solve_head_losses, guess)

fl1, fl2, fl3, fl4, fl5, fl6, fl7, fl8, fl9, fl10, fl11, fl12 = [i * gal / minute for i in flowrates]
totalflow = fl1 + fl2 + fl3 + fl4 + fl5 + fl6 + fl7 + fl8 + fl9 + fl10 + fl11 + fl12

total_head_required = hl1(totalflow) + hl2(fl1 + fl2 + fl3 + fl4 + fl5 + fl6) + hl3(fl1)
print(f"Make sure solver did well: {solve_head_losses(flowrates)}")
print(f"OPERATING POINT")
print(f"Maximum total flow: {totalflow}")
print(f"Maximum head required: {total_head_required}")
