#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Nafiseh
"""

# Import the Gurobi library
from gurobipy import *

# Create the model as an object
glass_co = Model ("glass_co")

# Mute the Gurobi
# pottery_co.setParam ('OutputFlag', False)


# Define the decion variables
x = glass_co.addVar(vtype=GRB.INTEGER, name = "door_batch")
y = glass_co.addVar(vtype=GRB.INTEGER, name = "window_batch")

# Define the set of constraints
glass_co.addConstr (1 * x  <= 4, name = "constraint_1")
glass_co.addConstr (2 * y  <= 12, name = "constraint_2")
glass_co.addConstr (3 * x + 2 * y <= 18, name = "constraint_3")


# Define the objective function
Z = 3000 * x + 5000 * y

# Specify the type of the model: minimization or maximization
glass_co.setObjective (Z, GRB.MAXIMIZE)

# Solve the model
glass_co.optimize()

# Print the objective value
if glass_co.status == GRB.OPTIMAL:
    print("Optimal value is --->", glass_co.objVal)


# print the optimal solutions: the decion variables values
glass_co.printAttr ('X')    
print ("Batch of doors is --->", x.X)
print ("Batch of windows is --->", y.X)