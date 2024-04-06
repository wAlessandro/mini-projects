from tkinter import *

from tkinter import filedialog

WWIDHT = 400
WHEIGHT = 520

window = Tk()
window.geometry(f'{WWIDHT}x{WHEIGHT}')
window.resizable(False, False)
window.config(bg='#D2D0C8')
window.title('List')


MENUBAR = Menu(window) #bar
window.config(menu=MENUBAR)

fileMenu = Menu(MENUBAR,tearoff=0) #in bar
MENUBAR.add_cascade(label='File',menu=fileMenu)

def saveText():
    file = filedialog.asksaveasfile(defaultextension='.txt',filetypes=[('text file','.txt'),('all files','*.')])
    list = str(listbox.get(0, END))
    file.write(list)
    file.close()

fileMenu.add_command(label='Save',command=saveText) #file command


listbox = Listbox(window,
                  height=10,
                  font=('Ink Free',25),
                  bg='#CCCABE',
                  fg='black')
listbox.pack(anchor='center')

items = Frame(window, bg='#CCCAC6')
items.pack(side='top')
usertext = Entry(items,
                width=20,
                
                )
usertext.pack()

def submit():
    listbox.insert(listbox.size(), usertext.get())
    usertext.delete(0,END)
sbmtbtn = Button(items,
                 text='Submit',
                 command=submit,
                 font=('Constantina'))
sbmtbtn.pack(side=LEFT)

def deletetxt():
    try:
        listbox.delete(listbox.curselection())
    except:
        print("select a item to delete!")
delbtn = Button(items,text='Delete',
                command=deletetxt,
                font=('Constantina'))
delbtn.pack(side=RIGHT)


window.mainloop()