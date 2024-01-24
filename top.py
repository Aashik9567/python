from tkinter import *
import random
import tkinter.messagebox as msg
from PIL import Image,ImageTk
def login():
  root.destroy()
  if var.get()=='aashiq' and var1.get()=='aashiq' :
     pls=Tk()
     pls.title('hello aashiq')
     pls.geometry("1000x500")
    # lab=Label(pls,text="welcome",font="comicsansm 20 bold",fg='orange',bg='white')
    #lab.place(x=50,y=32)
     scroll =Scrollbar(pls)
     scroll.pack(side=RIGHT,fill=Y)
     list=Listbox(pls,yscrollcommand=Scrollbar.set,height=500)
     for i in range(4):
         list.insert(END,f"number is {random.randint(0,500)}")
     list.pack(fill="right",padx=50,pady='50')
     Scrollbar.config(command=list.yview)
    
  else:
    msg.showerror("error","invalid username and password") 
#def helo():
    pls.mainloop()
root=Tk()
var=StringVar()
var1=StringVar()
root.title("GUI page")
root.geometry("1000x500")
root.resizable(False,False)
image=Image.open("login.jpg")
img=ImageTk.PhotoImage(image)
#im=img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
label=Label(root,image=img)
label.place(x=0,y=0)

frame=Frame(root,bg='orange',borderwidth=2,width=450,height=450).place(x=520,y=0)
a1=Label(frame,text="USERNAME",font="comicsanms 20 bold",fg='red').place(x=550,y=50)
a2=Label(frame,text="PASSWORD",font="comicsanms 20 bold",fg='red').place(x=550,y=150)
e1=Entry(frame,textvariable=var,borderwidth=2).place(x=550,y=100)
e2=Entry(frame,textvariable=var1,borderwidth=2,show="*").place(x=550,y=200)
button=Button(frame,text="login ",font="comicsanms 20 bold",fg='cyan',borderwidth=3,command=login).place(x=550,y=250)

#print(f"{var1},{var}")
#with open("listed.txt","a") as f:
  #f.write(f"username {var.get()} and password is{var1.get()}\n")
root.mainloon()