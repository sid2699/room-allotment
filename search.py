import os
import csv
import sys
import random
from tkinter import *
from tkinter import messagebox

def searchname():

      flag=0
      with open("db.csv") as f:
          read=csv.reader(f)
          for row in read:
              if row[1]==val_searchid.get():

                  dname=Label(root,text="Adhar No.",bg='black',fg='yellow').place(x=300,y=100)
                  dauthor=Label(root,text="First name",bg='black',fg='yellow').place(x=400,y=100)
                  did=Label(root,text="Last name",bg='black',fg='yellow').place(x=500,y=100)
                  dprice=Label(root,text="Gender",bg='black',fg='yellow').place(x=650,y=100)

                  ldval_id=Label(root,text=row[0]).place(x=300,y=150)
                  ldval_name=Label(root,text=row[1]).place(x=400,y=150)
                  ldval_pointer=Label(root,text=row[2]).place(x=500,y=150)
                  ldval_city=Label(root,text=row[3]).place(x=650,y=150)

                  flag=1
          if flag==0:
              messagebox.showinfo("ERROR","CUSTOMER NOT FOUND")

def searchaadhar():

      flag=0
      with open("db.csv") as f:
          read=csv.reader(f)
          for row in read:
              if row[0]==val_searchid.get():

                  dname=Label(root,text="Adhar No.",bg='black',fg='yellow').place(x=300,y=600)
                  dauthor=Label(root,text="First name",bg='black',fg='yellow').place(x=400,y=600)
                  did=Label(root,text="Last name",bg='black',fg='yellow').place(x=500,y=600)
                  dprice=Label(root,text="Gender",bg='black',fg='yellow').place(x=650,y=600)

                  ldval_id=Label(root,text=row[0]).place(x=300,y=650)
                  ldval_name=Label(root,text=row[1]).place(x=400,y=650)
                  ldval_pointer=Label(root,text=row[2]).place(x=500,y=650)
                  ldval_city=Label(root,text=row[3]).place(x=650,y=650)

                  flag=1
          if flag==0:
              messagebox.showinfo("ERROR","CUSTOMER NOT FOUND")

root=Tk()

val_name=StringVar()
val_author=StringVar()
val_id=StringVar()
val_price=StringVar()
val_searchid=StringVar()

root.geometry("900x900")
root.configure(bg='cyan')
root.title('OYO HOTELS')
canvas=Canvas(root,width=900,height=900)
canvas.pack()
mimage=PhotoImage(file='books.png')
canvas.create_image(0,0,anchor=NW,image=mimage)

lsearchid=Label(root,text="ENTER NAME :",bg='black',fg='yellow').place(x=300,y=10)
esearchid=Entry(root,textvariable=val_searchid,width=50,bd=5).place(x=450,y=250)
bsearch=Button(root,text="SEARCH",command=searchname,bg='orange',fg='white').place(x=600,y=60)

lsearchid=Label(root,text="ENTER AADHAR NUMBER :",bg='black',fg='yellow').place(x=300,y=400)
esearchid=Entry(root,textvariable=val_searchid,width=50,bd=5).place(x=450,y=250)
bsearch=Button(root,text="SEARCH",command=searchaadhar,bg='orange',fg='white').place(x=600,y=450)

root.mainloop()
