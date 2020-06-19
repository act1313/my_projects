import random

chars = 'abcdefghijklmnopqrstuvwsyz1234567890.?!@#$%&*ABCDEFGHIJKLMNOPQRSTUVWXYZ'

num = input("Number of Passwords?: ")
num = int(num)
length = input('Password Length?: ')
length = int(length)

for p in range(3):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
