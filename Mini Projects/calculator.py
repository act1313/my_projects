#Calculator
import math

print("Welcome to the calculator.")

def sequence():
    Math = input("Would you like to multiply(m), divide(d), add(a), subtract(s), exponent(e), get  the square root of number(sr), geometry(g), or get the remainder to a division problem(r)? ")

    if Math == "m":
        mnum1 = float(input("What is the first number would you like to multiply? "))
        mnum2 = float(input("What is the second number would you like to multiply? "))
        print(mnum1 * mnum2)

    elif Math == "d":
        dnum1 = float(input("What is the first number would you like to divide? "))
        dnum2 = float(input("What is the first number would you like to divide? "))
        print(dnum1 / dnum2)

    elif Math == "a":
        anum1 = float(input("What is the first number would you like to add? "))
        anum2 = float(input("What is the second number would you like to add? "))
        print(anum1 + anum2)

    elif Math == "s":
        snum1 = float(input("What is the first number would you like to subtract? "))
        snum2 = float(input("What is the second number would you like to subtract? "))
        print(snum1 - snum2)

    elif Math == "e":
        enum1 = float(input("What would you like the base number to be? "))
        enum2 = float(input("What would you like the exponent to be? "))
        print(enum1 ** enum2)

    elif Math == "sr":
        srnum = float(input("What number would you like the square root of? "))
        print(math.sqrt(srnum))

    elif Math == "r":
        rnum1 = float(input("What is the first number you would like to divide? "))
        rnum2 = float(input("What is the second number you would like to divide? "))
        print(rnum1 % rnum2)

    elif Math == "g":
        t = input("What type of geometry would you like to do? (volume(v), surface area(sa)")
        if t == "v":
            v = input("What 3D shape's volume would you like to calculate? (square/rectangle(s), triangle(t)")
            if v == "s":
                svnum1 = float(input("What is the length of your rectangular prism? "))
                svnum2 = float(input("What is the width of your rectangular prism? "))
                svnum3 = float(input("What is the height of your rectangular prism? "))
                print(svnum1 * svnum2 * svnum3)
            elif v == "t":
                tbnum1 = float(input("What is the base of the triangle face of the triangular prism? "))
                tbnum2 = float(input("What is the height of the triangle of the triangular prism? "))
                th = float(input("What is the height of the triangular prism? "))
                vtri = 0.5 * tbnum1 * tbnum2
                print(vtri * th)
            else:
                print("Incorrect Syntax")

        else:
            print("Incorrect Syntax")

    else:
        print("Incorrect Syntax!!!")

    question = input("Would you like to make anymore calculations? [y/n] ")

    if question == "y":
        sequence()

    elif question == "n":
        print("Goodbye!!!")

    else:
        print("Goodbye!!!")

sequence()
