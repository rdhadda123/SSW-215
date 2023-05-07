#Choose problem that needs to be solved
problem = int(input("What problem do you want to solve (1,2,3): "))

#Problem 1
if (problem == 1):
    terms = int(input("How many terms do you want: "))
    first = 0
    second = 1
    sum = 0
    count = 0
    if terms <= 0:
        print("Wrong input, enter positive integer")

    elif terms == 1:
        print("Fibonacci sequence for", terms, "terms is: ")
        print(first)

    else:
        print("Fibonacci sequence for", terms, "terms is: ")
        while count < terms:
            print(first)
            sum = first + second
            first = second
            second = sum
            count += 1

#Problem 2
if (problem == 2):
    myDict = {"A": 10, "B": 11, "C": 7, "D" : 15, "E" : 1, "F": 13}
    print("The Prime number keys are: ")
    for key in myDict.keys():
        if (myDict[key] > 1):
            for num in range(2, myDict[key] - 1):
                if (myDict[key] % num == 0):
                    break
            else:
                print(key)

#Problem 3
def expo(base, power):
        total = 1
        if power < 0:
            print("Power has to be non-negative")
            total = 0
        
        elif power == 0:
            total = 1

        else:
            for x in range(power):
                total *= base

        return total 
        
if (problem == 3):         
    base = int(input("What is the base: "))
    power = int(input("What is the power: "))
    print("The final product is", expo(base,power))   
     
    
                    
                
