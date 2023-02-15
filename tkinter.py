from tkinter import *
import random
from PIL import Image, ImageTk

# Create a Tkinter window
root = Tk()
root.title("GUI AASHIQ")
def hey():
    hello=random.randint(0,100)
    print("welcome",hello)
    c1=Label(text="welcome to hey function",font='sfmono 18 italic',bg='brown')
    c1.pack()
con=Frame(root,bg='cyan', borderwidth=8,relief=GROOVE)
con.pack(side=LEFT)
re=Label(con,text='ready',font='sfmono 18 italic',bg='brown')
re.pack(side=BOTTOM,anchor='ne')
a1=Button(con,fg='red',font='arial',bg='blue',text="LOGIN/SIGNUP",command=hey)
a1.pack(side=BOTTOM,padx=25)

# Open the image using PIL
img = Image.open("spidy.png")

# Create a PhotoImage object from the image
img = ImageTk.PhotoImage(img)

# Create a label to display the image
label = Label(root, image=img)
label.pack()
sty= Label(text="WELCOME TO MY GUI PAGE \nHELLO ITS ME AASHIQ ", bg='green'
, fg='cyan',padx=50,pady=50,borderwidth=10,relief=GROOVE,font="sfmono,16,bold" )

sty.pack(side=BOTTOM,anchor='nw',fill=X)

# Start the main event loop
root.mainloop()
