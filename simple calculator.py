number_1 = (input("Please enter number 1: "))
number_2 = (input("Please enter number 2: "))
operator = (input("Please enter operator (+ or - or * or /): "))

#If number_1 user entry is valid, turn string into float, otherwise rename string "error".
try:
    float(number_1)
    number_1 = float(number_1)
except ValueError:
    number_1 = "error"

#If number_2 user entry is valid, turn string into float, otherwise rename string "error".
try:
    float(number_2)
    number_2 = float(number_2)
except ValueError:
    number_2 ="error"

#If no string named "error", do the calculation, otherise print "Invalid input"
with open("results.txt", "a") as f:
    if number_1 != "error" and number_2 != "error" and (operator == "+" or operator == "-" or operator == "*" or operator == "/"):
        if operator == "+":
            print (f"{number_1} + {number_2} = {number_1+number_2}\n")
            f.write(f"{number_1} + {number_2} = {number_1+number_2}\n")
        elif operator == "-":
            print (f"{number_1} - {number_2} = {number_1-number_2}\n")
            f.write(f"{number_1} - {number_2} = {number_1-number_2}\n")
        elif operator == "*":
            print (f"{number_1} * {number_2} = {number_1*number_2}\n")
            f.write(f"{number_1} * {number_2} = {number_1*number_2}\n")
        elif number_2 ==0 and operator == "/":
            print ("Division by zero\n")
            f.write("Division by zero\n")
        elif operator == "/":
            print (f"{number_1} / {number_2} = {number_1/number_2}\n")
            f.write(f"{number_1} / {number_2} = {number_1/number_2}\n")

        print("Sum(s) successfully appended to results.txt")

    else:
        print("Invalid input\n")
        

