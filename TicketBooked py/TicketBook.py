from abc import *
class BookmyShow(ABC):
    @abstractmethod
    def TicketBook(self):
        pass
    @abstractmethod
    def Movielist(self):
        pass
    @abstractmethod
    def checkseats(self):
        pass
    def discount(self, amt):
        print("**10% Discount for Online Booking**")
        return amt * 10 / 100

class SenthilTheater(BookmyShow):
    def __init__(self):
        self.seats = 115
    def TicketBook(self):
        try:
            n = int(input("Enter a Seats Count: ")) 
            if n <= self.seats:
                print("----------------------------------") 
                print("As per Seats Price: Rs.175/-")
                t = n * 175
                print("--Total Amount:Rs.", t,"/-")
                print("----------------------------------") 
                d = super().discount(t)
                print("Discount Amount: Rs.", d)
                print("*Payable Amount: Rs.", t - d,"/-")
                print("----------------------------------") 
                self.seats -= n
                print("Ticket Booked Successfully..!")
            else:
                print("Sorry, not enough seats available.")
        except ValueError:
            print("Invalid input..! Please enter a valid number for seats.")

    def Movielist(self):
        print("Movie List:")
        print("1. Goat")
        print("2. Amaran")
        print("3. Vetaiyan")
        print("4. Kanguva")
    def checkseats(self):
        print("----------------------------------") 
        print("Available Seats:", self.seats)

b = SenthilTheater()

while True:
    try:
        print("--- Welcome to BookMyShow ---")
        print("1. Ticket Booking")
        print("2. View Movies List")
        print("3. Check Seat Availability")
        print("4. Exit")
        print("----------------------------------")
        opt = int(input("Select An Option: "))
        if opt == 1:
            b.TicketBook()
        elif opt == 2:
            b.Movielist()
        elif opt == 3:
            b.checkseats()
        elif opt == 4:
            print("----------------------------------") 
            print("Application Closed.., Thank you for using BookMyShow!")
            break
        else:
            print("Invalid Option..! Please choose a valid option.")
    except ValueError:
        print("Invalid input..! Please enter a number between 1 and 4.")
    print("----------------------------------") 
