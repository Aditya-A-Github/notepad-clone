import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def chCol():
    c = colorchooser.askcolor(title="Font color")
    ta.config(fg=c[1])

def chFont(*args):
    ta.config(font=(fontname.get(), sizebox.get()))

def newfile():
    w.title("Untitled")
    ta.delete(1.0, END)

def openfile():
    file = askopenfilename(defaultextension=".txt",
                           file=[("All Files", "*.*"),
                                 ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            w.title(os.path.basename(file))
            ta.delete(1.0, END)

            file = open(file, "r")

            ta.insert(1.0, file.read())

        except Exception:
            print("couldn't read file")

        finally:
            file.close()

def savefile():
    file = filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt',
                filetypes=[("All files", '*.*'),
                ("Text Documents", '*.txt')
                ]
            )
        
    if file is None:
        return
    
    else:
        try:
            w.title(os.path.basename(file))
            file = open(file, 'w')

            file.write(ta.get(1.0, END))
        
        except Exception:
            showerror("Error", "Couldn't save file")
        finally:
            file.close()

def cut():
    ta.event_generate("<<Cut>>")

def paste():
    ta.event_generate("<<Paste>>")

def copy():
    ta.event_generate("<<Copy>>")

def abt():
    showinfo("About", "This is a notepad app made by Aditya A")

def quit():
    w.destroy()

w = Tk()
w.title("Notepad")
file = None
w.geometry("500x500")

fontname = StringVar(w)
fontname.set("Arial")

fontsize = StringVar(w)
fontsize.set("25")

ta = Text(w, font=(fontname.get(), fontsize.get()))

scroll = Scrollbar(ta)
w.grid_rowconfigure(0, weight=1)
w.grid_columnconfigure(0, weight=1)
ta.grid(sticky=N + E + S + W)

f = Frame(w)
f.grid()

colb = Button(f, text="Color", command=chCol)
colb.grid(row=0, column=0)

fontbox = OptionMenu(f, fontname, *font.families(), command=chFont)
fontbox.grid(row=0, column=1)

sizebox = Spinbox(f, from_=1, to=100, textvariable=fontsize, command=chFont)
sizebox.grid(row=0, column=2)

scroll.pack(side=RIGHT, fill=Y)
ta.config(yscrollcommand=scroll.set)

menu = Menu(w)
w.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New", command=newfile)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)

editm = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=editm)
editm.add_command(label="Cut", command=cut)
editm.add_command(label="Copy", command=copy)
editm.add_command(label="Paste", command=paste)

help = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=help)
help.add_command(label="About", command=abt)

w.mainloop()
