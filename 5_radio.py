from tkinter import*
root=Tk()
root.title("GUI COURSE")
root.geometry("400x500+200+80")
root.resizable()
root.config(bg="#F0F0F8")
gender=Label(root, text="select gender:", font=("times new roman ", 20, "bold"), bg="#262626", fg="white").place(x=100, y=50)


def gender_funct():
    print(gender.get())
gender=StringVar()
Male=Radiobutton(root, text="Male", value="Male", font=("times new roman", 18, "bold") ).place(x=300, y=50)
Female=Radiobutton(root, text="Female", value="female", font=("times new roman", 18, "bold")).place(x=400, y=50)
gender.set("Male")
btn=Button(root, text="show", font=("times new roman ", 25, "bold"), command=gender_funct, bg="lightyellow").place(x=300, y=100, width=150, height=50)

root.mainloop()

