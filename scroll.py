from tkinter import*
root=Tk()
root.title("GUI COURSE")
root.geometry("800x500+200+80")
root.resizable()
root.config(bg="#F0F0F8")

frame1=Frame(root, bd=2, relief=RIDGE)
frame1.place(x=250, y=50, width=250, height=300)

scrolly=Scrollbar(frame1, orient=VERTICAL)
scrolly.pack(side=RIGHT, fill=Y)

data=Listbox(frame1, font=("times new roman", 20), justify=CENTER, yscrollcommand=scrolly.set)

data.pack()
scrolly.config(command=data.yview)

for i in range (0, 101):
    data.insert(i, "Number " +str(i))






root.mainloop()