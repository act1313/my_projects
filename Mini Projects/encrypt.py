from random import randint

ALPHABET = "abcdefghijklmnopqrstuvwsyz"

def generate_otp(sheets, length):
    for sheet in range(sheets):
        with open("otp" + str(sheet) + ".txt","w") as f:
            for i in range(length):
                f.write(str(randint(0,26))+"\n")
def load_sheet(filename):
    with open(filename, "r") as f:
        contents = f.read().splitlines()
    return contents
def get_plain_text():
    plain_text = input('Please Type Your Message: ')
    return plain_text.lower()
def load_file(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents
def save_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)
def encrypt(plaintext, sheet):
    ciphertext = ''
    for position, character in enumerate(plaintext):
        if character not in ALPHABET:
            ciphertext += character
        else:
            encrypted = (ALPHABET.index(character) + int(sheet[position])) % 26
            ciphertext += ALPHABET[encrypted]
    return ciphertex
generate_otp(5,100)

sheet = load_sheet('otp0.txt')
encrypt("This is a secret message.", sheet)
