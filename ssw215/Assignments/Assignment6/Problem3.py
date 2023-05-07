from gurobipy import *

problemThree = Model("problemThree")

#Part A and B
#Decision variables for official Team A for each city (Integers)
AR = problemThree.addVar(vtype = GRB.INTEGER, name = "Offical_A_Raleigh")
AA = problemThree.addVar(vtype = GRB.INTEGER, name = "Offical_A_Atlanta")
AD = problemThree.addVar(vtype = GRB.INTEGER, name = "Offical_A_Durham")
AC = problemThree.addVar(vtype = GRB.INTEGER, name = "Offical_A_Clemson")

#Decision variables for official Team B for each city (Integers)
BR = problemThree.addVar(vtype = GRB.INTEGER, name = "Offical_B_Raleigh")
BA = problemThree.addVar(vtype = GRB.INTEGER, name = "Offical_B_Atlanta")
BD = problemThree.addVar(vtype = GRB.INTEGER, name = "Offical_B_Durham")
BC = problemThree.addVar(vtype = GRB.INTEGER, name = "Offical_B_Clemson")

#Decision variables for official Team C for each city (Integers)
CR = problemThree.addVar(vtype = GRB.INTEGER, name = "Offical_C_Raleigh")
CA = problemThree.addVar(vtype = GRB.INTEGER, name = "Offical_C_Atlanta")
CD = problemThree.addVar(vtype = GRB.INTEGER, name = "Offical_C_Durham")
CC = problemThree.addVar(vtype = GRB.INTEGER, name = "Offical_C_Clemson")

#Decision variables for official Team D for each city (Integers)
DR = problemThree.addVar(vtype = GRB.INTEGER, name = "Offical_D_Raleigh")
DA = problemThree.addVar(vtype = GRB.INTEGER, name = "Offical_D_Atlanta")
DD = problemThree.addVar(vtype = GRB.INTEGER, name = "Offical_D_Durham")
DC = problemThree.addVar(vtype = GRB.INTEGER, name = "Offical_D_Clemson")
#End of part A and B

#Constraints as given in model
problemThree.addConstr(AR + AA + AD + AC == 1, name = "officialA_constraint")
problemThree.addConstr(BR + BA + BD + BC == 1, name = "officialB_constraint")
problemThree.addConstr(CR + CA + CD + CC == 1, name = "officialC_constraint")
problemThree.addConstr(DR + DA + DD + DC == 1, name = "officialD_constraint")
problemThree.addConstr(AR + BR + CR + DR == 1, name = "Raleigh_constraint")
problemThree.addConstr(AA + BA + CA + DA == 1, name = "Atlanta_constraint")
problemThree.addConstr(AD + BD + CD + DD == 1, name = "Clemson_constraint")
problemThree.addConstr(AC + BC + CC + DC == 1, name = "Durham_constraint")

#All nonzero constraints    
problemThree.addConstr(AR >= 0, name = "nonzero_constraint_1")
problemThree.addConstr(AA >= 0, name = "nonzero_constraint_2")
problemThree.addConstr(AD >= 0, name = "nonzero_constraint_3")
problemThree.addConstr(AC >= 0, name = "nonzero_constraint_4")
problemThree.addConstr(BR >= 0, name = "nonzero_constraint_5")
problemThree.addConstr(BA >= 0, name = "nonzero_constraint_6")
problemThree.addConstr(BD >= 0, name = "nonzero_constraint_7")
problemThree.addConstr(BC >= 0, name = "nonzero_constraint_8")
problemThree.addConstr(CR >= 0, name = "nonzero_constraint_9")
problemThree.addConstr(CA >= 0, name = "nonzero_constraint_10")
problemThree.addConstr(CD >= 0, name = "nonzero_constraint_11")
problemThree.addConstr(CC >= 0, name = "nonzero_constraint_12")
problemThree.addConstr(DR >= 0, name = "nonzero_constraint_13")
problemThree.addConstr(DA >= 0, name = "nonzero_constraint_14")
problemThree.addConstr(DD >= 0, name = "nonzero_constraint_15")
problemThree.addConstr(DC >= 0, name = "nonzero_constraint_16")

#Solution to be optimized
Z = 210*AR + 90*AA + 180*AD + 160*AC + 100*BR + 70*BA + 130*BD + 200*BC + 175*CR + 105*CA + 140*CD + 170*CC + 80*DR + 65*DA + 105*DD + 120*DC

#Setting solution to be minimized
problemThree.setObjective(Z, GRB.MINIMIZE)

#Solution getting optimized
problemThree.optimize()

#Part D) Prints total number of miles traveled for teams of officials to reach all games (Minimized optimal solution)
objective_value= problemThree.objVal
if problemThree.status == GRB.OPTIMAL:
    print("Optimal value and total number of miles traveled is --->", objective_value)

#Part C) Prints optimal assignment of teams of officials to games
problemThree.printAttr ('X')