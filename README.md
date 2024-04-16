## 374 final project

Current version:

Computes operating point and shows that it produces the required head and flowrate. Assumes we're using 16 of Pump C. Feel free to pull and make edits and tweak things. We can probably just link to this site when submitting our python.

Below, all flowrates are flowrates out of the toilets and sinks, in units of gal/minute. Listed first is the first floor, then second, each going from closest to the main pipe to furthest away.

Output of assume_1_gpm_last_sink.py:
```
Flowrates: [8.44413328 6.16273439 4.76610446 2.88076267 2.30501932 2.20906167
            4.0730172  2.94887831 2.26262715 1.3388585  1.05406013]
Total required head: 68.6519438176606 [ft]
Total required flow: 39.44525708208349 [gal/minute]
Total required pump pressure: 29.719839432171888 [psi]
Cost of pumps given choice A: $9000
Cost of pumps given choice B: $6400
Cost of pumps given choice C: $4000
Head supplied by pump A at flowrate: 13.322150811850278 [ft]
Head supplied by pump B at flowrate: 8.881433874566849 [ft]
Head supplied by pump C at flowrate: 4.440716937283424 [ft]
Number of pumps of A required in series at flowrate: 6
Number of pumps of B required in series at flowrate: 8
Number of pumps of C required in series at flowrate: 16
```
This one is missing the last sink in the flowrates because it is assumed to be 1 gal/minute

Output of solve_operating_point_pump_A.py:
```
Maximum total flow: 40.1571320300051 [gal/minute]
Maximum head required: 69.73285448245441 [ft]
Maximum pressure required: 30.187772160828725 [psi]
Flowrates: [8.52389583 6.2215246  4.81201538 2.90923581 2.32823715 2.23156689
            4.21470215 3.05271696 2.34325034 1.38807275 1.09372465 1.03818952]
Wattage required at maximum flow: 585.7501714838108 [W]
Cost of electricity for 1 month at 2023 US electricity prices, assuming constant max flow: 54.42767163420711 [$]
```

Output of solve_operating_point_pump_B.py:
```
Maximum total flow: 39.61475020547186 [gal/minute]
Maximum head required: 68.90745058529323 [ft]
Maximum pressure required: 29.830449848798164 [psi]
Flowrates: [8.46302311 6.17665708 4.7769768  2.88750502 2.31051694 2.21439039
            4.10686456 2.97368162 2.28188288 1.3506089  1.06352819 1.00911471]
Wattage required at maximum flow: 642.3739477092164 [W]
Cost of electricity for 1 month at 2023 US electricity prices, assuming constant max flow: 59.68913027156131 [$]
```

Output of solve_operating_point_pump_C.py:
```
Maximum total flow: 39.61475020547186 [gal/minute]
Maximum head required: 68.90745058529323 [ft]
Maximum pressure required: 29.830449848798164 [psi]
Flowrates: [8.46302311 6.17665708 4.7769768  2.88750502 2.31051694 2.21439039
            4.10686456 2.97368162 2.28188288 1.3506089  1.06352819 1.00911471]
Wattage required at maximum flow: 734.1416545248188 [W]
Cost of electricity for 1 month at 2023 US electricity prices, assuming constant max flow: 68.21614888178436 [$]
```


As you can see, both the flowrate and head are greater at the operating point than the minimum required no matter which type of pump is used, meaning that the system meets the specifications.