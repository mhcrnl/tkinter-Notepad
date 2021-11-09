#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# FILE: __main__.py
# RUN : python3 __main__.py
# AUTHOR: mhcrnl@gmail.com

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        """
        w = ttk.Button(master,option=value, ...)
        """
        self.exit_btn = ttk.Button(self, text="Exit", command=self.quit)
        self.exit_btn.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()

