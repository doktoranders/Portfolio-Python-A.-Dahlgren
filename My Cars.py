import json


class Car:
    def __init__(self):
        self.car_info = {
            'Owner': input("Enter the name of the owner: "),
            'Brand': input("Enter the brand: "),
            'Model': input("Enter the model: "),
            'Color': input("Enter the color: "),
            'Horsepower': int(input("Enter the number of horsepower: ")),
            'Year': int(input("Enter the production year: ")),
            'Number_of_owners': int(input("Enter the number of owners: ")),
            'Distance_in_km': float(input("Enter the distance in km: ")),
            'Asking_price': float(input("Enter the asking price: "))
        }

def save_car_data(filename, cars):
    with open(filename, 'w') as file:
        json.dump([car.car_info for car in cars], file)

def load_car_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def print_car_details(cars):
    for car in cars:
        print('Car Details:')
        for key, value in car.car_info.items():
            print(f'{key}: {value}')
        print()

cars = []
while True:
    if input('Do you want to enter car data? (y / n) ').lower() == 'y':
        cars.append(Car())
        print_car_details(cars)
    else:
        break

