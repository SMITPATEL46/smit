from tkinter  import*
import tkinter.messagebox
parent=Tk()

l1=Label(parent,text='name').place(x=30,y=50)
l2=Label(parent,text='city').place(x=30,y=90)
e1=Entry(parent,width=20).place(x=130,y=50)
e2=Entry(parent,width=20).place(x=130,y=90)

def click():
    tkinter.messagebox.showinfo("hello","doon")
b=Button(parent,width=10,text='click',background='yellow',command=click).place(x=180,y=140)

checkvar1=IntVar()
checkvar2=IntVar()
checkvar3=IntVar()
cb1=Checkbutton(text='c',variable=checkvar3)
cb2=Checkbutton(text='c++',variable=checkvar2)
cb3=Checkbutton(text='c#',variable=checkvar1)

cb1.pack()
cb2.pack()
cb3.pack()

parent.mainloop()