#Random Number Generator

from random import randint

print("Welcome to Random Number Generator!!!")

def generate():
    range_beg = int(input("What is the first number of your range(e.g. 2-10; 2)? "))
    range_end = int(input("What is the second number of your range(e.g. 2-10; 10)? "))

    print(randint(range_beg,range_end))

    y_n = input("Would you like to do it again (Y/N)? ")
    if y_n == "Y":
        generate()

    elif y_n == "N":
        print("Goodbye")
    else:
        print("Incorrect Syntax")


generate()
