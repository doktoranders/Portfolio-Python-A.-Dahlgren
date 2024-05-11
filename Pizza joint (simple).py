print('Do you want a small, medium or large pizza? ')
size = input()
if size == 'small':
      price = 15
elif size == 'medium':
      price = 30
elif size == 'large':
      price = 45
pepperoni = input('Do you want pepperoni? ')
if pepperoni == 'yes':
    if size == 'small' or size == 'medium':  # Fixed the condition
        price += 2  # Initialized the price variable before the if-elif statements
    else:
        price += 3
cheese = input('Do you want extra cheese? ')
if cheese == 'yes':
    price += 1
print(f'Your final bill is: {price}')