#creation of login form using tkinter

from tkinter import*                #to import tkinter library
from tkinter import messagebox      # from pillow library to add background image
from PIL import ImageTk,Image

def continue_log():
    email=email_phone.get()                     #to get what user has entered as email
    #print(email)
    if email == "enter_your_email":
        from email_log import otp
        otp()
    else:
        from email_log import wrong_access
        wrong_access()

def new_acc():
    from newuser import newu
    newu()

root=Tk()                           # create object
root.title("Shopperz")              #title for the gui       

root.minsize(600,600)               # to give a minimum size to the gui screen

root.iconbitmap("favicon.ico")      #to create favicon for gui

root.config(background="pink")      #to give background color to gui window hex code can also be used here

bd_image=Image.open("shop.jpg")         #to add image
resized_img=bd_image.resize((550,200))
img=ImageTk.PhotoImage(resized_img)
img_label=Label(root,image=img)
img_label.pack(pady=(10,10))         # to automatically adjust image in background of gui
                                     # pady for adjusting margin of photo for gui here 10 is px

text_label=Label(root,text="Sign in",fg="purple",bg="pink")
text_label.pack()
text_label.config(font=('broadway',30))

text_label=Label(root,text="email or phone number",fg="purple",bg="pink")
text_label.pack()
text_label.config(font=('Times New Roman',15))      #for font size and style

email_phone=Entry(root,width=50)                # creation of email entry box
email_phone.pack(ipady=4,pady=(1,15))

login_btn=Button(root,text="Continue",bg="purple",fg="white",width=30,height=3,command=continue_log)
login_btn.pack(pady=(10,20))
login_btn.config(font=("verdana",10))           #for font size and style

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

root.mainloop()                         # if this command is not present then the GUI will not appear on the screen
