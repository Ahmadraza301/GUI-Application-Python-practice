from tkinter import*
root=Tk()
root.title("GUI COURSE")
root.geometry("400x500+700+80")
root.resizable()
root.config(bg="#F0F0F8")
def show_data():
    var_data.set(str(text_field.get('1.0', END)))
    print(var_data.get())

var_data=StringVar()
text_field=Text(root)
text_field.place(x=50, y=200, width=400, height=150)

btn_get=Button(root, text="show", font=("time new roman",25, "bold"),bg="grey", fg="white", activebackground="grey", cursor="hand2", command=show_data).place(x=100, y=100, width=150, height=70)


root.mainloop()