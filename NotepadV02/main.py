#!/usr/bin/env python3
"""
Tkinter template file

In this file, we use the pack manager to create an app.

Author: mhcrnl@gmail.com
-------------------------------------------------------------
"""
import tkinter as tk
from tkinter import ttk, Menu
from tkinter.messagebox import showinfo
import sys

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title("My Awesome App")
        self.geometry("450x350")

        p1 = tk.PhotoImage(file='teamwork.png')
        self.iconphoto(False, p1)

        self.config(menu=MenuBar(self))
      
        # label

        self.label = ttk.Label(self, text="Hello, Tkinter!")
        self.label.pack()

        # button
        self.button = ttk.Button(self, text="Click ME!")
        self.button['command'] = self.button_clicked
        self.button.pack()

        #self.config(menu=MenuBar(self)

    def button_clicked(self):
        showinfo(title="Information",
                 message="Hello, Tkinter!")

class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        filemenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=filemenu)
        filemenu.add_command(label="New", command=self.callback)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1, command=self.quit)

        helpmenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.callback)

    def quit(self):
        sys.exit(0)
    
    def callback(self):
        print ("called the callback!")

        

if __name__ == "__main__":
    app = App()
    app.mainloop()
    exit(0)
    
