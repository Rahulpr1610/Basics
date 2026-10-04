class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def show_info(self):
        print(f"The book title {self.title} and the book by {self.author}")

create_book = Book("Amazing spider-man","Rahul")
create_book2 = Book("Amazing spider-man2","sam")
create_book3 = Book("Amazing spider-man3","andrew")

create_book.show_info()
create_book2.show_info()
create_book3.show_info()