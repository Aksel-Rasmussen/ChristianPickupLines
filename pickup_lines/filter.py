#!/bin/env python3

with open("pickuplines.csv", 'r') as f:
    l = f.readlines()
s = set()

[s.add(i) for i in l]

with open("filteredpickuplines.csv", 'w') as f:
    f.writelines(s)
