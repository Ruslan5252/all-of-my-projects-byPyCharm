class Book():
    def __init__(self, name, author="", year_release=""):
        self.name = name
        self.author = author
        self.year_release = year_release

    def display(self):
        print(f"{self.name}{self.author}{self.year_release}")


class Library(Book):
    def __init__(self,name_library,books=[]):
        self.name_library = name_library
        self.books=books
    def add_book(self,name,author="", year_release=""):
        book=Book(name,author,year_release)
        self.books.append(book)
    def list(self):
        for i in self.books:
            print(i.display())
    def filter(self,name="",author="", year_release=""):
        for i in self.books:
            if i(name)==self.name or i(author)==self.author or i(year_release)==self.year_release:
                print(i)

book_1 = Book('Чистый код', 'Дядя Боб', 2017)
book_2 = Book('От 2 до 5', 'Корней Чуковский', 1958)
book_3 = Book('Идеальный программист', 'Дядя Боб', 2018)
book_4 = Book('Рецепты татарской кухни', year_release=2018)
library = Library('Домашняя библиотека')
library.add_book(book_1)

library.add_book(book_2)

library.add_book(book_3)

library.add_book(book_4)
print(library.name_library)
library.list()

books = library.filter('Чистый код', 'Дядя Боб', 2017)







