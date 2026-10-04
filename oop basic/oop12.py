class HotelRoom:
    def __init__(self,room_number,guest_name=None,is_booked=False):
        self.room_number = room_number
        self.guest_name = guest_name
        self.is_booked = is_booked

    def book_room(self,guest_name):
        self.guest_name = guest_name
        self.is_booked = True
        print(f"{guest_name} is booked room number {self.room_number}")

    def vacate_room(self):
        self.guest_name = None
        self.is_booked = False

        print(f"{self.room_number} is vacated")

    def show_status(self,):
        print(f"Room Number: {self.room_number}")
        print(f"Booked: {self.is_booked}")
        print(f"Guest Name: {self.guest_name}")
        print("...........................")

room = HotelRoom(101)

room.show_status()
room.book_room("rahul")
room.show_status()
room.vacate_room()
room.show_status()
