from tkinter import *

window = Tk()
window.title("Calculator")


def calculate():
    global f
    display.delete(0, END)
    display.insert(END, eval(f[0].replace('=', "")))
    f.clear()

def click(text):
    global f

    display.insert(END, text)
    if text == "=":
        f.append(display.get())
        display.delete(5, END)
        calculate()
    if text == "CE":
        display.delete(0, END)
        f.clear()
    print(f)

display = Entry(window, fg = 'black', width = 17,  font="Calibri 14")
display.grid(row=0, column=0, columnspan=4)

btn = (('7', '8', '9', '/', 'CE'),
       ('4', '5', '6', '*', ' '),
       ('1', '2', '3', '-', ' '),
       ('0', '.', '=', '+', ' ')
       )

for i in range(4):
    for j in range(5):
            button = Button(window, text=btn[i][j], width=10, command=lambda i=i, j=j: click(btn[i][j]), font='Calibri 12', bg='grey', fg='white')
            button.grid(row=i+2, column=j , padx=8, pady=8)
window.grid_rowconfigure(6, weight=1)
window.grid_columnconfigure(4, weight=1)
activeStr = ''

f = []
display.delete(0, END)
mainloop()