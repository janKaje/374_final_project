from help import *

def solve_head_losses(flowrates):
    """This function will be passed to the solver. Takes a 12-dimensional array of flowrates and outputs a 12-dimensional array of differences in head loss between pipes."""
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
        hl1(totalflow) + hl2(fl1 + fl2 + fl3 + fl4 + fl5 + fl6) + hl3(fl1) - pump_curve_B(totalflow)*8
        # We know from assume_1_gpm_last_sink.py that we need minimum 8 B pumps and that those will be most
        # cost-efficient (with regard to installation)
    ]

    residuals = [i.asNumber(ft) for i in residuals]

    return residuals


# put into solver
guess = [1 for i in range(12)]
flowrates = fsolve(solve_head_losses, guess)

# parse solver output
fl1, fl2, fl3, fl4, fl5, fl6, fl7, fl8, fl9, fl10, fl11, fl12 = [i * gal / minute for i in flowrates]

totalflow = sum(flowrates)*gal/minute

total_head_required = hl1(totalflow) + hl2(fl1 + fl2 + fl3 + fl4 + fl5 + fl6) + hl3(fl1)

shaft_work = total_head_required*totalflow*rhoWater*grav

wattage = shaft_work/0.8

# print(f"Make sure solver did well: {solve_head_losses(flowrates)}")
print(f"Maximum total flow: {totalflow}")
print(f"Maximum head required: {total_head_required}")
print(f"Maximum pressure required: {(total_head_required*rhoWater*grav).asUnit(psi)}")
print(f"Flowrates: {flowrates}")
print(f"Wattage required at maximum flow: {wattage.asUnit(W)}")
print(f"Cost of electricity for 1 month at 2023 US electricity prices, assuming constant max flow: {(wattage*(0.1272*USD/kWh)*(1*month))}")
