from tkinter import *

window = Tk()

t1 = Text(window, height=1, width=20)
t1.tag_configure("center", justify="center")
t1.insert(END, "Kg")
t1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

b1 = Button(window, text="Convert")
b1.grid(row=0, column=2, rowspan=1)

# show window
window.mainloop()