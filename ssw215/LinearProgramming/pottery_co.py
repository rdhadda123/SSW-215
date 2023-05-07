#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Nafiseh
"""

# Import the Gurobi library
from gurobipy import *

def myfunction (b_one, b_two):
    # Create the model as an object
    pottery_co = Model ("pottery_co")
    
    # Mute the Gurobi
    pottery_co.setParam ('OutputFlag', True)
    
    
    # Define the decion variables
    x = pottery_co.addVar(vtype=GRB.INTEGER, lb= 0, name = "bowls_no")
    y = pottery_co.addVar(vtype=GRB.INTEGER,lb =0,  name = "mugs_no")
    
    # Define the set of constraints
    pottery_co.addConstr (1* x + 2 * y <= b_one, name = "labor constraint")
    pottery_co.addConstr (4 * x + 3 * y <= b_two, name = "clay constraint")
    
    # Define the objective function
    Z = 40 * x + 50 * y
    
    # Specify the type of the model: minimization or maximization
    pottery_co.setObjective (Z, GRB.MAXIMIZE)
    
    # Solve the model
    pottery_co.optimize()
    
    # Print the objective value
    #if pottery_co.status == GRB.OPTIMAL:
        #print("Optimal value is --->", pottery_co.objVal)
    
    
    # print the optimal solutions: the decion variables values
    pottery_co.printAttr ('X')    
    number_of_mugs=  x.X
    number_of_bowls= y.X
    objective_value= pottery_co.objVal
    #print ("Number of bowls is --->", x.X)
    #print ("Number of mugs is --->", y.X)
    return number_of_mugs, number_of_bowls, objective_value
    
    
mugs, bowls, obj_val = myfunction (40, 120) 

print ("Here is the result --->", mugs, bowls, obj_val)   