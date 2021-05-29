class Book:
    def __init__(self,number,title,author,pages):
        self.number=number
        self.title=title
        self.author=author
        self.pages=pages
    def getData(self):
        print(self.number,self.title,self.author,self.pages)

class Main:
    a=[]
    b=Book(1,"титулка1","автор1",1)
    c=Book(2,"титулка2","автор2",2)
    d=Book(3,"титулка3","автор3",3)
    e=Book(4,"титулка4","автор4",4)
    g=None
    a.append(b)
    a.append(c)
    a.append(d)
    a.append(e)
    a.append(g)
    try:
        for i in a:
            i.getData()
    except:
        AttributeError
        print("Book is empty")
    else:
        print("Все гуд")
    finally:
        print("Конец проверки")


