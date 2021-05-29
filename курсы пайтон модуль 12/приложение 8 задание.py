from tkinter import *


def press_key(event):
    print(event)
    if event.char == '\r':
        saveUsers()
    elif event.char == '\x08':
        clearList()
    elif event.char == ' ':
        clearfields()





def saveUsers():
    id = IDEntry.get()
    log = LOGINEntry.get()
    passw = PASSWORDEntry.get()
    file = open("mem.txt", 'a')
    resultBox.insert(END, 'id ' + str(id) + '\n')
    resultBox.insert(END, 'login ' + str(log) + '\n')
    resultBox.insert(END, 'password ' + str(passw) + '\n')
    resultBox.insert(END, '-----------------------' + '\n')
    file.write('id ' + str(id) + '\n')
    file.write('login ' + str(log) + '\n')
    file.write('password ' + str(passw) + '\n' + '-----------------------' + '\n')
    file.close()

def clearList():
    resultBox.delete(0, END)
    file = open("mem.txt", 'w')
    file.write("")


def clearfields():
    IDEntry.delete(0, END)
    IDEntry.insert(0, "")

    LOGINEntry.delete(0, END)
    LOGINEntry.insert(0, "")

    PASSWORDEntry.delete(0, END)
    PASSWORDEntry.insert(0, "")


window = Tk()
window['bg'] = '#234754'
window.bind("<Key>", press_key)
window.geometry("450x600+100+200")
window.title("Задание 8 ")

IDLabel = Label(window, text="ID:", font="Calibri 14")
IDLabel.grid(row=0, column=0, padx=20, pady=20)

LOGINLabel = Label(window, text="LOGIN:", font="Calibri 14")
LOGINLabel.grid(row=1, column=0, padx=20, pady=20)

PASSWORDLabel = Label(window, text="PASSWORD:", font="Calibri 14")
PASSWORDLabel.grid(row=2, column=0, padx=20, pady=20)

IDEntry = Entry(window, fg='black', width=17, font="Calibri 14")
IDEntry.grid(row=0, column=1, padx=20, pady=20)

LOGINEntry = Entry(window, fg='black', width=17, font="Calibri 14")
LOGINEntry.grid(row=1, column=1, padx=20, pady=20)

PASSWORDEntry = Entry(window, fg='black', width=17, font="Calibri 14")
PASSWORDEntry.grid(row=2, column=1, padx=20, pady=20)

resultBox = Listbox(window, width=35, height=35, font="14")
resultBox.grid(row=4, column=0, columnspan=2, padx=20, pady=20)
file = open("mem.txt", 'r')
for x in file:
    resultBox.insert(END, x)
    print(x)

add_button = Button(window, width=20, text="ADD USER", command=saveUsers, font="Calibri 12", bg="gray", fg="white")
add_button.grid(row=3, column=0, padx=20, pady=20)

clearButton = Button(window, width=20, text="CLEAR LIST", command=clearList, font="Calibri 12", bg="red", fg="white")
clearButton.grid(row=3, column=1, padx=20, pady=20)

window.mainloop()
