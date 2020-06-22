from Tasks.enter_task import *

from tkinter import *
from tkinter import scrolledtext


def gui_interface(output):
    window = Tk()
    window.title("Библиотека художественной литературы")
    window.geometry('2000x1400+200+300')

    txt = scrolledtext.ScrolledText(window, width=120, height=30, padx=10, pady=5)
    txt.insert(END, output + '\n')

    text = Entry(window, width=100)
    global key
    key = text.get()

    btn = Button(window, text="Кнопка ввода!", padx=10, pady=5, command=text)

    txt.place(x=15, y=400)
    text.place(x=15, y=50)
    btn.place(x=1500, y=100)

    window.mainloop()

