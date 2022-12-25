from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("GUI COURSE")
root.geometry("800x500+250+50")
root.resizable()
root.config(bg="#F0F0F8")

def message():
    messagebox.showerror("showError", "this is show error message box")
    
def message2():
    messagebox.showinfo("showinfo", "this is show info message box")
    
def message3():
    messagebox.showwarning("showwarning", "this is show warning message box")
    

btn1=Button(root, text="message1", command=message).place(x=50, y=50, height=50, width=100)

btn2=Button(root, text="message2", command=message2).place(x=50, y=120, height=50, width=100)

btn3=Button(root, text="message3", command=message3).place(x=50, y=190, height=50, width=100)


root.mainloop()