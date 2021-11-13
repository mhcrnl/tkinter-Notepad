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
import webbrowser
import shutil
import tkinter.messagebox as tk2

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
        self.file_submenu.add_command(label="New", command=self.newFile)
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
        self.options.add_command(label="Terminal", command=self.startTerm)
        self.menu_bar.add_cascade(label="Options", menu=self.options)
        #=============================================================
        # View Menu
        #=============================================================
        self.view = tk.Menu(self.menu_bar, tearoff=0)
        self.view.add_command(label="Background", command=self.background)
        self.view.add_command(label="Text")
        self.menu_bar.add_cascade(label="View",menu=self.view)
        #### ========================================================
        ### Markdown menu
        #### =======================================================
        self.mark = tk.Menu(self.menu_bar, tearoff=0)
        self.mark.add_command(label="Title",    command=self.title)
        self.mark.add_command(label="Subtitle", command=self.subtitle)
        self.mark.add_command(label="Subsubtitle", command=self.subsubtitle)
        self.mark.add_command(label="Heading 4", command=self.heading4)
        self.mark.add_command(label="Heading 5", command=self.heading5)
        self.mark.add_command(label="Heading 6", command=self.heading6)
        self.mark.add_command(label="Bold text", command=self.markBold)
        self.mark.add_command(label="Italic text", command=self.markItalic)
        self.mark.add_command(label="Italic Bold", command=self.italicBold)
        self.mark.add_command(label="Blockquotes", command=self.blockquotes)
        self.mark.add_command(label="Lists", command=self.lists)
        self.mark.add_command(label="Unordered Lists", command=self.unordered)
        self.mark.add_command(label="Code", command=self.code)
        self.mark.add_command(label="Images", command=self.images)
        self.mark.add_command(label="Links", command=self.links)
        self.mark.add_command(label="Url insert", command=self.url)
        self.mark.add_command(label="Email", command=self.email)
        self.menu_bar.add_cascade(label="Markdown", menu=self.mark)
        #### ========================================================
        ### Python Menu
        #### ==========================================================
        self.python = tk.Menu(self.menu_bar, tearoff=0)
        self.python.add_command(label="Console", command=self.console)
        self.python.add_command(label="Print", command=self.pyprint)
        self.python.add_command(label="Single comment", command=self.scom)
        self.python.add_command(label="Multi comment", command=self.mcom)
        self.python.add_command(label="Variable", command=self.variable)
        self.python.add_command(label="List", command=self.pylist)
        self.python.add_command(label="Tuples", command=self.pytuple)
        self.python.add_command(label="Dict", command=self.pydict)
        self.python.add_command(label="If", command=self.pyif)
        self.menu_bar.add_cascade(label="Python", menu=self.python)
        #### ==============================================================
        ### tkinter Menu
        #### =============================================================
        self.pyth = tk.Menu(self.menu_bar, tearoff=0)
        self.pyth.add_command(label="Tk Template", command=self.templates)
        self.pyth.add_command(label="Tk window", command=self.tkwin)
        self.pyth.add_command(label="ttk.Label", command=self.ttkLabel)
        self.pyth.add_command(label="ttk.Button", command=self.ttkButton)
        self.menu_bar.add_cascade(label="Tkinter", menu=self.pyth)
        #=============================================================
        #    HELP MENU
        #=============================================================
        self.help = tk.Menu(self.menu_bar, tearoff=0)
        self.help.add_command(label="View help")
        self.help.add_command(label="Github push",command=self.push)
        self.help.add_command(label="About", command=self.about)
        self.help.add_command(label="Web site", command=self.web)
        self.help.add_command(label="Word Count", command=self.wordCount)
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

        self.createPopup()
        self.parent.bind("<Button-3>", self.doPopup)
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

    #### =================================================
    ### tkinter templates
    #### =================================================
    def templates(self):
        shutil.copy("./Templates/__main__.py", "./NewApp/__main__.py")

    #### =================================================
    ### ttk.Button function
    #### ================================================
    def ttkButton(self):
        line = ("\"\"\"\n w = ttk.Button(master,option=value, ...)\n\"\"\"\n")
        self.text_area.insert(tk.INSERT, line)
        line2 = "self.exit_btn = ttk.Button(self, text=\"Exit\", command=self.quit)"
        self.text_area.insert(tk.INSERT, line2)
        line3 = "\nself.exit_btn.pack()"
        self.text_area.insert(tk.INSERT, line3)
    #### ================================================
    ### Start terminal
    #### ================================================
    def startTerm(self):
        os.system("gnome-terminal 'sudo apt-get update'")

    #### ==================================================
    ### Python if
    #### ==================================================
    def pyif(self):
        line = "if expresion:\n    statements(s)"
        self.text_area.insert(tk.INSERT, line)

    #### ==================================================
    ### Python dict insert
    #### =================================================
    def pydict(self):
        line = " dict = {'nume':'mihai', 'prenume':'cornel', 'code':345}"
        self.text_area.insert(tk.INSERT, line)

    #### =================================================
    ### Python tuples insert
    #### =================================================
    def pytuple(self):
        line = "\"\"\"\nTuple is read-only lists.\n\"\"\"\ntuple = ('abcd', 786, 2.23, 'mihai')"
        self.text_area.insert(tk.INSERT, line)

    #### ==================================================
    ### Python list insert
    #### ===================================================
    def pylist(self):
        line = "mylist = ['abcd', 267, 2.45, 'mihai', 23.0]"
        self.text_area.insert(tk.INSERT, line)

    #### ====================================================
    ### Create variable
    #### =====================================================
    def variable(self):
        line = "myVariable = var"
        self.text_area.insert(tk.INSERT, line)

    #### ====================================================
    ### Start console
    #### =====================================================
    def console(self):
        os.system("python3")

    #### =======================================================
    ### Python multi line comment
    #### =======================================================
    def mcom(self):
        line = ("\"\"\"\n Comment\n\"\"\"")
        self.text_area.insert(tk.INSERT, line)
    
    #### =======================================================
    ### Python single comment line
    #### ======================================================
    def scom(self):
        line = "# Comment"
        self.text_area.insert(tk.INSERT, line)
        
    #### =======================================================
    ### Python print function insert
    #### =======================================================
    def pyprint(self):
        line = "print(\"Text to print\")"
        self.text_area.insert(tk.INSERT, line)

    #### ========================================================
    ### Help word count function
    #### ========================================================
    def wordCount(self):
        userText = self.text_area.get("1.0", tk.END)
        wordList = userText.split()
        number_of_words = len(wordList)
        tk2.showinfo("Word Count", "Words: " + str(number_of_words))
        
    #### ========================================================
    ### New function
    #### ========================================================
    def newFile(self):
        if(tk2.askyesno("Message", "Unseved work will be lost. Continue?")):
            self.text_area.delete("1.0", tk.END)

    #### =========================================================
    ### ttkLabel
    #### =========================================================
    def ttkLabel(self):
        line = """        self.label = ttk.Label(self, text='Hello')
        self.label.pack() """
        self.text_area.insert(tk.INSERT, line)
    #### ==========================================================
    ### Python insert tkwin
    #### =========================================================
    def tkwin(self):
        line ="""#!/usr/bin/env python3\n# -*- coding: utf-8 -*-
# FILE: __main__.py\n# RUN : python3 __main__.py\n# AUTHOR: mhcrnl@gmail.com\n
import tkinter as tk\nfrom tkinter import ttk
from tkinter.messagebox import showinfo\nclass App(tk.Tk):
    def __init__(self):\n        super().__init__()\n\n
if __name__ == "__main__":\n    app = App()\n    app.mainloop()\n"""
        self.text_area.insert(tk.INSERT, line)

    #### ==========================================================
    ### Markdown insert email
    #### =========================================================
    def email(self):
        line = "<mhcrnl@gmail.com>"
        self.text_area.insert(tk.INSERT, line)
        
    #### ==========================================================
    ### Markdown insert url
    #### =========================================================
    def url(self):
        line = "<https://github.com/mhcrnl/tkinter-Notepad>"
        self.text_area.insert(tk.INSERT, line)
        
    #### ==========================================================
    ### Markdown insert links
    #### =========================================================
    def links(self):
        line = "[Markdown Guide](https://www.markdownguide.org/basic-syntax/#headings)"
        self.text_area.insert(tk.INSERT, line)

    #### ==========================================================
    ### Markdown insert images
    #### =========================================================
    def images(self):
        line = "![name_of_image](/asset/images/tux.png)"
        self.text_area.insert(tk.INSERT, line)

    #### ==========================================================
    ### Markdown insert code
    #### =========================================================
    def code(self):
        line = "```\n Insert code \n``` "
        self.text_area.insert(tk.INSERT, line)

    #### ==========================================================
    ### Markdown insert unordered
    #### =========================================================
    def unordered(self):
        line = "- Item"
        self.text_area.insert(tk.INSERT, line)

    #### ==========================================================
    ### Markdown insert lists
    #### =========================================================
    def lists(self):
        line = "1. List"
        self.text_area.insert(tk.INSERT, line)

    #### ==========================================================
    ### Markdown insert blockquotes
    #### =========================================================
    def blockquotes(self):
        line = "> TEXT"
        self.text_area.insert(tk.INSERT, line)

    #### ==========================================================
    ### Markdown insert italic bold
    #### =========================================================
    def italicBold(self):
        line = " ***ItalicBold*** "
        self.text_area.insert(tk.INSERT, line)

    #### ==========================================================
    ### Markdown insert italic
    #### =========================================================
    def markItalic(self):
        line = " *ITALIC* "
        self.text_area.insert(tk.INSERT, line)

    #### ==========================================================
    ### Markdown insert bold
    #### =========================================================
    def markBold(self):
        line = " **TEXT** "
        self.text_area.insert(tk.INSERT, line)

    #### ==========================================================
    ### Markdown insert heding6
    #### =========================================================
    def heading6(self):
        line = "###### "
        self.text_area.insert(tk.INSERT, line)

    #### ==========================================================
    ### Markdown insert heding5
    #### =========================================================
    def heading5(self):
        line = "##### "
        self.text_area.insert(tk.INSERT, line)

    #### ==========================================================
    ### Markdown insert heding4
    #### =========================================================
    def heading4(self):
        line = "#### "
        self.text_area.insert(tk.INSERT, line)

    #### ==========================================================
    ### Markdown insert subsubtitle
    #### =========================================================
    def subsubtitle(self):
        line = "### "
        self.text_area.insert(tk.INSERT, line)

    #### ==========================================================
    ### Markdown insert subtitle
    #### =========================================================
    def subtitle(self):
        line = "## "
        self.text_area.insert(tk.INSERT, line)

    #### ==========================================================
    ### Markdown insert title
    #### =========================================================
    def title(self):
        line = "#  New title"*1
        self.text_area.insert(tk.INSERT, line)

    #### ===========================================================
    ### deschide browserul
    #### ===========================================================
    def web(self):
        webbrowser.open('https://github.com/mhcrnl/tkinter-Notepad')

    #### ===============================================================
    ### Meniul About
    #### ==============================================================
    def about(self):
        ad = tk.Toplevel(self.parent)
        txt = "Programmer: Mihai Cornel\n Realised by mhcrnl(c)copyright noi2021"
        la = tk.Label(ad,text=txt,foreground='blue')
        la.pack()

    #### ================================================================
    ### Clear popup menu function
    #### ===============================================================
    def clear(self):
        sel=self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)

    #### ===========================================================
    ### Paste popup menu function
    #### ===========================================================
    def paste(self):
        try:
            teext=self.text_area.selection_get(selection='CLIPBOARD')
            self.text_area.insert(tk.INSERT,teext)
        except:
            showerror('ERROR',"Your can't paste something ")
        

    #### ========================================================
    ### Create popup menu
    #### ========================================================
    def createPopup(self):
        self.popup = tk.Menu(self.parent, tearoff=0, bd=5)
        self.popup.add_command(label='Copy', command=self.copy)
        self.popup.add_command(label="Paste", command=self.paste)
        self.popup.add_command(label="Clear", command=self.clear)

    #### =========================================================
    ### Display popup menu
    #### =========================================================
    def doPopup(self, event):
        try:
            self.popup.tk_popup(event.x_root, event.y_root)
        finally:
            self.popup.grab_release()
        
    #### =========================================================
    ### Copy function in clipboard
    #### =========================================================
    def copy(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())
    

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
        data = time.asctime(time.localtime(time.time()))# datetime.date.today()
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
