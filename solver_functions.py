from background_functions import *
from scipy.optimize import fsolve


def pumps_required(flowrates, d):
    """Goes to solve_pumps_required to figure out how many pumps the system will need.
    This function assumes that the last sink will have a flowrate of 1 gpm. It's used to solve
    for the flowrates at each appliance that will make appropriate head losses equal."""

    # Break apart array for better legibility
    fl1, fl2, fl3, fl4, fl5, fl6, fl7, fl8, fl9, fl10, fl11 = [i * gal / minute for i in flowrates]
    fl12 = 1 * gal / minute  # hard set final sink flowrate to 1 gal/min

    # Add units to diameters (required for head loss, friction functions)
    d = [i * inch for i in d]

    # Array which fsolve will try to make zero.
    residuals = [
        # Top floor
        hl23(fl12, d[3]) + hl26(fl12, d[4]) - hl22(fl11, d[4]),
        hl21(fl12 + fl11, d[3]) + hl22(fl11, d[4]) - hl20(fl10, d[4]),
        hl19(fl10 + fl11 + fl12, d[3]) + hl20(fl10, d[4]) - hl18(fl9, d[4]),
        hl17(fl9 + fl10 + fl11 + fl12, d[3]) + hl18(fl9, d[4]) - hl16(fl8, d[4]),
        hl15(fl8 + fl9 + fl10 + fl11 + fl12, d[3]) + hl16(fl8, d[4]) - hl14(fl7, d[4]),

        # Bottom floor
        hl12(fl6, d[1]) + hl25(fl6, d[2]) - hl11(fl5, d[2]),
        hl10(fl5 + fl6, d[1]) + hl11(fl5, d[2]) - hl9(fl4, d[2]),
        hl8(fl4 + fl5 + fl6, d[1]) + hl9(fl4, d[2]) - hl7(fl3, d[2]),
        hl6(fl3 + fl4 + fl5 + fl6, d[1]) + hl7(fl3, d[2]) - hl5(fl2, d[2]),
        hl4(fl2 + fl3 + fl4 + fl5 + fl6, d[1]) + hl5(fl2, d[2]) - hl3(fl1, d[2]),

        # Split
        hl2(fl1 + fl2 + fl3 + fl4 + fl5 + fl6, d[1]) + hl3(fl1, d[2]) - hl13(fl7 + fl8 + fl9 + fl10 + fl11 + fl12, d[0]) \
        - hl24(fl7 + fl8 + fl9 + fl10 + fl11 + fl12, d[3]) - hl14(fl7, d[4])
    ]

    # Strip units away to avoid unit errors
    residuals = [i.asNumber(ft) for i in residuals]

    # Flow must be greater than one. If less than one, drastically increase residuals to discourage fsolve from doing so
    if any([flow < 1 for flow in flowrates]):
        residuals = [(err + 1) * 1e4 if err > 0 else (err - 1) * 1e4 for err in residuals]

    if __name__ == "__main__":
        # print(residuals)
        pass

    return residuals


def solve_pumps_required(d, pump_type):
    """Solves for the number of pumps required, both in series and in parallel.
    Works by first solving for the flowrates, then computing the head required to push those flowrates through pipes,
    then depending on which type of pump is used, calculates how many pumps are required."""

    # Guess obtained from no_longer_needed/assume_1_gpm.py. Relatively close in almost all instances.
    guess = [8.44413328, 6.16273439, 4.76610446, 2.88076267, 2.30501932, 2.20906167, 4.0730172, 2.94887831, 2.26262715,
             1.3388585, 1.05406013]

    # Pass to fsolve
    flowrates, dic, ier, msg = fsolve(pumps_required, guess, args=d, full_output=True)

    # If solution did not converge, return an absurdly high number of pumps
    # if ier != 1:
    #     return [1e3, 1e3]

    # Parse function return
    fl1, fl2, fl3, fl4, fl5, fl6, fl7, fl8, fl9, fl10, fl11 = [i * gal / minute for i in flowrates]
    fl12 = 1 * gal / minute  # hard set final sink flowrate to 1 gal/min
    totalflow = sum(flowrates) * gal / minute + fl12
    d = [i * inch for i in d]

    # Total head required by system
    total_head_required = hl1(totalflow, d[0]) + hl13(fl7 + fl8 + fl9 + fl10 + fl11 + fl12, d[0]) \
                          + hl24(fl7 + fl8 + fl9 + fl10 + fl11 + fl12, d[3]) + hl14(fl7, d[4])
    # Same number, used for debugging
    total_head_required_alt = hl1(totalflow, d[0]) + hl2(fl1 + fl2 + fl3 + fl4 + fl5 + fl6, d[1]) \
                              + hl3(fl1, d[2])

    # Only runs if this file itself is run, not if it is imported to another file. Used for debugging.
    if __name__ == "__main__":
        print("\nDEBUG solver")
        print(flowrates)
        print(totalflow)
        print("check heads")
        print(total_head_required)
        print(total_head_required_alt)
        print("check solver")
        print(pumps_required(flowrates, [i.asNumber(inch) for i in d]))
        if pump_type == "A":
            print(pump_curve_A(totalflow))
        if pump_type == "B":
            print(pump_curve_B(totalflow))
        if pump_type == "C":
            print(pump_curve_C(totalflow))

    # Calculate number of pumps required based on previous work
    if pump_type == "A":

        # Starts by assuming only 1 in parallel. Increases until the flowrate is sufficient.
        no_parallel = 1
        while pump_curve_A(totalflow / no_parallel) <= 0*ft and no_parallel < 100:
            no_parallel += 1
        if no_parallel > 99:
            raise RuntimeError(
                f"Critical error occured while trying to calculate number of necessary pumps. Pump A x {no_parallel} was reached")

        # Returns a list: first is number of pumps in series, second is number of pumps in parallel.
        return [np.ceil(total_head_required / pump_curve_A(totalflow / no_parallel)), no_parallel]

    # Similar functions below.
    if pump_type == "B":

        no_parallel = 1
        while pump_curve_B(totalflow / no_parallel) <= 0*ft and no_parallel < 100:
            no_parallel += 1
        if no_parallel > 99:
            raise RuntimeError(
                f"Critical error occured while trying to calculate number of necessary pumps. Pump B x {no_parallel} was reached")

        return [np.ceil(total_head_required / pump_curve_B(totalflow / no_parallel)), no_parallel]

    if pump_type == "C":

        no_parallel = 1
        while pump_curve_C(totalflow / no_parallel) <= 0*ft and no_parallel < 100:
            no_parallel += 1
        if no_parallel > 99:
            raise RuntimeError(
                f"Critical error occured while trying to calculate number of necessary pumps. Pump C x {no_parallel} was reached")

        return [np.ceil(total_head_required / pump_curve_C(totalflow / no_parallel)), no_parallel]


def head_losses(flowrates, d, pump, number_of_pumps):
    """This function will be passed to the solver. Takes a 12-dimensional array of flowrates and outputs a
    12-dimensional array of differences in head loss between pipes. Also requires input of pipe diameters, pump type,
    and number of pumps that will be set in series."""

    # Transform array into more readable single variables and add units
    fl1, fl2, fl3, fl4, fl5, fl6, fl7, fl8, fl9, fl10, fl11, fl12 = [i * gal / minute for i in flowrates]
    totalflow = sum(flowrates) * gal / minute
    d = [i * inch for i in d]

    # Calculate residuals, which fsolve will try to make zero by tweaking flowrates.
    residuals = [
        # Top floor
        hl23(fl12, d[3]) + hl26(fl12, d[4]) - hl22(fl11, d[4]),
        hl21(fl12 + fl11, d[3]) + hl22(fl11, d[4]) - hl20(fl10, d[4]),
        hl19(fl10 + fl11 + fl12, d[3]) + hl20(fl10, d[4]) - hl18(fl9, d[4]),
        hl17(fl9 + fl10 + fl11 + fl12, d[3]) + hl18(fl9, d[4]) - hl16(fl8, d[4]),
        hl15(fl8 + fl9 + fl10 + fl11 + fl12, d[3]) + hl16(fl8, d[4]) - hl14(fl7, d[4]),

        # Bottom floor
        hl12(fl6, d[1]) + hl25(fl6, d[2]) - hl11(fl5, d[2]),
        hl10(fl5 + fl6, d[1]) + hl11(fl5, d[2]) - hl9(fl4, d[2]),
        hl8(fl4 + fl5 + fl6, d[1]) + hl9(fl4, d[2]) - hl7(fl3, d[2]),
        hl6(fl3 + fl4 + fl5 + fl6, d[1]) + hl7(fl3, d[2]) - hl5(fl2, d[2]),
        hl4(fl2 + fl3 + fl4 + fl5 + fl6, d[1]) + hl5(fl2, d[2]) - hl3(fl1, d[2]),

        # Split
        hl2(fl1 + fl2 + fl3 + fl4 + fl5 + fl6, d[1]) + hl3(fl1, d[2]) - hl13(fl7 + fl8 + fl9 + fl10 + fl11 + fl12,
                                                                             d[0]) - hl24(
            fl7 + fl8 + fl9 + fl10 + fl11 + fl12, d[3]) - hl14(fl7, d[4])
    ]

    # Add pump head term to residuals
    if pump == "A":
        residuals.append(
            hl1(totalflow, d[0]) + hl2(fl1 + fl2 + fl3 + fl4 + fl5 + fl6, d[1]) + hl3(fl1, d[2]) - pump_curve_A(
                totalflow) * number_of_pumps)

    elif pump == "B":
        residuals.append(
            hl1(totalflow, d[0]) + hl2(fl1 + fl2 + fl3 + fl4 + fl5 + fl6, d[1]) + hl3(fl1, d[2]) - pump_curve_B(
                totalflow) * number_of_pumps)

    elif pump == "C":
        residuals.append(
            hl1(totalflow, d[0]) + hl2(fl1 + fl2 + fl3 + fl4 + fl5 + fl6, d[1]) + hl3(fl1, d[2]) - pump_curve_C(
                totalflow) * number_of_pumps)

    # Take away units
    residuals = [i.asNumber(ft) for i in residuals]

    # Flow must be greater than one. If less than one, drastically increase residuals to discourage fsolve from doing so
    if any([flow < 1 for flow in flowrates]):
        residuals = [(err + 1) * 1e4 if err > 0 else (err - 1) * 1e4 for err in residuals]

    return residuals


def solve_head_losses(d, pump):
    """Easy port to fsolve"""
    # Call for number of pumps
    number_of_pumps = solve_pumps_required(d, pump)

    # Guess obtained from no_longer_needed/assume_1_gpm.py. Relatively close in almost all instances.
    guess_array = [8.44413328, 6.16273439, 4.76610446, 2.88076267, 2.30501932, 2.20906167, 4.0730172, 2.94887831,
                   2.26262715, 1.3388585, 1.05406013, 1]

    # Solve for actual head losses
    soln, dic, ier, msg = fsolve(head_losses, guess_array, args=(d, pump, number_of_pumps[0]), full_output=True)

    # In case solution did not converge, remove from list.
    if ier != 1:
        return [1e3 for i in range(12)], [1e3, 1e3]  # Making everything huge will remove it from relevant summaries

    # Return both if everything turned out well
    return soln, number_of_pumps


def count_system_pipe_cost(d):
    """Counts up dollar value of pvc pipe, fittings, and valves"""

    cost = 0
    # Main pipe
    if d[0] == 1:
        cost += 1.25 * 40
        if d[1] == 1:  # bottom floor
            cost += 0.5
        elif d[1] == 0.75:
            cost += 0.6
        elif d[1] == 0.5:
            cost += 0.5
        if d[3] == 1:  # top floor
            cost += 0.4
        elif d[3] == 0.75:
            cost += 0.6
        elif d[3] == 0.5:
            cost += 0.5
    elif d[0] == 0.75:
        cost += 40
        cost += 0.3  # 3/4 tee and 3/4 to 1/2 tee are the same price
        cost += 0.3  # same with bend
    elif d[0] == 0.5:
        cost += 0.75 * 40
        cost += 0.2
        cost += 0.2

    # Floor pipe: first floor
    if d[1] == 1:
        cost += 1.25 * (3 * 5 + 7.5)  # pipe
        if d[2] == 1:
            cost += 5 * 0.5 + 0.4  # fittings along pipe
        elif d[2] == 0.75:
            cost += 6 * 0.6
        elif d[2] == 0.5:
            cost += 6 * 0.5
    elif d[1] == 0.75:
        cost += (3 * 5 + 7.5)
        if d[2] == 0.75:  # etc
            cost += 6 * 0.3
        elif d[2] == 0.5:
            cost += 6 * 0.3
    elif d[1] == 0.5:
        cost += 0.75 * (3 * 5 + 7.5)
        cost += 6 * 0.2

    # Floor pipe: second floor
    if d[3] == 1:
        cost += 1.25 * (3 * 5 + 7.5)  # pipe
        if d[4] == 1:
            cost += 5 * 0.5 + 0.4  # fittings along pipe
        elif d[4] == 0.75:
            cost += 6 * 0.6
        elif d[4] == 0.5:
            cost += 6 * 0.5
    elif d[3] == 0.75:
        cost += (3 * 5 + 7.5)
        if d[4] == 0.75:  # etc
            cost += 6 * 0.3
        elif d[4] == 0.5:
            cost += 6 * 0.3
    elif d[3] == 0.5:
        cost += 0.75 * (3 * 5 + 7.5)
        cost += 6 * 0.2

    # Toilet and sink pipes: floor 1
    if d[2] == 1:
        cost += 4 * 6 * 1.25  # pipe
        cost += 6 * 0.4  # bend
        cost += 6 * 100  # valve
    elif d[2] == 0.75:
        cost += 4 * 6  # etc
        cost += 6 * 0.3
        cost += 6 * 75
    elif d[2] == 0.5:
        cost += 4 * 6 * 0.75
        cost += 6 * 0.2
        cost += 6 * 50

    # Toilet and sink pipes: floor 2
    if d[4] == 1:
        cost += 4 * 6 * 1.25  # pipe
        cost += 6 * 0.4  # bend
        cost += 6 * 100  # valve
    elif d[4] == 0.75:
        cost += 4 * 6  # etc
        cost += 6 * 0.3
        cost += 6 * 75
    elif d[4] == 0.5:
        cost += 4 * 6 * 0.75
        cost += 6 * 0.2
        cost += 6 * 50

    return cost


def compute_cost_with_specifications(array_of_arguments):
    """The workhorse of the program. Puts everything together.
    The first five entries to the input array are the diameters of different sections of pipe.
    The sixth and last entry is the pump type."""

    # Split array
    diams = array_of_arguments[0:5]
    pump_type = array_of_arguments[5]

    # Call for flowrates and number of pumps
    flowrates, no_pumps = solve_head_losses(diams, pump_type)

    # Call for cost of piping
    pipe_cost = count_system_pipe_cost(diams)

    # Parse flowrates
    fl1, fl2, fl3, fl4, fl5, fl6, fl7, fl8, fl9, fl10, fl11, fl12 = [i * gal / minute for i in flowrates]
    totalflow = sum(flowrates) * gal / minute

    # Calculate total head required by system (which thanks to fsolve is the same as pump head delivered
    total_head_required = hl1(totalflow, diams[0] * inch) + hl2(fl1 + fl2 + fl3 + fl4 + fl5 + fl6,
                                                                diams[1] * inch) + hl3(fl1, diams[2] * inch)

    # Calculate wattage and cost of pumps
    shaft_work = total_head_required * totalflow * rhoWater * grav
    wattage = 0
    pump_cost = 0
    if pump_type == "A":
        pump_cost = 1500 * no_pumps[0] * no_pumps[1]
        wattage = shaft_work / 0.9
    elif pump_type == "B":
        pump_cost = 800 * no_pumps[0] * no_pumps[1]
        wattage = shaft_work / 0.8
    elif pump_type == "C":
        pump_cost = 250 * no_pumps[0] * no_pumps[1]
        wattage = shaft_work / 0.7

    # Calculate total system cost, monthly maximum operating cost.
    # Assumes average 2023 US electricity price of 12.72 cents/kWh
    system_cost = pipe_cost + pump_cost
    month_operating_cost = (wattage * (0.1272 / kWh) * (1 * month)).asNumber()

    # Left from debugging
    if __name__ == "__main__":
        print("DEBUG cost fun")
        print(total_head_required)
        print(pump_curve_C(totalflow/no_pumps[1])*no_pumps[0])

    # Return every necessary bit of information
    return [diams, pump_type, no_pumps, system_cost, month_operating_cost, list(flowrates),
            totalflow.asNumber(gal / minute), total_head_required.asNumber(ft)]


def build_parameter_array():
    """Simply iterates through all possible combinations of diameter sizing and pump choice.
    Assumes diameter will only decrease along flow of pipe."""
    params = []
    for D0choice in [0.5, 0.75, 1]:
        for D1choice in [0.5, 0.75, 1]:
            for D2choice in [0.5, 0.75, 1]:
                if D2choice > D1choice or D1choice > D0choice:
                    continue
                for D3choice in [0.5, 0.75, 1]:
                    for D4choice in [0.5, 0.75, 1]:
                        if D4choice > D3choice or D3choice > D0choice:
                            continue
                        for pumpchoice in ["A", "B", "C"]:
                            params.append([D0choice, D1choice, D2choice, D3choice, D4choice, pumpchoice])

    return params

# More debugging
if __name__ == "__main__":
    print("DEBUG main")
    print(compute_cost_with_specifications([1, 1, 0.5, 1, 0.5, "C"]))
