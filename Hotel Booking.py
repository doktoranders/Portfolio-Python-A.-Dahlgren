class Booking:
    def __init__(self):
        self.hotel_dict = {}

    def unbook(self, customer_id: int):
        """Cancel a booking."""
        flag = input('Are you sure you want to cancel? ')
        if flag.lower() == 'y':
            if customer_id in self.hotel_dict:
                print('Ok, we will cancel your booking.')
                additional_wishes = input('Do you have any additional wishes? ')
                if additional_wishes == 'y':
                    additional_wishes = input('What are your additional wishes? ')
                    print(f'Perfect! We will fix {additional_wishes} for you.')
                self.hotel_dict[customer_id]['additional_wishes'] = additional_wishes
                del self.hotel_dict[customer_id]
            else:
                print('You have no booking to cancel.')

    def get_special_wishes(self):
        """Get special wishes from the user."""
        name = input('I see that you brought your wife. What is her name?: ')
        wishes = input(f'What special wishes do you have for {name}? ')
        print(f'We will make sure {name} gets {wishes}.')
        return name, wishes

    def get_next_customer_id(self) -> int:
        """Get the next customer ID."""
        if self.hotel_dict:
            return max(self.hotel_dict.keys()) + 1
        else:
            return 1

    def get_booking_info(self) -> dict: 
        """Get booking information from the user."""
        name = input('What is your name?: ')
        number_of_rooms = int(input('How many rooms do you want? '))
        number_of_beds = int(input('How many beds do you need? '))
        number_of_guests = int(input('How many are you? '))
        additional_wishes = input('Do you have any additional wishes (y / n)? ')
        if additional_wishes.lower() == 'y':
            additional_wishes = input('What are your additional wishes? ')
            print(f'Perfect! We will fix {additional_wishes} for you.')
        return {
            "name": name,
            "number_of_rooms": number_of_rooms,
            "number_of_beds": number_of_beds,
            "number_of_guests": number_of_guests,
            "wishes": additional_wishes

        }

    def customer_data(self) -> dict: 
        booking_info = self.get_booking_info()
        customer_id = self.get_next_customer_id()
        return customer_id, booking_info

    def check_in(self, customer_id: int, customer_data: dict):
        """Check a customer into the hotel."""
        self.hotel_dict[customer_id] = customer_data
        print(f'Customer {customer_id} is now checked in.')

    def main(self):
        customer_id, customer_data = self.customer_data()
        print(f"customer_id: {customer_id}")
        print(f"customer_data: {customer_data}")
        self.check_in(customer_id, customer_data)
        self.get_special_wishes()
        booking_marker = input('Would you like to cancel your booking? (y / n): ')
        if booking_marker.lower() == 'y':
            self.unbook(customer_id)
            print(self.hotel_dict)

if __name__ == "__main__":
    Bookings = Booking()
    while True:
        Bookings.main()
