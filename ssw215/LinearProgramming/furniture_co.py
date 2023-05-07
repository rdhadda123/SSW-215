#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Nafiseh
"""

# Import the Gurobi library
from gurobipy import *

def myfunction (b_one, b_two, b_three):
    # Create the model as an object
    furniture_co = Model ("furniture_co")
    
    # Mute the Gurobi
    # pottery_co.setParam ('OutputFlag', False)
    
    
    # Define the decion variables
    x = furniture_co.addVar(vtype=GRB.INTEGER, name = "no_table")
    y = furniture_co.addVar(vtype=GRB.INTEGER, name = "no_chair")
    
    # Define the set of constraints
    furniture_co.addConstr (5*x+2*y<=b_one, name = "constraint_1")
    furniture_co.addConstr (2*x+3*y<=b_two, name = "constraint_2")
    furniture_co.addConstr (4*x+2*y<=b_three, name = "constraint_3")
    
    
    # Define the objective function
    Z = 12* x+8*y
    
    # Specify the type of the model: minimization or maximization
    furniture_co.setObjective (Z, GRB.MAXIMIZE)
    
    # Solve the model
    furniture_co.optimize()
    
    # Print the objective value
    if furniture_co.status == GRB.OPTIMAL:
        print("Optimal value is --->", furniture_co.objVal)
    
    
    # print the optimal solutions: the decion variables values
    furniture_co.printAttr ('X') 
    no_of_table= x.X
    no_of_chair =y.X
    print ("# of tables are --->", x.X)
    print ("# of chairs are --->", y.X)
    objective_value= furniture_co.objVal
    return no_of_table, no_of_chair, objective_value
    
    
table, chair, obj_val = myfunction (150, 100, 80) 

print ("Here is the result --->", chair, table, obj_val)   