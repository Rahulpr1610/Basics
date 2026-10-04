class MovieTicket:
    def __init__(self,movie_name,available_seats):
        self.movie_name = movie_name
        self.available_seats = available_seats

    def book_ticket(self,seats):
        if seats <= self.available_seats:
            self.available_seats -= seats
            print("Booking successful")
        else:
            print("NOt enough seats available!")

    def cancel_ticket(self,seats):
            self.available_seats += seats
            print("Ticket cancelled successfully")

    def show_status(self):
        print("Movie_name: ",self.movie_name)
        print("Available_seats: ",self.available_seats)

p = MovieTicket("Lokha",120)
p.book_ticket(51)
p.cancel_ticket(12)
p.show_status()
