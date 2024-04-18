# 374 Final Project

This is the python code used to assist with BYU CH EN 374 Winter 2024 final project. 

* `latest.log` has main final output 
* `optimize_everything.py` is the main python file to run
* `display.py`, `background_functions.py`, `parse_json.py`, `solver_functions.py`, and `units.py` are all supplementary files
* `diagram_and_notes.pdf` is a hand-drawn diagram of the system, used to help me understand and keep track of things. Some numbers on it correspond to some in the code, but good luck figuring out what's what
* `\logs` houses all logs
* `\no_longer_needed` houses old code that's no longer used, but there for backup reasons
* `raw_data.json` contains all the raw data used in optimization from the past run

The optimizer has run and all relevant data can be found in `latest.log`.

## Method

This incredibly cutting-edge optimization technique consists of iterating through each possible combination of diameter sizes and pump types, calculating the total system cost and monthly maximum operating cost of each combination, and sorts all permutations of said parameters by those costs. The program follows the following steps:
1) A list of all possible permutations of parameters are made
2) For each one:
   1) The last sink on the last floor is assumed to have a flowrate of 1 gpm and fsolve is called to find the necessary flowrates through all other appliances to make that happen
   2) The minimum amounts of the given pump type (both in series and in parallel) necessary to sustain said flow are calculated
   3) The actual operating point is calculated by another call to fsolve
   4) The system cost (or installation cost -- the cost of all physical components in the given system) is calculated, and
   5) The maximum monthy operating cost (just electricity) is estimated
3) The different relevant quantities are compiled, sorted, and logged

As you can tell, this is not very fast. fsolve is called an insane number of times and there are many, many tasks to run. Each run takes about an hour and thirty minutes on my laptop to compute. For this reason, the raw output data as well as detailed logs are written to file to avoid having to run this program over and over again.

## Assumptions

The 90-degree bends made to route the pipe to the other side of the room in each floor are considered to be exactly at the rightmost toilet and sink. Technically they would have to be set at least an inch or two to the right, but that length is considered negligible.

The total loss of pressure and kinetic energy along a length of piping is assumed to be equal to the energy lost to friciton plus the energy converted to gravitational potential energy. Thus we can assume that it would behave the same exact way as would a similarly structured system that was laid flat, where each pipe that would lead "up" instead has that height differential more head loss.

There are only 5 relevant categories for pipe sizes: the main vertical pipe that goes from the basement all the way to the second floor, each floor's pipe that runs under the floor, and each floor's collection of vertical pipes that run from the floor to appliances. This vastly simplifies calculation (and the lives of the hypothetical plumbers that might be installing this).

All pumps are directly at the entrance to the main pipe at z=0. In practice, pump systems (especially those with many in series and/or parallel) would need extra piping to connect them which would slightly change the system curve, but for ease of calculation and because of the magnitude of other losses this is considered negligible.

Pipe diameter is assumed to never increase along the path of water flow. It just makes sense that the pipes with more flow should be bigger, and also drastically reduces computation time.