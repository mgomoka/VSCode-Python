from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Tkinter")
window.geometry('350x200')

combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Text")
combo.current(1) # Set The Selected Item
combo.grid(column = 0, row = 0)

window.mainloop()
