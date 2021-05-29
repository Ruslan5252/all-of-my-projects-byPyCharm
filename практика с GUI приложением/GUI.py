
import tkinter as tk

win = tk.Tk()
win.geometry("500x600")
win.title("мое первое GUI приложение")
for i in range(5):
    for j in range(2):
        tk.Button(win,text='Hello').grid(row=i,column=j,stick='we')
        win.grid_columnconfigure(0,minsize=200)
        win.grid_columnconfigure(1,minsize=100)
btn1 = tk.Button(win, text='Hello 1')
btn2 = tk.Button(win, text='Hello 2')
btn3 = tk.Button(win, text='Hello 3')
btn4 = tk.Button(win, text='Hello world')
btn5 = tk.Button(win, text='Hello 5')
btn6 = tk.Button(win, text='Hello 6')
btn7 = tk.Button(win, text='Hello 7')
btn8 = tk.Button(win, text='Hello 8')

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1,stick='we')
btn3.grid(row=1, column=0)
btn4.grid(row=1, column=1)
btn5.grid(row=2, column=0)
btn6.grid(row=2, column=1,stick='we')
btn7.grid(row=3, column=0,columnspan=2,stick='we')
btn8.grid(row=0, column=2,rowspan=4,stick='NS')
win.mainloop()  # открыть главный цикл ( запустить окно)'''

import tkinter as tk


def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print("Empty Entry")


def delete_entry():
    name.delete(0, 'end')


win = tk.Tk()
win.geometry("500x600")
win.title("мое первое GUI приложение")
tk.Label(win, text='Имя').grid(row=0, column=0, stick='w')
name = tk.Entry(win)
name.grid(row=0, column=1)
tk.Button(win, text='get', command=get_entry).grid(row=1, column=0, stick='n')
tk.Button(win, text='delete', command=delete_entry).grid(row=1, column=1, stick='n')
tk.Button(win, text='insert', command=lambda: name.insert(0, 'hello')).grid(row=1, column=2, stick='we')
win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=200)
win.mainloop()
