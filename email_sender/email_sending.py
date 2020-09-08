
import smtplib
import tkinter
from tkinter import *
from tkinter import messagebox as mb

#login into gmail account
def login():
    sender_mail = sender_email.get()
    sender_pass = sender_password.get()
    email_server = "smtp.gmail.com"
    global sender
    global mail_server
    sender = sender_mail
    mail_server = smtplib.SMTP(email_server)
    try:
        #_ = mail_server.set_debuglevel(1)

        _ = mail_server.starttls()

        login = mail_server.login(sender, sender_pass)
        mb.showinfo("Login","Login Successful")
    except smtplib.SMTPAuthenticationError:
        mb.showerror("Denied", "Invalid Credentials")


def send_mail():
    #collect input from the GUI
    text = mail.get("1.0", "end-1c")
    sub = subject.get()
    receipient_mail = receiver_email.get()
    #create header of mail
    headers = "From: {}\r\nTo: {}\r\nSubject: {}\r\n\r\n".format(sender[:5].upper(), receipient_mail, sub)
    message = headers + text
    try:
        mail_server.sendmail(sender, receipient_mail, message)
        mb.showinfo("Mail","Mail sent succesfully!")

    except smtplib.SMTPException:
        mb.showerror("Error",'Invalid Recipient')
        return


#close the GUI and logout from account
def close():
    mail_server.quit()
    window.destroy()

#Setting up GUI structure

window = Tk()

window.wm_title("Email Sender")

#for sender email
l1=Label(window,text="Sender Email",font =(
  'Verdana', 10),width = 15,bg ="sky blue")
l1.grid(row=0,column=0)

sender_email = StringVar()
e1= Entry(window,width=40,textvariable=sender_email)
e1.grid(row=0,column=1)

#for sender pass
l2=Label(window,text="Password",font =(
  'Verdana', 10),width = 15,bg ="sky blue")
l2.grid(row=0,column=2)

sender_password = StringVar()
e2= Entry(window,width=40,textvariable=sender_password,show='*')
e2.grid(row=0,column=3)

#for receiver email

l3=Label(window,text="Recipient Email",font =(
  'Verdana', 10),width = 15,bg ="sky blue")
l3.grid(row=1,column=0)

receiver_email = StringVar()
e3= Entry(window,width=40,textvariable=receiver_email)
e3.grid(row=1,column=1)

#For subject
l4 =Label(window,text='Subject',font=('Verdana',10),
          width=15,bg="sky blue")
l4.grid(row=2,columns=1)

subject = StringVar()
e4= Entry(window,width=40,textvariable=subject)
e4.grid(row=2,column=1)

#for Message
l5=Label(window,text="Message",font =(
  'Verdana', 10),width = 15,bg ="sky blue")
l5.grid(row=3,column=2)

mail = Text(window, height = 20,
                bg = "light yellow",wrap="word")
mail.configure(font=("Times New Roman", 14))
mail.grid(row=4,column=1,rowspan=10,columnspan=4)


#Send Button
b1=Button(window,text="Send",bg = 'sky blue',width=12,command=send_mail)
b1.grid(row=3,column=4)

b2 = Button(window,text="Login",bg="sky blue",width=12,command=login)
b2.grid(row=0,column=4)

b3 = Button(window,text="Close",bg="sky blue",width=12,command=close)
b3.grid(row=14,column=4)

window.mainloop()

