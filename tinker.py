from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
import sqlite3

'''def printt():
    first=fn.get()
    last=pn.get()
    dob=dn.get()
    var1=var.get()
    rad=rad_var1.get()
    var3=var_c1
    var3=var_c2    
    
    print("Hello ", end="")
    print(first, end=" ")
    print(last)
    print("Your Date of Birth is ", end="")
    print(dob)
    print("Your country is ", end="")
    print(var1)
    print("Your preffered programming Language is ", end="")
    print(var3)
    print("Your gender is ", end="")
    print(rad)    
    print("Registeration Successfu!l")
    tkinter.messagebox.showinfo("Welcome", 'Registeration was successful')
 '''   
def exit1():
    window.destroy()
    
def abt():
    tkinter.messagebox.showinfo("Author's Quest", "This is a beta version") 
    
def new_win():
    root=Tk()
    root.geometry("250x300")
    root.title('Login Page')
    l1=Label(root,text='This is Login Page. Click exit').pack()
    b1=Button(root, text="Exit", command=abt).pack()
def database():
    first=fn.get()
    last=pn.get()
    dob=dn.get()
    var1=var.get()
    rad=rad_var1.get()
    var3=var_c1
    var3=var_c2
    conn=sqlite3.connect("Form.db")
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Student (Name TEXT, Last TEXT, DOB TEXT, Country TEXT, Language TEXT, Gender TEXT)')
    cursor.execute('INSERT INTO Student (Name, last, DOB, Country, Language, Gender) VALUES (?, ?, ?, ?, ?, ?)',(first, last, dob,var1, rad, var3))
    conn.commit()
window=Tk()
fn=StringVar()
pn=StringVar()
dn=StringVar()
var=StringVar()
var_c1="Python"
var_c2="Java"
rad_var1=StringVar()


window.title("Registeration Form")
window.geometry("500x500")
img=Image.open(r'C:\Users\sanje\Desktop\RG\VTC\board_pic1.jpg')
photo=ImageTk.PhotoImage(img)

menu=Menu(window)
window.config(menu=menu)
sub_menu1=Menu(menu)
sub_menu2=Menu(menu)

menu.add_cascade(label="File", menu=sub_menu1)
sub_menu1.add_command(label="Exit", command=exit1)

menu.add_cascade(label="Option", menu=sub_menu2)
sub_menu2.add_command(label="About", command=abt)

lab=Label(image=photo, height=150, width=150).pack()
label1=Label(window, text="Registeration Form", relief="solid", font=("Arial Bold", 20 ,"bold")).pack()

label2=Label(window, text="First Name", font=("arial", 15))
label2.place(x=80,y=220)

entry1=Entry(window,textvar=fn)
entry1.place(x=200,y=224)

label3=Label(window, text="Last Name", font=("arial", 15))
label3.place(x=80,y=250)

entry2=Entry(window, textvar=pn)
entry2.place(x=200, y=254)

label4=Label(window, text="DOB", font=("arial", 15))
label4.place(x=80,y=280)

entry3=Entry(window, textvar=dn)
entry3.place(x=200, y=284)

label5=Label(window, text="Country", font=("arial", 15))
label5.place(x=80,y=310)

List1=['Poland', 'Germany', 'India', 'Nepal']
droplist=OptionMenu(window, var, *List1)
var.set("Select Country")
droplist.config(width=15)
droplist.place(x=198, y=314)

label6=Label(window, text="Prog. Lang.", font=("arial", 15))
label6.place(x=80,y=340)
c1=Checkbutton(window, text="Python", variable=var_c1).place(x=200, y=344)
c2=Checkbutton(window, text="Java", variable=var_c2).place(x=280, y=344)

label7=Label(window, text="Gender", font=("arial", 15))
label7.place(x=80,y=380)
r1=Radiobutton(window, text="Male", variable=rad_var1, value="Male").place(x=200, y=384)
r1=Radiobutton(window, text="Female", variable=rad_var1, value="Female").place(x=250, y=384)

b1=Button(window, text="Sign Up", bg="Yellow", fg="Black",relief=GROOVE, height=3, width=10, command=database)
window.bind("<Return>", database)
b1.place(x=400, y=450)
b2=Button(window, text="Quit", bg="brown", fg="Black",relief=GROOVE, height=3, width=10, command=exit1)
b2.place(x=20, y=450)
b3=Button(window, text="Login", bg="pink", fg="Black",relief=GROOVE, height=3, width=10, command=new_win)
b3.place(x=200, y=450)

window.mainloop()