from tkinter import *
import random
import tkinter.messagebox as msg
def hel():
  c=Label(text={var.get(),car.get()})
  c.pack()
root=Tk()
var=DoubleVar()
car=DoubleVar()
var.set(60)
root.geometry("900x400")
lc=LabelFrame(root,text="hello g",fg="orange")
lc.pack()
sc=Scale(root,variable=var,from_=0,to=200,bg='orange')
sc.pack(anchor="nw",side=RIGHT)
app=Spinbox(root,from_=0,to=100,textvariable=car)

app.pack()
but=Button(root,text="click me",command=hel)
but.pack()
root.mainloop()
