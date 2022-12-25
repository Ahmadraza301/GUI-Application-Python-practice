from tkinter import*
root=Tk()
root.title("GUI COURSE")
root.geometry("800x500+250+50")
root.resizable()
root.config(bg="#F0F0F8")
title=Label(root, text="User registration form ", font=("impact", 30), bg="#262626", fg="white").place(x=0, y=0, relwidth=1)

def get_data():
    if var_check==1:

        result="username: " +var_username.get()+"\t email:" +var_email.get()+"\t gender"+var_gender.get
        lbl_result.config(text=str(result))
    else:
        lbl_result.config(text="please accept the terms and conditions ")
lbl_username=Label(root, text="USERNAME", font=("times new roman ", 20)).place(x=50, y=100)
lbl_email=Label(root, text="EMAIL", font=("times new roman ", 20)).place(x=50, y=180)
lbl_gender=Label(root, text="GENDER", font=("times new roman ", 20)).place(x=50, y=260)

var_username=StringVar()
var_email=StringVar()
var_gender=StringVar()
var_check=IntVar()

text_username=Entry(root, textvariable=var_username, font=("times new roman ", 20)).place(x=250, y=100, width=400, height=40)
text_email=Entry(root, textvariable=var_email, font=("times new roman ", 20)).place(x=250, y=180, width=400, height=40)
male=Radiobutton(root, text="Male", value="male",  variable=var_gender, font=("times new roman ", 20)).place(x=250, y=260)
female=Radiobutton(root, text="Female", value="female", variable=var_gender, font=("times new roman " ,20)).place(x=350, y=260)
var_gender.set("male")
check_=Checkbutton(root, text="Accept our Terms & Conditions", onvalue=1, offvalue=0, variable=var_check, font=("times in roman", 15)).place(x=250, y=340)

btn=Button(root, text="show data", command=get_data, font=("times new roman ", 15, "bold"), bg="grey", fg="white").place(x=250, y=400, width=110, height=60)
def new_func(root):
    lbl_result=Label(root, font=("times in roman", 20)).place(x=0, y=450)





root.mainloop()