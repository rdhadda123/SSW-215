from cmath import pi


problem = int(input("What problem do you want to do?: "))

if (problem == 1):
    radius = float(input("what is the radius: "))

    area = pi * (radius ** 2)
    print("The area is", area)

elif (problem == 2):
    edge = int(input("what is the edge: "))
    surfaceArea = 6 * edge ** 2

    print("The surface area is:", surfaceArea)

elif (problem == 3):
    new = int(input("what is the number of new: "))
    oldies = int(input("what is the number of old: "))

    total = (new * 3.00) + (oldies * 2.00)

    print("The total is $", total)
