import string
class Alphabet():
    def __init__(self,lang,letters):
        self.lang=lang
        self.letters=letters
    def print(self):
        print("буквы русского алфавита:","абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    def letter_num(self):
        print(len(self.letters))
class EngAlphabet(Alphabet):
    def __init__(self,lang,letters,ans):
        super().__init__(lang,letters)
        self.ans=ans
    def print(self):
        print("буквы английского алфавита:", "abcdifghijklmnopqrstuvwxyz")
    def is_en_letter(self,letter):
        self.letter=letter
        list=string.ascii_letters
        if letter in list:
            print("Такая буква есть в английскоом алфавите")
        else:
            print("Введеная буква не относится к английскому алфавиту")
    def example(self):
        print("In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content")
a=EngAlphabet("en","abcdef","wqegf")
a.print()
a.letter_num()
a.is_en_letter("f")
a.example()
