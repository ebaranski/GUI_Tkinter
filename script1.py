from tkinter import *

window = Tk()


def km_to_miles():
    miles = float(e1_value.get()) * 1.6
    t1.insert(END, miles)


# add widget (button) to window (.grid or .pack)
# www.tkdocs.com/images/gridexample1.png
b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0, rowspan=1)

# add widget (input box) to window
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

# add widget (text) to window
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

# enter value, press button and show in text
# for button to do something, add command parm to run function
# get input field by using textvariable parm on Entry widget (use .get() to get string value)
# add value to text by using .insert

# show window
window.mainloop()
