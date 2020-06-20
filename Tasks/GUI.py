
from Tasks.enter_task import *

from tkinter import *
from tkinter import scrolledtext

def gui_interface(output):
    window = Tk()

    window.title("Библиотека художественной литературы")
    window.geometry('2000x1400+200+300')

    txt = scrolledtext.ScrolledText(window, width=120, height=30, padx=10, pady=5)
    txt.place(x=15, y=400)
    txt.insert(END, output + '\n')

    text = Entry(window, width=100)
    text.place(x=15, y=50)

    btn = Button(window, text="Кнопка ввода!", padx=10, pady=5, command=text)
    btn.place(x=1500, y=100)

    window.mainloop()






