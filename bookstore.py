import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pygubu


class bookstoreApp:

    def __init__(self):
        # create a builder
        self.builder = builder = pygubu.Builder()

        # load an ui file
        builder.add_from_file('window.ui')

        # create the mainwindow
        self.toplevel_1 = builder.get_object('toplevel_1')

        # set any style used in window.ui
        # c:\Users\ericb\PythonProjects\pygubu\env\Scripts\pygubu-designer.exe
        # See https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style
        ttk.Style().configure('CustomFrame.TFrame', background='#afeadc')
        ttk.Style().configure('CustomLabel.TLabel', background='#afeadc', foreground='#041e42')
        style = ttk.Style()
        style.map("CustomButton.TButton",
                  foreground=[('pressed', 'red'), ('active', '#041e42')],
                  background=[('pressed', '!disabled', 'black'), ('active', 'white')]
                  )

        # connect callbacks
        builder.connect_callbacks(self)

    def view_all_click(self):
        messagebox.showinfo("Message", 'You clicked button View All')
        print('You clicked button View All')

    def delete_selection_click(self):
        messagebox.showinfo("Message", 'You clicked button Delete Selection')

    def add_entry_click(self):
        messagebox.showinfo("Message", 'You clicked button Add Entry')

        entry = self.builder.get_object('entry_title')
        value = entry.get()
        messagebox.showinfo("Message", value)

        entry = self.builder.get_variable('titlefield')
        value = entry.get()
        messagebox.showinfo("Message", repr(value))

    def close_click(self):
        messagebox.showinfo("Message", 'You clicked button Close')

    def update_selection_click(self):
        messagebox.showinfo("Message", 'You clicked button Update Selection')

    def search_entry_click(self):
        messagebox.showinfo("Message", 'You clicked button Search Entry')

    def run(self):
        self.toplevel_1.mainloop()


if __name__ == '__main__':
    app = bookstoreApp()
    app.run()
