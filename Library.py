from datetime import datetime, timedelta
from random import randint

books = ['Gladiator', 'The Godfather', 'The Notebook', 'The Da Vinci Code', 'The Kite Runner', 'The Little Prince', 'The Alchemist', 
        'The Twilight Saga', 'Harry Potter', 'Lord of the Rings', 'The Secret']
amazon_books = ["Harry Potter", "Lord of the Rings", "The Alchemist", "The Da Vinci Code", "The Godfather", "The Kite Runner", 
                "The Little Prince", "The Notebook", "The Secret", "The Twilight Saga"]

def due_date_generator():
    today_date = datetime.now()
    due_date = today_date + timedelta(days = randint(15, 30))  
    return due_date

def check_availability(title):
    if title in books:
        return True
    else:
        return False

def order_book(title):
    if title in amazon_books:
        return 'Yes, we have that book! It will be delivered in 2 days.'
    else:
        return 'Sorry, but we do not have that book in our inventory.'    

def check_due_date(book_due_date):
    today_date = datetime.now()
    if today_date > book_due_date:
        return True
    else:
        return False

def return_books(title, book_due_date):
    if check_due_date(book_due_date):
        print('You will have to pay a fine of $5.00')
    else:
        print('Thank you for returning your books on time!')

def library_presentation():
    print('''This library has a collection of 11 books. The books are: Gladiator, The Godfather, The Notebook, 
          The Da Vinci Code, The Kite Runner, The Little Prince, The Alchemist, The Twilight Saga, Harry Potter, 
          Lord of the Rings, The Secret.''')

def borrow_books(title):
    if check_availability(title):
        book_due_date = due_date_generator()
        print(f'You have borrowed {title}. It is due on {book_due_date.strftime("%m / %d / %Y")}.')
        books.remove(title)
        return book_due_date
    else:
        print("Sorry, but we don't have that book!")
        return None

question = input('Do you want to know a little about this library? (y / n) ')
if question == 'y':
    library_presentation()
else:
    print('Ok, no problem!')

borrow_book = input('Do you want to borrow a book? (y / n) ')
if borrow_book == 'y':
    title = input('What is the title of the book? ')
    due_date = borrow_books(title)

buy_book = input('Or maybe you want to buy a book also? (y / n) ')
if buy_book == 'y':
    title = input('What is the title of the book? ')
    if check_availability(title):
        print('Yes, we have that book!')
    else:
        book_answer = input('Sorry, but we do not have that book in our inventory, but we can order it for you! (y / n) ')
        if book_answer == 'y':
            print(order_book(title))
        else:
            print('Ok, no problem!')

if due_date:
    return_books(title, due_date)