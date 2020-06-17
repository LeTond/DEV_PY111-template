
from Tasks.enter_task import *

from tkinter import *
from tkinter import scrolledtext


def gui_interface(output):
    window = Tk()

    window.title("Библиотека художественной литературы")
    window.geometry('2600x1400+200+300')

    text = Entry(window, width=100)
    text.place(x=50, y=50)

    btn = Button(window, text="Кнопка ввода!", padx=10, pady=5)
    btn.place(x=2200, y=100)

    txt = scrolledtext.ScrolledText(window, width=120, height=30, padx=10, pady=5)
    txt.place(x=300, y=400)
    txt.insert(END, output + '\n')

    window.mainloop()



