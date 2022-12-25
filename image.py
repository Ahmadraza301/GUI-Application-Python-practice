from tkinter import*
root=Tk()
root.title("GUI COURSE")
root.geometry("1000x600+200+80")
root.resizable()
root.config(bg="#F0F0F8")

icon=PhotoImage(file="images/1828.png_300.png")
lbl_image=Label(root, text="username", image=icon, compound=RIGHT).place(x=50, y=50, height=200, width=300)






root.mainloop()