from tkinter import*
root=Tk()
root.title("GUI COURSE")
root.geometry("400x500+700+50")
root.config(bg="#008000")
root.resizable()

lbl_title=Label(root, text="Title", font=("time new roman",30, "bold"),bg="lightyellow", fg="red").pack(fill=X)

lbl_title=Label(root, text="Abdullah the chutiya", font=("time new roman",20, "italic"),bg="white", fg="black", pady=30, bd=10, relief=RAISED).pack(fill=X, pady=5, padx=10)

lbl_title=Label(root, text="Raza", font=("time new roman",21, "bold"),bg="white", fg="black").place(x=150, y=300, height=100, width=200)

root.mainloop()
