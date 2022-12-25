from tkinter import*
root=Tk()
root.title("GUI COURSE")
root.geometry("600x350+200+50")
root.resizable(width=False, height=False)
root.config(bg="#F0F0F8")

lbl_title=Label(root, text="Title", font=("time new roman",30, "bold"),bg="lightyellow", fg="red").place(x=0, y=0, relwidth=1)
Text_entry=Entry(root, font=("time new roman",10, "bold"),bg="white", fg="black", bd=5, relief=GROOVE).place(x=0,y=60,relwidth=1)

root.mainloop()