import csv
from tkinter import*
from tkinter import messagebox
def Hello():
    import csv
    with open('db.csv','a',newline='') as f:
        write=csv.writer(f)
        write.writerow([adhar.get(),Fname.get(),Lname.get(),contact.get(),loc.get()])
    with open('db.csv','r') as f:
        read=csv.reader(f)
        for row in read:
            print(row)

root = Tk()
root.title("Room Management System")

Tops = Frame(root,bg="white",width = 1600,height=50)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700)
f2.pack(side=RIGHT)

#TOP
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Room Management System",fg="steel blue",bd=10)
lblinfo.grid(row=0,column=0)
messagebox.showinfo("Hello", "Welcome to our hotel")

def qexit():
    root.destroy()

def reset():
    adhar.set("")
    Fname.set("")
    Lname.set("")
    contact.set("")
    loc.set("")


adhar = StringVar()
Fname = StringVar()
Lname = StringVar()
gender = StringVar()
contact = StringVar()
loc = StringVar()

lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Adhar No.",fg="steel blue",bd=10)
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=adhar , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtreference.grid(row=0,column=1)

lblfname = Label(f1, font=( 'aria' ,16, 'bold' ),text="First name",fg="steel blue",bd=10)
lblfname.grid(row=1,column=0)
txtfname = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fname , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtfname.grid(row=1,column=1)

lblLname = Label(f1, font=( 'aria' ,16, 'bold' ),text="Last name",fg="steel blue",bd=10)
lblLname.grid(row=2,column=0)
txtLname = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Lname , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtLname.grid(row=2,column=1)


lblgender = Label(f1, font=( 'aria' ,16, 'bold' ),text="Gender",fg="steel blue",bd=10)
lblgender.grid(row=3,column=0)

var = IntVar()
R1 = Radiobutton(f1,font=( 'aria' ,16, 'bold' ), text="MALE", variable=var, value=1) 
R1.place(x=320,y=170)
R2 = Radiobutton(f1,font=( 'aria' ,16, 'bold' ), text="FEMALE", variable=var, value=2) 
R2.place(x=180,y=170)


lblcontact = Label(f1, font=( 'aria' ,16, 'bold' ),text="contact no.",fg="steel blue",bd=10)
lblcontact.grid(row=4,column=0)
txtcontact = Entry(f1,font=('ariel' ,16,'bold'), textvariable=contact , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtcontact.grid(row=4,column=1)

lblloc = Label(f1, font=( 'aria' ,16, 'bold' ),text="location",fg="steel blue",bd=10)
lblloc.grid(row=5,column=0)
txtloc = Entry(f1,font=('ariel' ,16,'bold'), textvariable=loc , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtloc.grid(row=5,column=1)


#--buttons--
btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="SUBMIT", bg="green",command=Hello)
btnTotal.grid(row=8, column=0)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="orange",command=reset)
btnreset.grid(row=8, column=3)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="red",command=qexit)
btnexit.grid(row=8, column=4)

lbl = Label(f1, font=( 'aria' ,16, 'bold' ),text="",bd=10)
lbl.grid(row=7,column=0)


def price():
    roo = Tk()
    roo.title("details")

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ROOM NO.", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="__200__" , fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="BED", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="3", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="FAN", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="2", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Meal CHARGES", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="200", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="TOTAL PRICE     ", fg="black", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="  400 for month", fg="black", anchor=W)
    lblinfo.grid(row=4, column=3)

    roo.mainloop()

def partners():
    roo = Tk()
    roo.title("partners")
    lblinfo = Label(roo, font=('aria', 12, 'bold'), text="ROOM PARTNERS", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 12,'bold'), text="  BALANCE" , fg="black")
    lblinfo.grid(row=0, column=3)

    lblinfo = Label(roo, font=('aria', 10, 'bold'), text="VIshwa", fg="steel blue")
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 10, 'bold'), text="paid", fg="green")
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 10, 'bold'), text="Aditi", fg="steel blue")
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 10, 'bold'), text="100 remaining", fg="orange")
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 10, 'bold'), text="rehan", fg="steel blue")
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 10, 'bold'), text="paid", fg="green")
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 10, 'bold'), text="niraj", fg="steel blue")
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 10, 'bold'), text=" not paid", fg="red")
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 10, 'bold'), text="deepak", fg="steel blue")
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 10, 'bold'), text="not paid", fg="red")
    lblinfo.grid(row=5, column=3)
    import csv
    with open('db.csv','r') as f:
        read=csv.reader(f)
        for row in read:
            print(row)

    canvas = Canvas(roo, width=300, height = 300)
    canvas.pack()

    img = PhotoImage(file='C:\\Desktop\\pic.png')
    canvas.create_image(20,20,image=img)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="ROOM-DETAILS", bg="blue",command=price)
btnprice.grid(row=2, column=4)
#btnpartners=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PARTNERS", bg="blue",command=partners)
#btnpartners.grid(row=3, column=4)

root.mainloop()
