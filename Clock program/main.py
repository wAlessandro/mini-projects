from tkinter import *
import time
print(time.ctime())
window = Tk()
time
def timeupdate():
    currenttime = time.strftime("%I:%M:%S %p")
    timelabel.config(text=currenttime)
    daylabel.config(text=time.strftime("%A"))
    datelabel.config(text=time.strftime("%B %d, %Y"))
    window.after(1000,timeupdate)
    
timelabel = Label(window,bg='black',fg='white',font=('Constantina',50))
timelabel.pack()

daylabel = Label(window,font=("Ink Free",40))
daylabel.pack()

datelabel = Label(window,font=("Ink Free",20))
datelabel.pack()


timeupdate()
window.mainloop()