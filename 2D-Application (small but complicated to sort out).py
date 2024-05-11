line1 = [' ', ' ', ' ']
line2 = [' ', ' ', ' ']
line3 = [' ', ' ', ' ']

lines = {'A': line1, 'B': line2, 'C': line3}

spot = input("Enter the spot where you want to place your X: (e.g. A1, B2, C3, etc.) ")
spot_letter = spot[0]
spot_number = int(spot[1]) - 1  # Subtract 1 to make the numbers right!

lines[spot_letter][spot_number] = 'X'

print(lines['A'])
print(lines['B'])
print(lines['C'])