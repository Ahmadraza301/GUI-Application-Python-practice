from tkinter import*
from tkinter import messagebox
#from tkinter import Menubutton
root=Tk()
root.title("GUI COURSE")
root.geometry("800x500+250+50")
root.config(bg="#F0F0F8")

def employedetails():
    messagebox.showinfo("employemenu", "this is show employee  menubar")
    

mymenu=Menu(root)

mymenu.add_command(label="employee", command=employedetails())
mymenu.add_command(label="employee", command=employedetails())
mymenu.add_command(label="employee", command=employedetails())
mymenu.add_command(label="employee", command=employedetails())

root.config(Menu=mymenu)








root.mainloop()