import tkinter as tk
from tkinter import ttk
import tkinter
import PIL
from PIL import Image, ImageTk
import os.path
import sys
import os
directory = os.path.dirname(os.path.abspath(__file__)) 
filename = os.path.join(directory, 'iro.png')
root = tk.Tk()
window = tkinter.Canvas(root, height=400, width=400,background='#AA0505')
w = tkinter.Label(window, text="Hello, world!")
w

style = ttk.Style()

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
#All Code regarding window and tab changes have been copied from stackoverflow
def move_window(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

root.overrideredirect(True) # turns off title bar, geometry
title_bar = ttk.Frame(root, relief='raised')
close_button = tkinter.Button(title_bar, text='X', command=root.destroy,relief="ridge" )

# a canvas for the main area of the window

root.title("Avengers Test")
root.configure(background="#AA0505")
root.geometry("750x750")
title_bar.pack(expand=0, fill="x")
title_bar.config()
close_button.pack(anchor='ne')
total = tk.IntVar()  # defaults to 0
var = tk.IntVar()
def scoredown():
    total.get()
    total.set(total.get()-1) 
        
def scoreup():
    total.get()
    total.set(total.get()+1)
    
           
                  

                                
                                              
  
mygreen = "#AA0505"
myred = "#FBCA03"
#style elements are copied from https://stackoverflow.com/questions/23038356/change-color-of-tab-header-in-ttk-notebook

style.theme_create( "yummy", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] }, "padding": [10, 1]},
        "TNotebook.Tab": {
            "configure": {"padding": [5, 5], "background": mygreen },
            "map":       {"background": [("selected", myred)],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )

style.theme_use("yummy")

note = ttk.Notebook(root)


#Introduction of Quiz
f1 = ttk.Frame(note, width=300, height=200)
note.add(f1, text = 'Intro')
ew=tkinter.Label(f1, font='helveltica', text="Iron Man is a popular character, and many ppl do not know much about him")
e2w=tkinter.Label(f1, font='helveltica', text="We made this quiz to bring awareness to Iron Man")

ew.grid(row=1, column=0, sticky=tkinter.W)
e2w.grid(row=2, column=0, sticky=tkinter.W)




f2 = ttk.Frame(note, width=300, height=200)
note.add(f2, text = 'Q1')
note.pack(expand=1, fill='both', padx=5, pady=5)
e=tkinter.Scale(f2, from_=1, to=10,label='How much do you like Iron Man?',command=scoreup)
e.grid(row=1, column=0, sticky=tkinter.W)

f3 = ttk.Frame(note,width=300, height=200)
note.add(f3, text='Q2')
a=tkinter.Label(f3, font='helveltica', text="What year was the Iron Man Movie made?")
a.grid(row=1, column = 1)

x=tkinter.Button(f3, text="2008", command = scoreup)
x.grid(row=2, column = 1)
b=tkinter.Button(f3, text="2010",command=scoredown)
b.grid(row=3, column=1)
c=tkinter.Button(f3, text="2006", command=scoredown)
c.grid(row=4, column=1) 

f4 = ttk.Frame(note,width=300, height=200)
note.add(f4, text='Q3')
f=tkinter.Label(f4, font='helveltica', text="What is Tony Stark's profession?")
f.grid(row=1, column = 1)
t=tkinter.Button(f4, text="Weapons Dealer", command = scoreup)
t.grid(row=2, column = 1)
q=tkinter.Button(f4, text="Playboy",command=scoredown)
q.grid(row=3, column=1)
o=tkinter.Button(f4, text="Warlord", command=scoredown)
o.grid(row=4, column=1) 

page5=ttk.Frame(note,width=300, height=200)
note.add(page5, text='Q4')
R0=tkinter.Label(page5, font='helveltica', text="What is Tony Stark's age?")
R0.grid(row=1, column = 1)
R1 = tkinter.Radiobutton(page5, text="45", value=1,
                  command=scoredown )
R1.grid(row=2, column =1)

R2 = tkinter.Radiobutton(page5, text="42", value=2,
                  command=scoredown)
R2.grid(row=3, column=1)

R3 = tkinter.Radiobutton(page5, text="48", value=3,
                  command=scoreup)
R3.grid(row=4, column=1)

f6=ttk.Frame(note,width=300, height=200)
note.add(f6, text='Q5')
R0=tkinter.Label(f6, font='helveltica', text="How many suits does Tony Stark own?")
R0.grid(row=1, column = 1)
R = tkinter.Radiobutton(f6, text="102", value=1,
                  command=scoredown )
R.grid(row=2, column =1)

R23 = tkinter.Radiobutton(f6, text="42", value=2,
                  command=scoredown)
R23.grid(row=3, column=1)

R333 = tkinter.Radiobutton(f6, text="49", value=3,
                  command=scoreup)
R333.grid(row=4, column=1)

f7 = ttk.Frame(note,width=300, height=200)
R0=tkinter.Label(f7, font='helveltica', text="How many movies has Iron Man been in?")
R0.grid(row=1, column = 1)
Re = tkinter.Radiobutton(f7, text="7", value=1,
                  command=scoreup )
Re.grid(row=2, column =1)

R2e3 = tkinter.Radiobutton(f7, text="16", value=2,
                  command=scoredown)
R2e3.grid(row=3, column=1)

R33e3 = tkinter.Radiobutton(f7, text="21", value=3,
                  command=scoredown)
R33e3.grid(row=4, column=1)

Total=ttk.Frame(note,width=300, height=200)
note.add(Total, text='TotalScore')
tkinter.Label(Total, text="Total/4:").pack()
tkinter.Label(Total, textvariable=total).pack()
tkinter.Button(Total, text="Restart", command=restart_program).pack()
root.mainloop()
