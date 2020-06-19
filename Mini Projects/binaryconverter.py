#Binary Converter

SUBSTITUTIONS = [['0','00110000'],['1','00110001'],['2','00110010'],['3','00110011'],['4','00110100'],['5','00110101'],['6','00110110'],['7','00110111'],['8','00111000'],['9','00111001'],['a','01100001'],['b','01100010'],['c','01100011'],['d','01100100'],['e','01100101'],['f','01100110'],['g','01100111'],['h','01101000'],['i','01101001'],['j','01101010'],['k','01101011'],['l','01101100'],['m','01101101'],['n','01101110'],['o','01101111'],['p','01110000'],['q','01110001'],['r','01110010'],['s','01110011'],['t','01110100'],['u','01110101'],['v','01110110'],['w','01110111'],['x','01111000'],['y','01111001'],['z','01111010']]


def encode_string(message, substitutions):

    for s in  substitutions:
        old = s[0]
        new = s[1]
        message = message.replace(old,new)

        print(message + " ")


print("Welcome to the binary converter!!!")

na = input("Whould you like to convert a number or a word? ")


if na == "number":
    message = input("What number would you like to convert to binary? ")
    print("Calculating")
    binary = encode_string(message, SUBSTITUTIONS)
    print(binary)

elif na == "word":
    message = input("What word would you like to convert to binary? ")
    print("Calculating")
    binary = encode_string(message, SUBSTITUTIONS)
    print(binary)

else:
    print("Incorrect Syntax")
