import re
import os.path

# user chooses whether to "type" sum or "load" file
print("type - to type in the sum")
print("load - to load the sums from a text file")
entry_choice = input("Enter either 'type' or 'load' from the menu above to proceed:")

# if "type" get input off user
if entry_choice == "type":
    with open("results.txt", "a") as f:
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

        if not (operator == "+" or operator == "-" or operator == "*" or operator == "/"):
             operator = "error"

        #If no string named "error", do the calculation, otherwise print "Invalid input"
        if number_1 !="error" and number_2 !="error" and operator !="error":

            formatted_plus = f"{number_1} + {number_2} = {number_1+number_2}\n"
            formatted_minus = f"{number_1} - {number_2} = {number_1-number_2}\n"
            formatted_multiply = f"{number_1} * {number_2} = {number_1*number_2}\n"
            divide_by_zero = "Division by zero\n"
            divide = f"{number_1} / {number_2} = {number_1/number_2}\n"
            error = "Invalid input\n"

            if operator == "+":
                f.write(formatted_plus)
                print (formatted_plus)
            elif operator == "-":
                f.write(formatted_minus)
                print (formatted_minus)
            elif operator == "*":
                f.write(formatted_multiply)
                print (formatted_multiply)
            elif number_2 ==0 and operator == "/":
                f.write(divide_by_zero)
                print (divide_by_zero)
            elif operator == "/":
                f.write(divide)
                print (divide)
                
            print("Sum(s) successfully appended to results.txt")

        else:
            print ("Invalid input\n")
            
#if user chooses "load", open file if valid
elif entry_choice == "load":
    print("Please make sure the text file contains one sum with one operator per line, e.g. \"1+1\".")
    filename = input("What is your filename?  (Please include extension.):")
    if os.path.isfile(filename):
        with open("sums.txt", "r") as a_file, open("results.txt", "a") as f:
            for line in a_file:  
                if line != "\n":

                    # strip spaces and "=" 
                    line = line.replace("=","").replace(" ","").replace("\n","")


                    #find type of operator, making sure there's only one if not "-"
                    if line.count("+") == 1 and line.count("*") == 0 and line.count("/") == 0:
                            operator = "+"
                    elif line.count("*") == 1 and line.count("+") == 0 and line.count("/") == 0:
                            operator = "*"
                    elif line.count("/") == 1 and line.count("+") == 0 and line.count("*") == 0:
                            operator = "/"    
                    elif "-" in line and line.count("+") == 0 and line.count("*") == 0 and line.count("/") == 0:
                            operator = "minus"   
                    else:
                            operator = "error"

                    #turn "-" operator into word "minus" to disambiguate from negative numbers
                    if operator == "minus" and line.count("-") == 3:
                        line = re.sub(r"(.*)-(.*)-(.*)-(.*)", r"\1-\2minus\3-\4", line)
                    elif operator == "minus" and line.count("-") == 2 and line[0]=="-":
                        line = re.sub(r"(.*)-(.*)-(.*)", r"\1-\2minus\3", line)
                    elif operator == "minus" and line.count("-") == 2 and line[0]!="-":
                        line = re.sub(r"(.*)-(.*)-(.*)", r"\1minus\2-\3", line)

                    #check for illegal characters
                    checked_line = [x if re.match('^[0-9.-]+$', x) else "error" for x  in line.split(operator)]

                    #check there are two operators
                    if len(checked_line) != 2:
                        checked_line = ["error","error"]

                    #try to turn into floats to check valid numbers
                    try:
                        number_1 = float(checked_line[0])
                        number_2 = float(checked_line[1])
                    except:
                        number_1 = "error"
                        number_2 = "error"

                    #do the sum
                    if number_1 !="error" and number_2 !="error" and operator !="error":

                        formatted_plus = f"{number_1} + {number_2} = {number_1+number_2}\n"
                        formatted_minus = f"{number_1} - {number_2} = {number_1-number_2}\n"
                        formatted_multiply = f"{number_1} * {number_2} = {number_1*number_2}\n"
                        divide_by_zero = "Division by zero\n"
                        divide = f"{number_1} / {number_2} = {number_1/number_2}\n"
                        error = "Invalid input\n" 

                        if operator == "+":
                            result = (formatted_plus)
                            print (formatted_plus)
                        elif operator == "minus":
                            result = (formatted_minus)
                            print (formatted_minus)
                        elif operator == "*":
                            result = (formatted_multiply)
                            print (formatted_multiply)
                        elif operator == "/" and number_2 == 0:
                            result = (divide_by_zero)
                            print (divide_by_zero)
                        elif operator == "/":
                            result = (divide)
                            print (divide)

                        #write to the file
                        f.write("\n"+str(result))
                    else:
                        print ("Invalid input\n")
                        f.write("Invalid input\n")
        

            print("Sum(s) successfully appended to results.txt")
 
    else:
        print("File does not exist")

else:
    print("You did not type \"type\" or \"load\"")


