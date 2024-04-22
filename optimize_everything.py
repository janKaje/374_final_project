import json
from datetime import datetime as dt
from time import time as now
from display import summary, time_str
from solver_functions import build_parameter_array
from solver_functions import compute_cost_with_specifications as cost

logtext = ""

try:
    timetext = dt.now().strftime('%Y%m%d_%H%M%S')


    def log(txt):
        """Logs message to console and .log file."""
        print(txt)
        global logtext
        logtext += txt


    def solve_all(params):
        """Main solver function. Iterates through params, computing the cost breakdown and details of each set of parameters"""
        # Instantiate results list
        results = []

        # Start timer
        function_timer = now()

        log(f"Executing {len(params)} solver functions...\n")

        # Iterate
        counter = 0
        for param in params:

            # Compute and store
            results.append(cost(param))

            # Helpful log messages to let you know how far along the program is
            counter += 1
            if len(params) - counter != 0:
                time_left = round((now() - function_timer) / counter * (len(params) - counter))
                print(f"Estimated time remaining: {time_str(time_left)}")
            if counter % 10 == 0:
                time_taken = round(now() - function_timer)
                log(f"{counter} options solved so far in {time_str(time_taken)}.\n")

        # Report complete and return
        time_taken = round(now() - function_timer)
        log(f"Done! Solved {counter} functions in {time_str(time_taken)}.\n")
        return results


    # Start timer
    starttime = now()

    log("Building parameter array...\n")

    # Build parameters to be pushed to cost function
    params = build_parameter_array()

    log(f"Parameter array built! Time taken: {now() - starttime} seconds. {len(params)} arrays to try.\n")

    # Compute all
    solutions = solve_all(params)

    # Store raw data (full-length runs usually take over an hour
    # so being able to fetch rather than compute the data can save massive amounts of time
    with open("raw_data.json", "w") as file:
        json.dump(solutions, file)

    # Summarize
    log(f"Summarizing...\n")
    top5system = sorted(solutions, key=lambda x: x[3])[0:5]
    top5operation = sorted(solutions, key=lambda x: x[4])[0:5]
    log(f"Summary finished. Program done in {time_str(round(now() - starttime))}.\n")
    log(summary(top5system, "Top five with regards to system cost"))
    log(summary(top5operation, "Top five with regards to operation cost"))
    print("Logging data...")

    # Save to .log files
    with open("latest.log", "w") as file:
        file.write(logtext)
    with open(f"logs/run_{timetext}.log", "w") as file:
        file.write(logtext)
    print("Done logging. In the future you can import the json file if you'd like to see all the raw data.")

except Exception as ex:

    # In case of an error during execution, attempt to save data
    print("Error occured during execution. Attempting to save logs...")
    try:
        _ = solutions[0]
        with open("raw_data.json", "w") as file:
            json.dump(solutions, file)
        print("JSON file successfully saved")
    except:
        print("JSON file couldn't be saved")
    try:
        with open("latest.log", "w") as file:
            file.write(logtext)
        with open(f"logs/run_{timetext}.log", "w") as file:
            file.write(logtext)
        print("LOG files successfully saved")
    except:
        print("LOG files couldn't be saved")
    raise ex
