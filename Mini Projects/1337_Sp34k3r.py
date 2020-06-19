SUBSTITUTIONS = [['e','3'],['a','4'],['l','1'],['o','0'],['t','7']]

def encode_message(message, substitutions):

    for s in substitutions:
        old = s[0]
        new = s[1]
        message = message.replace(old,new)

        print("converted text = " + message)


message = input("What would you like to convert to hacker speak? ")
converted_text = encode_message(message, SUBSTITUTIONS)

print('original text = ' +  message)
