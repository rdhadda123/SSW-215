from gurobipy import *

problemTwo = Model("problemTwo")

#Parts A and B)
#Continuous decision variables for the amount of sugar beets in each kibbutz
x1 = problemTwo.addVar(vtype = GRB.CONTINUOUS, name = "Kibbutz1_Sugarbeets")
x2 = problemTwo.addVar(vtype = GRB.CONTINUOUS, name = "Kibbutz2_Sugarbeets")
x3 = problemTwo.addVar(vtype = GRB.CONTINUOUS, name = "Kibbutz3_Sugarbeets")

# Continuous decision variables for the amount of cotton in each kibbutz
x4 = problemTwo.addVar(vtype = GRB.CONTINUOUS, name = "Kibbutz1_Cotton")
x5 = problemTwo.addVar(vtype = GRB.CONTINUOUS, name = "Kibbutz2_Cotton")
x6 = problemTwo.addVar(vtype = GRB.CONTINUOUS, name = "Kibbutz3_Cotton")

# Continuous decision variables for the amount of sorghum in each kibbutz
x7 = problemTwo.addVar(vtype = GRB.CONTINUOUS, name = "Kibbutz1_Sorghum")
x8 = problemTwo.addVar(vtype = GRB.CONTINUOUS, name = "Kibbutz2_Sorghum")
x9 = problemTwo.addVar(vtype = GRB.CONTINUOUS, name = "Kibbutz3_Sorghum")
#End of parts A and B

#Constraints for usable land
problemTwo.addConstr(x1 + x4 + x7 <= 400, name = "land_constraint_one")
problemTwo.addConstr(x2 + x5 + x8 <= 600, name = "land_constraint_two")
problemTwo.addConstr(x3 + x6 + x9 <= 300, name = "land_constraint_three")

#Constraints for water allocation
problemTwo.addConstr(3*x1 + 2*x4 + x7 <= 600, name = "water_constraint_one")
problemTwo.addConstr(3*x2 + 2*x5 + x8 <= 800, name = "water_constraint_two")
problemTwo.addConstr(3*x3 + 2*x6 + x9 <= 375, name = "water_constraint_three")

#Constraints for total acreage
problemTwo.addConstr(x1 + x2 + x3 <= 600, name = "acre_constraint_one")
problemTwo.addConstr(x4 + x5 + x6 <= 500, name = "acre_constraint_two")
problemTwo.addConstr(x7 + x8 + x9 <= 320, name = "acre_constraint_three")

#Constraints for equal propertion of land
problemTwo.addConstr((3*(x1 + x4 + x7) - 2*(x2 + x5 + x8)) == 0, name = "equalland_constraint_one")
problemTwo.addConstr(((x2 + x5 + x8) - 2*(x3 + x6 + x9)) == 0, name = "equalland_constraint_two")
problemTwo.addConstr((4*(x3 + x6 + x9) - 3*(x1 + x4 + x7)) == 0, name = "equalland_constraint_three")

#Non-zero constraints
problemTwo.addConstr(x1 >= 0, name = "nonzero_constraint_1")
problemTwo.addConstr(x2 >= 0, name = "nonzero_constraint_2")
problemTwo.addConstr(x3 >= 0, name = "nonzero_constraint_3")
problemTwo.addConstr(x4 >= 0, name = "nonzero_constraint_4")
problemTwo.addConstr(x5 >= 0, name = "nonzero_constraint_5")
problemTwo.addConstr(x6 >= 0, name = "nonzero_constraint_6")
problemTwo.addConstr(x7 >= 0, name = "nonzero_constraint_7")
problemTwo.addConstr(x8 >= 0, name = "nonzero_constraint_8")
problemTwo.addConstr(x9 >= 0, name = "nonzero_constraint_9")

#Solution to be optimized
Z = 1000*(x1 + x2 + x3) + 750*(x4 + x5 + x6) + 250*(x7 + x8 + x9)

#Setting solution to be maximized
problemTwo.setObjective(Z, GRB.MAXIMIZE)

#Optimizes solution
problemTwo.optimize()

#Part C) Finds optimal solution and prints it
objective_value= problemTwo.objVal
if problemTwo.status == GRB.OPTIMAL:
    print("Optimal value is ---> $", round(objective_value, 2))

problemTwo.printAttr ('X')
