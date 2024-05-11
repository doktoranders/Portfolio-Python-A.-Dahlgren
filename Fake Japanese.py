import random

def random_answer(random_output):
    if random_output == 0:
        return '-'
    elif random_output == 1:
        return '|'
    elif random_output == 2:
        return '_'
    elif random_output == 3:
        return '/'
    elif random_output == 4:
        return '//'
    elif random_output == 5:
        return '\\'

random_output = random.randint(0, 6)  # Generate a random integer between 0 and 6
while random_output != 6:
    output = random_answer(random_output)
    print(output, end='')
    random_output = random.randint(0, 6)
