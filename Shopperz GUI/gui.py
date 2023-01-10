#creation of login form using tkinter

from tkinter import* #to import tkinter library
from PIL import ImageTk,Image # from pillow library to add background image
from tkinter import messagebox

def handle():
    #print("click")
    email=email_input.get() #to get what user has entered as email
    pas=pass_input.get()
    #print(email,pas)
    if email=="devottam2809@gmail.com" and pas=="abcd1234":
        messagebox.showinfo("Login Successful")
    else:
        messagebox.showerror("Access Denied")

root=Tk()   # create object
root.title("Hello") #title for the gui
#root.iconbitmap('favicon.ico') #to create favicon for gui

root.minsize(400,400) # to give a minimum size to the gui screen
root.maxsize(800,500) #give a maximum size for gui
#root.geometry('300x300') #to give a set geometry for gui
root.configure(background='blue') #to give background color to gui window hex code can also be used here
img=Image.open('dcpic.jpg')
resized_img=img.resize((100,100))
img=ImageTk.PhotoImage(resized_img) #to add image
img_label=Label(root,image=img)
img_label.pack(pady=(10,10)) # to automatically adjust image in background of gui
                            # pady for adjusting margin of photo for gui here 10 is px
 
text_label=Label(root,text="DCpic",fg="white",bg="red")
text_label.pack()
text_label.config(font=('verdana',24)) #for font size and style

email_label=Label(root,text="Enter Password",fg="white",bg="blue") # creation of password box
email_label.pack(pady=(20,5))
email_label.config(font=("verdana",14))

email_input=Entry(root,width=50)
email_input.pack(ipady=4,pady=(1,15)) # ipady for height

pass_label=Label(root,text="Enter Email",fg="white",bg="blue") # creation of password box
pass_label.pack(pady=(20,5))
pass_label.config(font=("verdana",14))

pass_input=Entry(root,width=50)
pass_input.pack(ipady=4,pady=(1,15))

login_btn=Button(root,text="Login Here",bg="white",fg="black",width=30,height=3,command=handle) #creation of login button
login_btn.pack(pady=(10,20))
login_btn.config(font=("verdana",10))


root.mainloop() #if main loop is not there then gui will apper but will not be on screen

# 11 march (devansh)
# 8 august (harshita) gumane le chalo as gift
