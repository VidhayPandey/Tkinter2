from tkinter import *


root = Tk()
root.title("Account Login App")
root.geometry('400x400')

frame = Frame(master=root, height=250, width=360, bg="#3275D2")

lb1 = Label(frame,text = "Full name or name", bg="#2B23C5",fg='white', width=12)
lb2 = Label(frame,text = "Email Id", bg="#2B23C5",fg='white', width=12)
lb3 = Label(frame,text = "Password", bg="#2B23C5",fg='white', width=12)
lb4 = Label(frame,text = "Date of birth", bg="#2B23C5",fg='white', width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame, show="*")
DOB_entry = Entry(frame)

def display():
    name = name_entry.get()
    greet = "Hey "+ name
    message= "\nCongratulations for your new account!!!!!!"
    textbox.insert(END,greet)
    textbox.insert(END, message)

textbox = Text(bg="#11CD3C", fg="black")

btn = Button(text= "Create Account", command=display, bg="green")

frame.place(x=20,y=0)
lb1.place(x=20,y=20)
name_entry.place(x=150,y=20)

lb2.place(x=20,y=80)
email_entry.place(x=150,y=80)

lb3.place(x=20,y=140)
password_entry.place(x=150,y=140)

lb4.place(x=20,y=200)
DOB_entry.place(x=150,y=200)

btn.place(x=130,y=260)
textbox.place(y=300)

root.mainloop()
