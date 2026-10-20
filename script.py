''' Practice code 1 = Employee Class and increase salary by 10%'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):
        percent = 10
        new_sal = self.salary * percent / 100
        self.salary += new_sal

employee1 = Employee("Rohan", 10000)
employee1.increase_salary(10)
print(employee1.salary)
print("----------------------------------------------------------------------------------------")

''' Practice code 2 = Book Class with borrow and return functionality '''

class Book:
    def __init__(self, title, author, available= True):
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            print("Book borrowed successfully.")
        else:
            print("Book is already borrowed.")

    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned successfully.")
        else:
            print("Book is already in the library.")

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Available:", self.available)


book1 = Book("1984", "George Orwell", True)
book2 = Book("To Kill a Mockingbird", "Harper Lee", True)
book3 = Book("Pride and Prejudice", "Jane Austen", True)
book4 = Book("The Great Gatsby", "F. Scott Fitzgerald", False)
book5 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", False)

book1.display()
book1.borrow()
book1.return_book()

print("-------------------------------------------------------------------------------------------------------")

''' Practice code 3 = Shopping Cart Class with add items, remove items and total price calculation '''

class ShoppingCart:
    def __init__(self):
        self.items = []


    def add_items(self, name, price):
        self.items.append((name, price))
        print("Item added")

    def remove_items(self, name):
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)
                print("Item removed")
                return
        print("Item not found")

    def show_cart(self):
        for item in self.items:
            print(item[0], "-" ,item[1])

    def total_price(self):
        return sum(price for _, price in self.items)

cart = ShoppingCart()

cart.add_items("Apple", 100)
cart.add_items("Orange", 200)
cart.add_items("Banana", 50)
cart.add_items("Grape", 145)

cart.remove_items("Apple")

cart.show_cart()
print("$",cart.total_price())

print("-------------------------------------------------------------------------------------------------------")

''' Practice code 4 = Food ordering system add items, and total price calculation '''

class FoodItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_details(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)

    def apply_discount(self):
        percent = 10
        discount = self.price * percent / 100
        self.price -= discount


class ComboMeal(FoodItem):
    def __init__(self, name, price, category):
        super().__init__(name, price, category)
        self.combo_items = ["Aloo Wrap", "Pepsi", "Brownie"]

    def show_items(self):
        print("Combo Items:")
        for item in self.combo_items:
            print("-", item)

    def extra_discount(self):
        percent = 20
        discount = self.price * percent / 100
        self.price -= discount


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.order_history = []

    def place_order(self, order):
        self.order_history.append(order)

    def view_order_history(self):
        for order in self.order_history:
            print(f"Order ID: {order.order_id}, Total: ₹{order.total_price}")


class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []
        self.total_price = 0

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        self.total_price = sum(item.price for item in self.items)
        return self.total_price

    def apply_coupon(self, code):
        self.calculate_total()

        if code == "SAVE10":
            discount = 0.10
        elif code == "SAVE20":
            discount = 0.20
        else:
            print("Invalid coupon code")
            return self.total_price

        self.total_price -= self.total_price * discount
        return self.total_price


# ---------------- Example ----------------

burger = FoodItem("Burger", 150, "Fast Food")
pizza = FoodItem("Pizza", 300, "Fast Food")
combo = ComboMeal("Combo Meal", 500, "Combo")
fries = FoodItem("French Fries", 120, "Starter")
garlic_bread = FoodItem("Garlic Bread", 180, "Starter")
sandwich = FoodItem("Veg Sandwich", 140, "Snack")
pasta = FoodItem("White Sauce Pasta", 260, "Main Course")
noodles = FoodItem("Hakka Noodles", 220, "Main Course")
fried_rice = FoodItem("Fried Rice", 240, "Main Course")
paneer_tikka = FoodItem("Paneer Tikka", 280, "Starter")
chole_bhature = FoodItem("Chole Bhature", 200, "Main Course")
masala_dosa = FoodItem("Masala Dosa", 180, "South Indian")
cold_coffee = FoodItem("Cold Coffee", 130, "Beverage")
coke = FoodItem("Coca Cola", 60, "Beverage")
brownie = FoodItem("Chocolate Brownie", 110, "Dessert")
ice_cream = FoodItem("Vanilla Ice Cream", 90, "Dessert")
gulab_jamun = FoodItem("Gulab Jamun", 80, "Dessert")
family_combo = ComboMeal("Family Combo", 899, "Combo")
kids_combo = ComboMeal("Kids Combo", 299, "Combo")
pizza_combo = ComboMeal("Pizza Combo", 699, "Combo")
burger_combo = ComboMeal("Burger Combo", 399, "Combo")

order = Order("ORD101")
order.add_item(burger)
order.add_item(pizza)
order.add_item(combo)



print("Total Price:", order.calculate_total())

print("After Coupon:", order.apply_coupon("SAVE10"))

customer = Customer("Rahul", "C101")
customer.place_order(order)

print("\nOrder History:")
customer.view_order_history()


print("-------------------------------------------------------------------------------------------------------")


''' Practice code 5 = Library management system add books, manage users, borrow and return books '''


class Book:
    def __init__(self, title, author, ISBN, availability=True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability = availability

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.ISBN}")
        print(f"Available: {self.availability}")


class PhysicalBook(Book):
    def __init__(self, title, author, ISBN, availability=True):
        super().__init__(title, author, ISBN, availability)


class Ebook(Book):
    def __init__(self, title, author, ISBN, availability=True):
        super().__init__(title, author, ISBN, availability)


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)


class Student(User):
    limit = 3

    def borrow_book(self, book):
        if len(self.borrowed_books) < self.limit:
            self.borrowed_books.append(book)
            book.availability = False
            print("Book borrowed by student")
        else:
            print("Student borrowing limit exceeded")


class Teacher(User):
    limit = 5

    def borrow_book(self, book):
        if len(self.borrowed_books) < self.limit:
            self.borrowed_books.append(book)
            book.availability = False
            print("Book borrowed by teacher")
        else:
            print("Teacher borrowing limit exceeded")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        print("Book not found")

    def display_books(self):
        for book in self.books:
            book.display()

    def return_book(self, book):
        book.availability = True
        print("Book returned")


# Creating books
book1 = PhysicalBook("1984", "George Orwell", "ISBN001")
book2 = Ebook("Harry Potter", "J.K Rowling", "ISBN002")
book3 = PhysicalBook("The Great Gatsby", "F.Scott", "ISBN003")
book4 = Ebook("The Alchemist", "Paulo Coelho", "ISBN004")
book5 = PhysicalBook("Pride and Prejudice", "Jane Austen", "ISBN005")
book6 = Ebook("Atomic Habits", "James Clear", "ISBN006")
book7 = PhysicalBook("To Kill a Mockingbird", "Harper Lee", "ISBN007")
book8 = Ebook("Rich Dad Poor Dad", "Robert Kiyosaki", "ISBN008")
book9 = PhysicalBook("The Hobbit", "J.R.R. Tolkien", "ISBN009")
book10 = Ebook("Deep Work", "Cal Newport", "ISBN010")
book11 = PhysicalBook("1984", "George Orwell", "ISBN001")
book12 = Ebook("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "ISBN002")
book13 = PhysicalBook("The Great Gatsby", "F. Scott Fitzgerald", "ISBN003")

# Creating library
library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


# Creating users
student = Student("Rahul", "Sharma")
teacher = Teacher("Amit", "Verma")


# Borrowing books
student.borrow_book(book1)
teacher.borrow_book(book2)


# Display library books
library.display_books()

print("-------------------------------------------------------------------------------------------------------")


''' Practice code 6 = Car Engine and Starting the Car Engine '''


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()

    class Engine:
        def __init__(self):
         self.status = "off"


        def start(self):
            self.status = "Running"
            print("Engine started")
        def stop(self):
            self.status ="Off"
            print("Engine stopped")

    def drive(self):
        if self.engine.status == "Running":
            print(f"Driving {self.brand} {self.model}")
        else:
            print(f"Start the Engine First")

car = Car("BMW", "M5")
Car2 = Car("Mustang", "GT")
car.drive()
car.engine.start()
car.drive()

print("-------------------------------------------------------------------------------------------------------")


'''Practice 7 - How to access any file in the system and read and write it through pyton'''


with open(r"C:\Users\Admin\Documents\Note.txt", "r") as file:
    content = file.read()
    print(content)

print("OR")


with open(r"C:\Users\Admin\Documents\Note.txt", "w") as file:
    file.write("I am too good")


with open(r"C:\Users\Admin\Documents\Note.txt", "r") as file:
    print(file.read())


print("-------------------------------------------------------------------------------------------------------")

''' Practice code 8 '''


class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display_info(self):
        print("Name:", self.name)
        print("ID:", self.id)


class Member(Person):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.__borrowed_books = []
        self.limit = 3

    def borrow_book(self, book):

        if len(self.__borrowed_books) < self.limit:

            if book.available:
                self.__borrowed_books.append(book)
                book.available = False
                print(f"{book.title} borrowed successfully")
            else:
                print("Book is not available")

        else:
            print("Borrowing limit exceeded")

    def return_book(self, book):

        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.available = True
            print(f"{book.title} returned successfully")

        else:
            print("Book not found")

    def get_borrowed_books(self):
        return self.__borrowed_books

    def display_info(self):
        super().display_info()
        print("Borrowed books:")

        for book in self.__borrowed_books:
            print(book.title)


class Librarian(Person):

    def __init__(self, name, id):
        super().__init__(name, id)
        self.books = []

    def add_book(self, book):

        self.books.append(book)
        print(f"{book.title} added successfully")

    def remove_book(self, book):

        if book in self.books:
            self.books.remove(book)
            print(f"{book.title} removed successfully")


    def display_info(self):

        super().display_info()
        print("Books:")

        for book in self.books:
            print(book.title)



class Book:

    def __init__(self, title, author, ISBN):

        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = True


    def display(self):

        print("Title:", self.title)
        print("Author:", self.author)
        print("ISBN:", self.ISBN)
        print("Available:", self.available)



class Library:

    def __init__(self):

        self.books = []


    def add_book(self, book):

        self.books.append(book)


    def search_book(self, title):

        for book in self.books:

            if book.title.lower() == title.lower():
                return book

        print("Book not found")
        return None


    def display_books(self):

        for book in self.books:
            book.display()


    def return_book(self, book):

        book.available = True
        print("Book returned")



# -------------------------------
# Creating Books
# -------------------------------

book1 = Book("1984", "George Orwell", "ISBN001")
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "ISBN002")
book3 = Book("The Alchemist", "Paulo Coelho", "ISBN003")
book4 = Book("Atomic Habits", "James Clear", "ISBN004")


# Creating Library

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)


# Display all books

library.display_books()


print("------------------")


# Creating Member

student = Member("John", 101)

student.display_info()


print("------------------")


# Borrow book

student.borrow_book(book1)


print("------------------")


# Display member info

student.display_info()


print("------------------")


# Return book

student.return_book(book1)




print("-------------------------------------------------------------------------------------------------------")

''' Practice code 9 = Rectangle area and perimeter finder and founding that it is a square or not '''

class Rectangle:
    def __init__(self, length ,width):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

    def is_square(self):
        if self.length==self.width:
            return True
        else:
            return False

    def display_info(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())

        if self.is_square():
            print("This is a Square")
        else:
            print("This is not a Square")


r1 = Rectangle(23,5)
r1.display_info()

print("-------------------------------------------------------------------------------------------------------")

''' Practice code 10 = Bank account deposit and withdraw '''

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrew:", amount)
            print("Current Balance:", self.balance)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current Balance:", self.balance)

acc = BankAccount("Rahul", 1000)

acc.check_balance()

acc.deposit(500)

acc.withdraw(300)

acc.withdraw(2000)

acc.check_balance()


print("-------------------------------------------------------------------------------------------------------")
