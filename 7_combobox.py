from tkinter import*
from tkinter import ttk 
root=Tk()
root.title("GUI COURSE")
root.geometry("800x500+250+50")
root.resizable()
root.config(bg="#F0F0F8")
def get_data():
    print(language.get())
language=ttk.Combobox(root, values=("select languages ", "python", "html", "css", "javascript", "django", "php"), font=("times new roman ", 20, "bold", ), justify="center", state="readonly").place(x=100, y=50, width=200, height=40)
language.Place(x=100, y=50, Width=200, height=40)
language.set("select languages")

btn=Button(root, text="show", command=get_data()).place(x=50, y=200)












root.mainloop()