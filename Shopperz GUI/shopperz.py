from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image

def continue_log():
    email=email_phone.get()
    #print(email)
    if email == "devottam2809@gmail.com":
        from email_log import otp
        otp()
    else:
        from email_log import wrong_access
        wrong_access()

def new_acc():
    from newuser import newu
    newu()

root=Tk()
root.title("Shopperz")

root.minsize(600,600)

root.iconbitmap("favicon.ico")

root.config(background="pink")

bd_image=Image.open("shop.jpg")
resized_img=bd_image.resize((550,200))
img=ImageTk.PhotoImage(resized_img)
img_label=Label(root,image=img)
img_label.pack(pady=(10,10))

text_label=Label(root,text="Sign in",fg="purple",bg="pink")
text_label.pack()
text_label.config(font=('broadway',30))

text_label=Label(root,text="email or phone number",fg="purple",bg="pink")
text_label.pack()
text_label.config(font=('Times New Roman',15))

email_phone=Entry(root,width=50)
email_phone.pack(ipady=4,pady=(1,15))

login_btn=Button(root,text="Continue",bg="purple",fg="white",width=30,height=3,command=continue_log)
login_btn.pack(pady=(10,20))
login_btn.config(font=("verdana",10))

text_label=Label(root,text="By continuing, you agree to Shopperz Conditions of Use and Privacy Notice.",fg="purple",bg="pink")
text_label.pack()
text_label.config(font=('Times New Roman',12))

text_label=Label(root,text=" ",bg="pink")
text_label.pack()
text_label=Label(root,text=" ",bg="pink")
text_label.pack()

text_label=Label(root,text="--------------------New to Shopperz ?-------------------",fg="purple",bg="pink")
text_label.pack()
text_label.config(font=('Times New Roman',15))

login_btn=Button(root,text=" Create your Shopperz Account ",bg="purple",fg="white",width=40,height=1,command=new_acc)
login_btn.pack(pady=(10,20))
login_btn.config(font=("verdana",10))

text_label=Label(root,text=" ",bg="pink")
text_label.pack()
text_label=Label(root,text=" ",bg="pink")
text_label.pack()

text_label=Label(root,text="-----------------------------------------------------------------------------------------------------------------------------------------------",fg="purple",bg="pink")
text_label.pack()
text_label.config(font=('Times New Roman',15))

text_label=Label(root,text=" Conditions of Use      Privacy Notice      Help ",fg="purple",bg="pink")
text_label.pack()
text_label.config(font=('Times New Roman',10))

root.mainloop()