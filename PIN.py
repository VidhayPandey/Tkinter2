from tkinter import *

root = Tk()
root.title("ATM PIN SETUP")
root.geometry("400x500")

frame = Frame(master=root, height=250, width=360, bg="#3F65D9")

lb1 = Label(frame,text = "Password", bg="#2B23C5",fg='white', width=12)
lb2= Label(frame,text = "Email Id", bg="#2B23C5",fg='white', width=12)
lb3= Label(frame,text = "Legal Name", bg="#2B23C5",fg='white', width=12)

PIN_entry = Entry(frame)
email_entry = Entry(frame)
name_entry = Entry(frame)


def display():
    name= name_entry.get()
    greet = "Hey "+ name
    greet = "Be aware to not share your password!"
    message= "\nYour account with PIN is created. Congratulations!!!"
    textbox.insert(END,greet)
    textbox.insert(END, message)

textbox = Text(bg="#11CD3C", fg="black")

btn = Button(text= "Create your Account", command=display, bg="green")

frame.place(x=20,y=0)
lb1.place(x=20,y=20)
PIN_entry.place(x=150,y=20)

lb2.place(x=20,y=80)
email_entry.place(x=150,y=80)

btn.place(x=130,y=260)
textbox.place(y=300)

root.mainloop()
