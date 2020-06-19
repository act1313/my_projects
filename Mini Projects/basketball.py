#Basketball Shot Calculator

def calculator():
    type_of_shot = input("Would you like to calculate two pointers, three pointers, free throws, or field goals?")

    if type_of_shot == "two pointers":
        shots_made = int(input("How many two point shots did you make:"))
        shots_taken = int(input("How many two point shots did you take:"))
        percentage = float(shots_made / shots_taken * 100)
        print("%", percentage)

    elif type_of_shot == "three-pointers":
        shots_made = int(input("How many three point shots did you make:"))
        shots_taken = int(input("How many three point shots did you take:"))
        percentage = float(shots_made / shots_taken * 100)
        print("%", percentage)

    elif type_of_shot == "free throws":
        shots_made = int(input("How many free throws did you make:"))
        shots_taken = int(input("How many free throws did you take:"))
        percentage = float(shots_made / shots_taken * 100)
        print("%", percentage)

    elif type_of_shot == "field goals":
        shots_made = int(input("How many field goals did you make:"))
        shots_taken = int(input("How many field goals did you take:"))
        percentage = float(shots_made / shots_taken * 100)
        print("%", percentage)

    else:
        print("Incorrect Syntax XD")
        y_n = input("Would you like to try again")
        if y_n == "y":
            calculator()
        elif y_n == "n":
            print("Goodbye!!!")
        else:
            print("Incorrect Syntax")

calculator()
