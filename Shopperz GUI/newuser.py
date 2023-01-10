from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image

def welcome():
    root=Tk()
    root.title("Shopperz")

    root.minsize(600,600)

    root.iconbitmap("favicon.ico")

    root.config(background="pink")

    text_label=Label(root,text=" Welcome ",fg="purple",bg="pink")
    text_label.pack()
    text_label.config(font=('broadway',30))

    text_label=Label(root,text=" To ",fg="purple",bg="pink")
    text_label.pack()
    text_label.config(font=('broadway',30))

    text_label=Label(root,text=" Shopperz ",fg="purple",bg="pink")
    text_label.pack()
    text_label.config(font=('broadway',30))
    
def newu():
    root=Tk()
    root.title("Shopperz")

    root.minsize(600,600)

    root.iconbitmap("favicon.ico")

    root.config(background="pink")

    #bd_image=Image.open("shop.jpg")
    #resized_img=bd_image.resize((550,200))
    #img=ImageTk.PhotoImage(resized_img)
    #img_label=Label(root,image=img)
    #img_label.pack(pady=(10,10))

    text_label=Label(root,text=" Create Account ",fg="purple",bg="pink")
    text_label.pack()
    text_label.config(font=('broadway',30))

    text_label=Label(root,text=" Your Name ",fg="purple",bg="pink")
    text_label.pack()
    text_label.config(font=('Times New Roman',15))

    phone=Entry(root,width=50)
    phone.pack(ipady=4,pady=(1,15))

    text_label=Label(root,text=" Mobile Number ",fg="purple",bg="pink")
    text_label.pack()
    text_label.config(font=('Times New Roman',15))

    phone=Entry(root,width=50)
    phone.pack(ipady=4,pady=(1,15))

    text_label=Label(root,text=" Password ",fg="purple",bg="pink")
    text_label.pack()
    text_label.config(font=('Times New Roman',15))

    phone=Entry(root,width=50)
    phone.pack(ipady=4,pady=(1,15))

    text_label=Label(root,text=" Passwords must be at least 6 characters. ",fg="purple",bg="pink")
    text_label.pack()
    text_label.config(font=('Times New Roman',10))

    text_label=Label(root,text="----------------------------------------------------------------",fg="purple",bg="pink")
    text_label.pack()
    text_label.config(font=('Times New Roman',15))

    text_label=Label(root,text=" By enrolling your mobile phone number, you consent to receive automated security notifications via text message from Amazon. Message and data rates may apply. ",fg="purple",bg="pink")
    text_label.pack()
    text_label.config(font=('Times New Roman',10))

    login_btn=Button(root,text="Continue",bg="purple",fg="white",width=30,height=3,command=welcome)
    login_btn.pack(pady=(10,20))
    login_btn.config(font=("verdana",10))

    root.mainloop()



