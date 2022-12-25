from tkinter import*
root=Tk()
root.title("GUI COURSE")
root.geometry("600x350+200+50")
root.resizable(width=False, height=False)
root.config(bg="#008000")
#-------GRID SYSTEM -------
#lbl=Label(root, text="GRID SYSTEM").grid(row=0, column=10)
#lbl=Label(root, text="GRID SYSTEM").grid(row=1, column=11)
#lbl=Label(root, text="GRID SYSTEM").grid(row=4, column=2)
#lbl=Label(root, text="GRID SYSTEM").grid(row=5, column=5)

#-------PACK SYSTEM -------
#lbl=Label(root, text="PACK1 SYSTEM").pack(side=LEFT)
#lbl=Label(root, text="PACK2 with fill SYSTEM").pack(expand=1,fill=BOTH)
#lbl=Label(root, text="PACK3 with Normal SYSTEM").pack()

#-------PLACE  SYSTEM -------
lbl=Label(root, text="PLACE1 SYSTEM").place(x=100, y=100)
lbl=Label(root, text="PLACE2 SYSTEM").place(x=200,y=200)
lbl=Label(root, text="PLACE3 SYSTEM").place(x=300, y=300)




root.mainloop()

