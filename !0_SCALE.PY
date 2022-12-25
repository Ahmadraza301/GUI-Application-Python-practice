from tkinter import*
root=Tk()
root.title("GUI COURSE")
root.geometry("800x500+250+50")
root.resizable()
root.config(bg="lightyellow")

price=Scale(root, from_=50, to=250, orient=HORIZONTAL, sliderlength=100, length=700, showvalue=False)
price.place(x=50, y=50)

lbl_result=Label(root, bg="" )
lbl_result.place(x=0, y=250, relwidth=1)

root.mainloop()