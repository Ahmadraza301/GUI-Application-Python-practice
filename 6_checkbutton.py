from tkinter import*
root=Tk()
root.title("GUI COURSE")
root.geometry("700x500+200+80")
root.resizable()
root.config(bg="#F0F0F8")
def get_data():
    print(check_var.get())
check_var=IntVar()
check=Checkbutton(root, text="accept?not", onvalue=1, offvalue=0, variable=check_var, font=("times new roman", 25, "bold")).place(x=200, y=150)
btn=Button(root, text="show", font=("times new roman ", 25, "bold"), bg="lightyellow", command=get_data).place(x=200, y=100, width=100, height=50)

root.mainloop()