class Book():
    def __init__(self,name,author="",year_release=""):
        self.name=name
        self.author=author
        self.year_release=year_release


    def display(self):
        print(f"{self.name:<30}{self.author:<20}{self.year_release:>5}" )
book = Book('Title', 'Author', 2020)

book.display()
book = Book('Title', year_release=2020)

book.display()

book = Book('Title', 'author')

book.display()