#Fahrenheit To Celcius

def converter():
    f = int(input("What degrees fahrenheit would you like to covert to celcius? "))
    c1 = f - 32
    c2 = c1 * 5/9

    print(c2, "°C")

    y_n = input("Would you like to convert again? [Y/N] ")

    if y_n == "Y":
        converter()

    elif y_n == "N":
        print("Goodbye")

    else:
        print("Incorrect Syntax")

converter()
