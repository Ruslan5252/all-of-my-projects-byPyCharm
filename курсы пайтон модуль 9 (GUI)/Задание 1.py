from tkinter import *

window = Tk()
window.title("First GUI APP")

textLabel = Label(window, text="Hello, ", font=("Calibri", 20), width=30)

textLabel.grid(row=0, column=0)
window.mainloop()