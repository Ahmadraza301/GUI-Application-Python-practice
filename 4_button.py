from tkinter import*
root=Tk()
root.title("GUI COURSE")
root.geometry("400x500+700+80")
root.resizable()
root.config(bg="#F0F0F8")
def get_name(): 
    #print(Text_entry.get())
    lbl_result.config(text=str(Text_entry.get()))

var_text=StringVar()


lbl_title=Label(root, text="Title", font=("time new roman",30, "bold"),bg="lightyellow", fg="red").place(x=0, y=0, relwidth=1)
Text_entry=Entry(root, font=("time new roman",10, "bold"),bg="white", fg="black", textvariable=var_text, bd=5, relief=GROOVE).place(x=0,y=60,relwidth=1)

btn_get=Button(root, text="show", font=("time new roman",40, "bold"),bg="grey", fg="white", activebackground="grey", cursor="hand2").place(x=100, y=100, width=150, height=70)
address=Text(root).place(x=50, y=200, width=400, height=200)
lbl_result=Label(root, font=("time new roman",15, "bold"),bg="lightyellow", fg="red")
lbl_result.place(x=0, y=20, relwidth=1)

root.mainloop()