#!/usr/bin/python3
# -*- coding: utf-8 -*-
# FILE: notepad_v_01.py
# RUN : python3 notepad_v_01.py
# -----------------------------------------------------------BEGIN file
import tkinter as tk
import os
from tkinter import filedialog as fd
from tkinter.colorchooser import askcolor
import time
import datetime

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
        self.file_submenu.add_command(label="Open", command=self.open)
        self.file_submenu.add_command(label="Save", command=self.save)
        self.file_submenu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_submenu)
        #=============================================================
        # Edit Menu
        #============================================================
        self.edit = tk.Menu(self.menu_bar, tearoff=0)
        self.edit.add_command(label="Clear All", command=self.clearall)
        self.edit.add_command(label="Insert date", command=self.date)
        self.edit.add_command(label="Insert hour", command=self.ora)
        self.edit.add_command(label="Insert line", command=self.line)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit)
        #=============================================================
        # Options menu
        #=============================================================
        self.options = tk.Menu(self.menu_bar, tearoff=0)
        self.options.add_command(label="Text normal", command=self.normal)
        self.options.add_command(label="Text bold", command=self.bold)
        self.options.add_command(label="Text underline", command=self.underline)
        self.options.add_command(label="Text italic", command=self.italic)
        self.menu_bar.add_cascade(label="Options", menu=self.options)
        #=============================================================
        # View Menu
        #=============================================================
        self.view = tk.Menu(self.menu_bar, tearoff=0)
        self.view.add_command(label="Background", command=self.background)
        self.view.add_command(label="Text")
        self.menu_bar.add_cascade(label="View",menu=self.view) 
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
        #============================================================
        # Add image icon on window
        #============================================================
        p1 = tk.PhotoImage(file="texteditor.png")
        self.parent.iconphoto(False, p1)
        #===========================================================
        # add toolbar icons
        #============================================================
        self.toolbar = tk.Frame(self.parent, bd=1, relief=tk.RAISED)
        self.ceas = tk.Label(self.toolbar, text="Ceas")
        self.ceas.pack(side=tk.LEFT)
        self.update()
        self.closeCalc = tk.Button(self.parent, text="Close Computer",
                                   command=self.shutdownComputer)
        self.closeCalc.pack(side=tk.LEFT)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

    #### =========================================
    ### Function to italic text
    #### =========================================
    def italic(self):
       self.text_area.config(font=('Segio UI',20,'italic'))

    #### =========================================================
    ### Function to underline text
    #### ==========================================================
    def underline(self):
        self.text_area.config(font=('Segio UI',20,'underline'))
    
    #==========================================================
    # Function to bold text
    #=========================================================
    def bold(self):
        self.text_area.config(font=('Segio UI', 20, "bold"))

    #==========================================================
    # Function text normal
    #==========================================================
    def normal(self):
        self.text_area.config(font=("Segio UI", 20))
        
    #============================================================
    # Function to insert hour
    #===========================================================
    def ora(self):
        ora=time.localtime()
        self.text_area.insert(tk.INSERT, ora)

    #============================================================
    # Function to insert a line in tk.Text
    #============================================================
    def line(self):
        line="-"*60
        self.text_area.insert(tk.INSERT, line)

    #==============================================================
    # Function to insert date
    #============================================================
    def date(self):
        data = datetime.date.today()
        self.text_area.insert(tk.INSERT, data)
    #==============================================================
    # Tk text clearall
    #==============================================================
    def clearall(self):
        self.text_area.delete(1.0, tk.END)
    #===============================================================
    # Tk Text backgroud
    #===============================================================
    def background(self):
        (triple, color)=askcolor()
        if color:
            self.text_area.config(background=color)
    
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
    #==============================================================
    # Tkinter Open File Dialog function
    #==============================================================
    def open(self):
        filetypes = (('text files', '*.txt'),
                     ('All files', '*.*'))
        filename = fd.askopenfile(filetypes=filetypes)
        #showinfo( title="Selected File", message=filename)
        self.text_area.insert('1.0', filename.readlines())
    #==============================================================
    # Tkinter save file dialog function
    #==============================================================
    def save(self):
        f = fd.asksaveasfile(mode='w', defaultextension='.txt')
        if f is None:
            return
        text2save = str(self.text_area.get(1.0, tk.END))
        f.write(text2save)
        f.close()
    #==============================================================
    # Update time in ceas
    #==============================================================
    def update(self):
        self.ceas.config(text=time.strftime("%I:%M:%S"))
        self.ceas.after(1000, self.update)
    #=============================================================
    # Close the computer
    #=============================================================
    def shutdownComputer(self):
        os.system("shutdown now")
        
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Python Tkinter Notepad")
    Notepad(root).pack(side="top", fill="both")
    root.mainloop()
#--------------------------------------------------------------END file
