from tkinter import *
from tkinter import messagebox
with open('history.txt', 'a') as create:
    create.write('')
window = Tk()
window.title('Calculator')
window.resizable(False,False)
window['bg'] = '#424242'

tela = Text(window, width=25, height=2, fg='black',font=('Arial',20))
tela.grid(column=6,padx=0, pady=40, ipadx=0, ipady=0)
tela.configure(background='white')

#functions
def resolve():
    result = eval(tela.get("1.0","end-1c"))
    tela.delete('1.0', END)
    tela.insert('1.0', result)
    with open('history.txt', 'a') as carac:
        carac = carac.write('=\n' + str(result) + '\n')
def addsing(sing):
    tela.insert(END, sing)
    with open('history.txt', 'a') as car:
        numbers = car.write(str(sing))
def readh():
    with open('history.txt', 'r') as h:
        red = h.read()
        #box = messagebox.showinfo('history', red,)
        window2 = Tk()
        window2.title('History')
        window2.geometry('300x300')
        window2.resizable(False, True)
        history =  Label(window2, text=red, font=('Arial',15))
        history.pack()
def delhistory():
    with open('history.txt', 'w') as d:
        deletar = d.write('')
showh = Button(window, width=7, height=2, text='History', bg='#3b3f49', activebackground='#3b3f49',font=('Bold',12),command=readh)
showh.grid(column=2, row=0)
delhis = Button(window, width=7, height=2, text='Clear', bg='#3b3f49',activebackground='#3b3f49', font=('Bold',12),command=delhistory)
delhis.grid(column=3, row=0)

def unwrite():
    tela.delete('1.0', END)
def op(): 
    #operadores
    
    plus = Button(window, width=3, height=0, text='+',activebackground='#999893', font=('Arial', 25), command=lambda: addsing('+'))
    plus['bg'] = '#424242'
    plus.grid(column=2  ,row=3, padx=0, pady=0, ipadx=0, ipady=0)

    sub = Button(window, width=3, height=0, text='-',activebackground='#999893', font=('Arial', 25), command=lambda: addsing('-'))
    sub['bg'] = '#424242'
    sub.grid(column=2  ,row=4, padx=0, pady=0, ipadx=0, ipady=0)

    mult = Button(window, width=3, height=0, text='x',activebackground='#999893', font=('Arial', 25), command=lambda: addsing('*'))
    mult['bg'] = '#424242'
    mult.grid(column=2  ,row=5, padx=0, pady=0, ipadx=0, ipady=0)

    div = Button(window, width=3, height=0, text='÷',activebackground='#999893', font=('Arial', 25), command= lambda: addsing('/'))
    div['bg'] = '#424242'
    div.grid(column=2  ,row=6, padx=0, pady=0, ipadx=0, ipady=0)

    delete = Button(window, width=5, height=0, text='c', font=('Arial', 25), command=lambda: unwrite())
    delete['bg'] = '#3b3f49'
    delete.grid(column=3, row=6, padx=0, pady=0, ipadx=0, ipady=0)

    equal = Button(window, width=5, height=0, text='=', font=('Arial', 25), command= resolve)
    equal['bg'] = '#82c5f6'
    equal.grid(column=5, row=6, padx=0, pady=0, ipadx=0, ipady=0)
def numbers():
    #numeros
    zero = Button(window, width=5, height=0, text='0', font=('Arial', 25), command=lambda: addsing(int(0)))
    zero['bg'] = '#4c4c4c'
    zero.grid(column=4,row=6, padx=0, pady=0, ipadx=0, ipady=0)

    one = Button(window, width=5, height=0, text='1', font=('Arial', 25), command=lambda: addsing(int(1)))
    one['bg'] = '#4c4c4c'
    one.grid(column=3,row=5, padx=0, pady=0, ipadx=0, ipady=0)


    two = Button(window, width=5, height=0, text='2', font=('Arial', 25), command=lambda: addsing(2))
    two['bg'] = '#4c4c4c'
    two.grid(column=4,row=5, padx=0, pady=0, ipadx=0, ipady=0)

    three = Button(window, width=5, height=0, text='3', font=('Arial', 25), command=lambda: addsing(3))
    three['bg'] = '#4c4c4c'
    three.grid(column=5,row=5, padx=0, pady=0, ipadx=0, ipady=0)

    four = Button(window, width=5, height=0, text='4', font=('Arial', 25), command=lambda: addsing(4))
    four['bg'] = '#4c4c4c'
    four.grid(column=3,row=4, padx=0, pady=0, ipadx=0, ipady=0)

    five = Button(window, width=5, height=0, text='5', font=('Arial', 25), command=lambda: addsing(5))
    five['bg'] = '#4c4c4c'
    five.grid(column=4,row=4, padx=0, pady=0, ipadx=0, ipady=0)

    six = Button(window, width=5, height=0, text='6', font=('Arial', 25), command=lambda: addsing(6))
    six['bg'] = '#4c4c4c'
    six.grid(column=5,row=4, padx=0, pady=0, ipadx=0, ipady=0)

    seven = Button(window, width=5, height=0, text='7', font=('Arial', 25), command=lambda: addsing(7))
    seven['bg'] = '#4c4c4c'
    seven.grid(column=3,row=3, padx=0, pady=0, ipadx=0, ipady=0)

    eight = Button(window, width=5, height=0, text='8', font=('Arial', 25), command=lambda: addsing(8))
    eight['bg'] = '#4c4c4c'
    eight.grid(column=4,row=3, padx=0, pady=0, ipadx=0, ipady=0)

    nine = Button(window, width=5, height=0, text='9', font=('Arial', 25), command=lambda: addsing(9))
    nine['bg'] = '#4c4c4c'
    nine.grid(column=5,row=3, padx=0, pady=0, ipadx=0, ipady=0)


op()
numbers()

window.mainloop()
