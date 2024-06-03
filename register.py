from tkinter import*
import tkinter.messagebox
p=Tk()
l1=Label(p,text='name').place(x=30,y=50)
l2=Label(p,text='mobile').place(x=30,y=90)
l3=Label(p,text='address').place(x=30,y=130)
e1=Entry(p,width=20).place(x=100,y=50)
e2=Entry(p,width=20).place(x=100,y=90)
e3=Entry(p,width=20).place(x=100,y=130)


def d():
    tkinter.messagebox.showinfo("message","submited")
b1=Button(p,text='submit',width=10,background='yellow',command=d).place(x=100,y=170)



tkinter.mainloop()