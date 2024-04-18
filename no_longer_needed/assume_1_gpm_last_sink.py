from help import *

def solve_head_losses(flowrates):
    """This function will be passed to the solver. Takes an 11-dimensional array of flowrates and outputs an 11-dimensional array of differences in head loss between pipes."""
    # Transform array into more readable single variables and add units
    fl1, fl2, fl3, fl4, fl5, fl6, fl7, fl8, fl9, fl10, fl11 = [i * gal / minute for i in flowrates]
    fl12 = 1 * gal / minute  # hard set final sink flowrate to 1 gal/min

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
            fl7 + fl8 + fl9 + fl10 + fl11 + fl12) - hl14(fl7)
    ]

    residuals = [i.asNumber(ft) for i in residuals]

    return residuals


guess = [1 for i in range(11)]

flowrates = fsolve(solve_head_losses, guess)

fl1, fl2, fl3, fl4, fl5, fl6, fl7, fl8, fl9, fl10, fl11 = [i * gal / minute for i in flowrates]
fl12 = 1 * gal / minute  # hard set final sink flowrate to 1 gal/min
totalflow = fl1 + fl2 + fl3 + fl4 + fl5 + fl6 + fl7 + fl8 + fl9 + fl10 + fl11 + fl12

total_head_required = hl1(totalflow) + hl2(fl1 + fl2 + fl3 + fl4 + fl5 + fl6) + hl3(fl1)
print(f'Flowrates: {flowrates}')
print(f'Total required head: {total_head_required}')
print(f'Total required flow: {totalflow}')
print(f"Total required pump pressure: {(total_head_required*rhoWater*grav).asUnit(psi)}")
print(f"Cost of pumps given choice A: ${np.ceil(total_head_required/pump_curve_A(totalflow))*1500}")
print(f"Cost of pumps given choice B: ${np.ceil(total_head_required/pump_curve_B(totalflow))*800}")
print(f"Cost of pumps given choice C: ${np.ceil(total_head_required/pump_curve_C(totalflow))*250}")
print(f'Check to make sure solver did well: {solve_head_losses(flowrates)}')
print(f'Head supplied by pump A at flowrate: {pump_curve_A(totalflow)}')
print(f'Head supplied by pump B at flowrate: {pump_curve_B(totalflow)}')
print(f'Head supplied by pump C at flowrate: {pump_curve_C(totalflow)}')
print(f"Number of pumps of A required in series at flowrate: {np.ceil(total_head_required/pump_curve_A(totalflow))}")
print(f"Number of pumps of B required in series at flowrate: {np.ceil(total_head_required/pump_curve_B(totalflow))}")
print(f"Number of pumps of C required in series at flowrate: {np.ceil(total_head_required/pump_curve_C(totalflow))}")
