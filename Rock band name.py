#Enter your first name and your pet's name and the program will provide a name for your rock band.

def get_band_name(first_name, pet_name):
    band_name_part_1 = first_name[:5]
    band_name_part_2 = pet_name[:5]
    return band_name_part_1 + band_name_part_2

try:
    first_name = input('Enter your first name ')
    pet_name = input('Enter your pet name: ')
    print(f'So your first name is {first_name} and the name of your pet is {pet_name}.')
    band_name_final = get_band_name(first_name, pet_name)
    print(f'So your band name is {band_name_final}')
except NameError as e:
    print('That is not a valid name!', e)
