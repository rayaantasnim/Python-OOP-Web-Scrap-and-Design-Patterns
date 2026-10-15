# Class creating named Book:
class Book:
    title = ""
    author = ""
    price = ""

    def __init__(self, t, a, p):
        self.title = t
        self.author = a
        self.price = p

    def show_details(self):
        print(f"Book Name: {self.title} \nAuthor: {self.author} \nPrice: {self.price} BDT")
        print("")

    def apply_discount(self, percent):
        amount = self.price * (percent / 100)
        self.price = int(self.price - amount)
        print("")
        print(f"Discount applied: {percent}%")
        print(f"New Price: {self.price}")
        print("")


# Creating 7 book objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 2000)
book2 = Book("1984", "George Orwell", 1500)
book3 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 2500)
book4 = Book("Don Quixote", "Miguel de Cervantes", 1198)
book5 = Book("A Tale of Two Cities","Charles Dickens", 742)
book6 = Book("The Lord of the Rings", " J.R.R. Tolkien", 3198)
book7 = Book("The Little Prince", "Antoine de Saint-Exupéry", 1500)

# Showing details
book1.show_details()
book2.show_details()
book3.show_details()
book4.show_details()
book5.show_details()
book6.show_details()
book7.show_details()

# Applying discounts by input
dis=int(input("Enter your desired value of discount:"))

while(True):
    if(dis>50):
        print ("Discount exceeds permitted limit. Transaction cannot proceed.")
        dis = int(input("Enter again:"))
    else:
        book = input("Enter your book name:").lstrip()
        if(book == "The Great Gatsby"):
            book1.apply_discount(dis)

        elif(book == "1984"):
            book2.apply_discount(dis)

        elif(book == "Harry Potter and the Philosopher's Stone"):
            book3.apply_discount(dis)

        elif(book == "Don Quixote"):
            book4.apply_discount(dis)

        elif(book == "A Tale of Two Cities"):
            book5.apply_discount(dis)

        elif(book == "The Lord of the Rings"):
            book6.apply_discount(dis)

        elif(book == "The Little Prince"):
            book7.apply_discount(dis)

        else:
            print("Book is not found in our collection.")
        break 
 