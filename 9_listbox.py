from tkinter import*
root=Tk()
root.title("GUI COURSE")
root.geometry("800x500+250+50")
root.resizable()
root.config(bg="#F0F0F8")

def get_language():
    get_cursor=language_list.curselection()
    #print(language_list.get(0))
    print(get_cursor)
    for i in get_cursor:
        print(language_list.get(i))
    
language_list=Listbox(root, font=("times new roman", 15), bg="#008000", fg="white", justify="center", selectmode=EXTENDED)
language_list.place(x=100, y=50)

btn=Button(root, text="show", command=get_language, font=("times new roman", 20), bg="green", fg="white").place(x=120, y=300, height=40)

for i in range(0, 20):
    language_list.insert(i, "language: "+str(i))


root.mainloop()