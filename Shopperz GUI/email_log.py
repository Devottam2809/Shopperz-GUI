from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image

def access():

    log=Tk()
    log.title("Shopperz Login")

    log.minsize(500,300)

    log.iconbitmap("favicon.ico")

    log.config(background="pink")

    #bd_image=Image.open("successlogin.jpeg")
    #resized_img=bd_image.resize((400,400))
    #img=ImageTk.PhotoImage(resized_img)
    #img_label=Label(log,image=img)
    #img_label.pack(pady=(10,10))

    text_label=Label(log,text="Login Successful",fg="purple",bg="pink")
    text_label.pack()
    text_label.config(font=('broadway',30))

    text_label=Label(log,text=" Redirecting you to the Homepage ",fg="purple",bg="pink")
    #text_label=Label(log,text=" -----------------------------------------------------------------------------------------------",fg="purple",bg="pink")
    text_label.pack()
    text_label.config(font=('Times New Roman',15))

    text_label=Label(log,text=" ----------------------------------------",fg="purple",bg="pink")
    text_label.pack()
    text_label.config(font=('Times New Roman',15))
    log.mainloop()

def otp():

    log=Tk()
    log.title("Shopperz Login")

    log.iconbitmap("favicon.ico")

    log.minsize(500,300)
    log.config(background="pink")

    text_label=Label(log,text="Enter the OTP",fg="purple",bg="pink")
    text_label.pack()
    text_label.config(font=('Times New Roman',15))

    otp=Entry(log,width=50)
    otp.pack(ipady=4,pady=(1,15))

    login_btn=Button(log,text="Continue",bg="purple",fg="white",width=30,height=3,command=access)
    login_btn.pack(pady=(10,20))
    login_btn.config(font=("verdana",10))
    log.mainloop()

def wrong_access():
    
    log=Tk()
    log.title("Shopperz Login")

    log.minsize(500,300)

    log.iconbitmap("favicon.ico")

    log.config(background="pink")

    text_label=Label(log,text="Please Try Again",fg="purple",bg="pink")
    text_label.pack()
    text_label.config(font=('broadway',30))

    text_label=Label(log,text=" ----------------------------------------",fg="purple",bg="pink")
    text_label.pack()
    text_label.config(font=('Times New Roman',15))

    text_label=Label(log,text="No user with the registered email",fg="purple",bg="pink")
    text_label.pack()
    text_label.config(font=('Times New Roman',15))
    log.mainloop()
