import smtplib
from tkinter import *

window = Tk()
window.title("EmailSender")
window.geometry("500x200")
window.resizable(False,False)
window['bg'] = 'white'

body = Text(window,width=40,height=10,padx=10,pady=10)
body.pack(side=RIGHT,anchor='n')

Content = Frame(window,width=10,height=10).pack(side=LEFT)

eplaceholder = Label(Content,text='Email:').pack(anchor='w')
email = Entry(window,width=30,)
email.pack()

passplaceholder = Label(Content,text='Password:').pack(anchor='w')
password = Entry(window,show="•",width=30)
password.pack()

rplaceh = Label(Content,text='To:').pack(anchor='w')
receiver = Entry(window,width=30)
receiver.pack()

subplace = Label(Content,text='Tittle:').pack(anchor='w')
subject = Entry(window,width=30)
subject.pack(anchor='w')




def send():
    tittle = str(subject.get())
    print(f"____{tittle}____")
    message = f"""From: {str(email.get())}
To: {receiver.get()}\n
Subject: {tittle}\n
{str(body.get('1.0',END))}
"""
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(str(email.get()),password.get())
    server.sendmail(str(email.get()),str(receiver.get()),str(body.get("1.0",END)))

submittbn = Button(window,text='Send',command=send)
submittbn.pack(anchor='s')

window.mainloop()