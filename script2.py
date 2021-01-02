from tkinter import *

window = Tk()

def convert_number():
    grams = float(e1_value.get()) * 1000
    t2.delete("1.0", END)  #Delete contents from start to end
    t2.insert(END, grams)
    pounds = float(e1_value.get()) * 2.20462
    t3.delete("1.0", END)
    t3.insert(END, pounds)
    ounces = float(e1_value.get()) * 35.274
    t4.delete("1.0", END)
    t4.insert(END, ounces)


t1 = Text(window, height=1, width=20)
t1.tag_configure("label1", justify="center")
t1.insert(END, "Kg", "label1")
t1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

b1 = Button(window, text="Convert", width=20, command=convert_number)
b1.grid(row=0, column=2, rowspan=2)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=0)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=1)

t4 = Text(window, height=1, width=20)
t4.grid(row=1, column=2)

# show window
window.mainloop()