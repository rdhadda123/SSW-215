#Rishabh Dhadda
#Assignment 7
#SSW-215

import numpy.random
import numpy as np
import numpy.linalg as LA
import pandas as pd
import matplotlib.pyplot as plt

problem = (int)(input("What problem do you want to solve(1-3): "))

if problem == 1:
    #Creating two matrices that hold random numbers
    A = np.random.randint(50, 120, (3,5))
    B = np.random.randint(10, 60, (5,6))

    #Creating matrix C which is product of A and B
    C = np.dot(A,B)

    #Creating matrix R which is product of C multiplied by 10
    R = np.dot(C, 10)

    print(A)
    print(B)
    print(C)
    print(R)

elif problem == 2:
    #Values for variable coefficients
    X = np.array([[4, -8, -2, 7], [-4, 1, -9, -4], [-2, -64, -6, 5], [-7, -8, -25, -2]])

    #Values for sum 
    Y = np.array([9, -5, 5, 2])

    #Variable to solve system of equations
    Z = LA.solve(X,Y)

    print(Z)

elif problem == 3:
    # Reads data from text file and puts it into four categories
    df1 = pd.read_csv('salary.txt', ' ', names= ["Employee", "Salary", "Year", "Gender"])
    print(df1)
    print()

    #Creates subset of all rows in Employee and Salary heading
    print(df1.iloc[:, [0,1]])
    
    #Groups all data by gender and then uses describe() function to get max, standard deviation, and mean for salaries
    grouped = df1.groupby('Gender')
    print()
    print(grouped.describe())

    #Plots salary against year
    df1.plot.scatter(x = "Year", y = "Salary")
    plt.show()
    
else:
    print("The number is invalid. Choose from 1-3")