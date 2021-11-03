#!/usr/bin/pytho3
# -*- coding: utf-8 -*-
# FILE: notepad_v_01.py
# RUN : python3 notepad_v_01.py
# __________________________________________BEGIN file
import tkinter as tk

class Notepad(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent 
        # --------------------------------------menu_bar
        self.menu_bar = tk.Menu(self.parent)


        # File Submenu
        self.file_submenu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_submenu.add_command(label="New")
        self.file_submenu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_submenu)


        self.parent.config(menu=self.menu_bar)
        
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Python Tkinter Notepad")
    Notepad(root).pack(side="top", fill="both")
    root.mainloop()
#---------------------------------------------END file
