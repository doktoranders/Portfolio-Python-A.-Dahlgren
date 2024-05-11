import random
going_forward = 'enter'
while going_forward != 'exit':
    i = 1
    password = ''
    length = int(input('Enter the length of the password: '))
    while i <= length:
        choice = random.randint(1, 4)
        if choice == 1:
            lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
            low_lett = random.choice(lowercase_letters)
            password += low_lett
            
        elif choice == 2:
            uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            up_lett = random.choice(uppercase_letters)
            password += up_lett
            
        elif choice == 3:
            digits = '0123456789'
            digit = random.choice(digits)
            password += digit
            
        elif choice == 4:
            special_characters = '!@#$%^&*()_+'
            special_char = random.choice(special_characters)
            password += special_char
        i += 1
    print(password)
    going_forward = input('Press "exit" to exit: ')
    if going_forward == 'exit':
        break