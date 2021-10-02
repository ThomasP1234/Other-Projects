import random

while True:
    length = int(input('How many characters long for your password. '))
    password = ""

    for i in range(length):
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        characters = str(characters)
        password += characters[random.randint(0, len(characters)-1)]

    print(f'Your password is: {password}')
    while True:
        again = input('Do you want to generate another? [y/n] ')
        if again == 'y':
            break
        elif again == 'n':
            exit()
        else:
            print('Enter either y or n')