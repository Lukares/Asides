class Conversion:
    
    # Code created by Luke Reddick
    # Please use inputs of one character, so C, F, K, c, f ,k 
    # for celsius, fahrenheit, and Kelvin respectively

     
    convertFrom = str((input("What temperature are you converting from? (C/F/K) : " + "\n")))
    convertTo = str((input("What temperature would you like to convert to? (C/F/K) : " + "\n")))
    try:
        valueTemp = float((input(("What is the value of your temperature you would like to convert? : " + "\n"))))
    except:
        print("Your input was invalid.")

    def convert(w, s, x):
        if s == "F" or s == "f":
            if w == "C" or w == "c":
                result = (x - 32) * (5/9)
                print(str(x) + " degrees Fahrenheit is \n" + str(round(result, 3)) + " degrees Celsius \n")
            elif w == "K" or w == "k":
                result = (x - 32) * (5/9) + 273.15
                print(str(x) + " degrees Fahrenheit is \n" + str(round(result, 3)) + " degrees Kelvin \n")
            else:
                print("Your input did not make sense to the program, try again.")
        elif s == "C" or s == "c":
            if w == "F" or w == "f":
                result = (x * (9/5)) + 32
                print(str(x) + " degrees Celsius is \n" + str(round(result, 3)) + " degrees Fahrenheit \n")
            elif w == "K" or w == "k":
                result = x + 273.15
                print(str(x) + " degrees Celsius is \n" + str(round(result, 3)) + " degrees Kelvin \n")
            else:
                print("Your input did not make sense to the program, try again.")
        elif s == "K" or s == "k":
            if w == "F" or w == "f":
                result = (x - 273.15 - 32) * (5/9)
                print(str(x) + " degrees Kelvin is \n" + str(round(result, 3)) + " degrees Fahrenheit \n")
            elif w == "C" or w == "c":
                result = x - 273.15
                print(str(x) + " degrees Kelvin is \n" + str(round(result, 3)) + " degrees Celsius \n")
            else:
                print("Your input did not make sense to the program, try again. \n")    
        else:
            print("Your input did not make sense to the program, try again. \n")

    try:          
        convert(convertTo, convertFrom, valueTemp)
    except:
        print("Since input was invalid... \n Use single characters for the first two inputs and digits for the third. \n")
    
    input(" \nPress enter to exit.")
