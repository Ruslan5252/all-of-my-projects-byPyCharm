class Lion:
    def __init__(self,name):
        self.name=name
    def __repr__(self): # как будет видеть объект разработчик
        return f"The object Lion - {self.name} "
    def __str__(self):
        return f"The Lion - {self.name} "