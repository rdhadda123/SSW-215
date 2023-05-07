from gurobipy import *

def problem_one(constr_one, constr_two, constr_three):
    problemOne = Model("problemOne")

    #Variables representing x1 and x2, x = x1, y = x2
    x = problemOne.addVar(vtype = GRB.INTEGER, name = "var1")
    y = problemOne.addVar(vtype = GRB.INTEGER, name = "var2")

    #Constraints as listed in the model, each constraint value gets passed into the function
    problemOne.addConstr(x + 2*y >= constr_one, name = "constraint_one")
    problemOne.addConstr(2*x - 3*y <= constr_two, name = "constraint_two")
    problemOne.addConstr(x + y >= constr_three, name = "constraint_three")

    #Constraints to make sure each variable is not less than 0
    problemOne.addConstr(x >= 0, name = "nonzero_constraint_one")
    problemOne.addConstr(y >= 0, name = "nonzero_constraint_two")

    #Function that needs to be optimized
    Z = 15*x + 20*y

    #Setting objective to maximize
    problemOne.setObjective(Z, GRB.MAXIMIZE)

    #Optimizes function
    problemOne.optimize()

    #Printing out results for decision variables and objective function
    objective_value= problemOne.objVal
    if problemOne.status == GRB.OPTIMAL:
        print("Optimal value is --->", objective_value)

    problemOne.printAttr ('X') 
    x1 = x.X
    x2 = y.X
    print ("# of x1 --->", x1)
    print ("# of x2 --->", x2)
        
    return x1, x2, objective_value

 #Call to function
var1, var2, obj_val = problem_one(10, 6, 6)

print("The result is --->", var1, var2, obj_val)
