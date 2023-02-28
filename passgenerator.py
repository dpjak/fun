# password generator

import random

passSymbols = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'F',
               'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' '1',
               '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*']
# list of characters

password = (''.join(passSymbols))
#  turns list in to array of strings

print('Hello there, this is password generator')
print('=' * 100)

while True:
    passlen = input('how many character you want your password to be:'.capitalize())
    try:        # checks if passlen is a numeric number
        passlen = int(passlen)
    except:
        print('Only numeric digits are allowed')
        continue
    if passlen < 8:     # check password length stands in criteria
        print('Your password should be at least 8 digits')
        continue
    break
# asks for amount of characters that the password will contain

passgen = random.choices(password, k=passlen)
#  randomizes the choice of characters, number of times was indicated in pass length
print('=' * 50)
print('your new password is: ' + ''.join(passgen))  # print the resulted password
print('=' * 50)
with open('generated_passwords', 'w') as the_file:  # writes the password to a txt file
    the_file.write('\nyour new password is: ' + ''.join(passgen))
