#!/usr/bin/pytho3
# -*- coding: utf-8 -*-
# FILE: notepad_v_01.py
# RUN : python3 notepad_v_01.py
# -----------------------------------------------------------BEGIN file
import tkinter as tk
import os
class Notepad(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent 
        #=============================================================
        #				1. MENU BAR
        #=============================================================
        self.menu_bar = tk.Menu(self.parent)
        #=============================================================
        #          1.A File Submenu
        #=============================================================
        self.file_submenu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_submenu.add_command(label="New")
        self.file_submenu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_submenu)
        #=============================================================
        #    HELP MENU
        #=============================================================
        self.help = tk.Menu(self.menu_bar, tearoff=0)
        self.help.add_command(label="View help")
        self.help.add_command(label="Github push",command=self.push)
        self.menu_bar.add_cascade(label="Help", menu=self.help)
        
        self.parent.config(menu=self.menu_bar)
        #===========================================================
        # ADD TEXT AREA
        #==========================================================
        self.text_area = tk.Text(self.parent, font="Lucida 14",undo=True)
        self.create_text_area()
    #================================================================
    # ACTUALIZAREA CODULUI PE GITHUB(executa fila gitpush.sh)
    #================================================================
    def push(self):
        os.system("./gitpush.sh")
    #===============================================================
    def create_text_area(self):
        # text area 
        self.text_area.pack(expand=True, fill="both")
        # scroll bar
        self.scroll_bar = tk.Scrollbar(self.text_area)
        self.scroll_bar.pack(side = tk.RIGHT, fill=tk.Y)
        self.scroll_bar.config(command=self.text_area.yview)
        
        self.text_area.config(yscrollcommand=self.scroll_bar.set)
        
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Python Tkinter Notepad")
    Notepad(root).pack(side="top", fill="both")
    root.mainloop()
#--------------------------------------------------------------END file
