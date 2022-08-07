import tkinter as tk
from decimal import *

root = tk.Tk()
root.title('Calculator')
root.resizable(0, 0)

frmScreen = tk.Frame(master=root, height=10, bg='grey')
frmScreen.pack(fill=tk.X)

entScreen = tk.Entry(master=frmScreen, relief='sunken', bg='#DFEFF1', font=('TkDefaultFont', 14, 'bold'), justify='right')
entScreen.pack(fill=tk.X, padx=2, pady=3)

frmButtons = tk.Frame(master=root, bg='grey')
frmButtons.pack()

Total = 0.0
FreshTotal = True
entScreen.insert(0, '0')
Operation = False
LastOp = 'none'
LastEnt = 0.0
Fresh = True
LastEq = False
Error = False
Memory = 0.0
MemoryFlag = False

def errored():
    global Error
    clear()
    Error = True
    entScreen.delete(0, 'end')
    entScreen.insert(0, 'ERROR')

def Calculate():
    global Total, LastOp, LastEnt, LastEq, FreshTotal, Error
    if entScreen.get() == '-':
        entScreen.delete(0)
        entScreen.insert(0, 0)
    if FreshTotal:
        try:
            Total = Decimal(entScreen.get())
            FreshTotal = False
        except InvalidOperation:
            errored()
    elif not LastEq and not Operation:
        try:
            LastEnt = Decimal(entScreen.get())
            if LastOp == '+':
                Total += Decimal(entScreen.get())
            elif LastOp == '-':
                Total -= Decimal(entScreen.get())
            elif LastOp == 'X':
                Total = Total * Decimal(entScreen.get())
            elif LastOp == '/':
                try:
                    Total = Total / Decimal(entScreen.get())
                except ZeroDivisionError:
                    errored()
        except InvalidOperation:
            errored()
    else:
        if LastOp == '+':
            Total += LastEnt
        elif LastOp == '-':
            Total -= LastEnt
        elif LastOp == 'X':
            Total = Total * LastEnt
        elif LastOp == '/':
            try:
                Total = Total / LastEnt
            except ZeroDivisionError:
                errored()

#control functions for the button
def numb1():
    global Operation, Fresh, Error
    if not Error:
        if not Fresh and not Operation:
            if entScreen.get() == '0':
                entScreen.delete(0, 'end')
            if len(entScreen.get()) < 24:
                entScreen.insert('end', '1')
        else:
            if Fresh and not Operation:
                clear()
            entScreen.delete(0, 'end')
            entScreen.insert('end', '1')
            Operation, Fresh = False, False
def numb2():
    global Operation, Fresh, Error
    if not Error:
        if not Fresh and not Operation:
            if entScreen.get() == '0':
                entScreen.delete(0, 'end')
            if len(entScreen.get()) < 24:
                entScreen.insert('end', '2')
        else:
            if Fresh and not Operation:
                clear()
            entScreen.delete(0, 'end')
            entScreen.insert('end', '2')
            Operation, Fresh = False, False
def numb3():
    global Operation, Fresh, Error
    if not Error:
        if not Fresh and not Operation:
            if entScreen.get() == '0':
                entScreen.delete(0, 'end')
            if len(entScreen.get()) < 24:
                entScreen.insert('end', '3')
        else:
            if Fresh and not Operation:
                clear()
            entScreen.delete(0, 'end')
            entScreen.insert('end', '3')
            Operation, Fresh = False, False
def numb4():
    global Operation, Fresh, Error
    if not Error:
        if not Fresh and not Operation:
            if entScreen.get() == '0':
                entScreen.delete(0, 'end')
            if len(entScreen.get()) < 24:
                entScreen.insert('end', '4')
        else:
            if Fresh and not Operation:
                clear()
            entScreen.delete(0, 'end')
            entScreen.insert('end', '4')
            Operation, Fresh = False, False
def numb5():
    global Operation, Fresh, Error
    if not Error:
        if not Fresh and not Operation:
            if entScreen.get() == '0':
                entScreen.delete(0, 'end')
            if len(entScreen.get()) < 24:
                entScreen.insert('end', '5')
        else:
            if Fresh and not Operation:
                clear()
            entScreen.delete(0, 'end')
            entScreen.insert('end', '5')
            Operation, Fresh = False, False
def numb6():
    global Operation, Fresh, Error
    if not Error:
        if not Fresh and not Operation:
            if entScreen.get() == '0':
                entScreen.delete(0, 'end')
            if len(entScreen.get()) < 24:
                entScreen.insert('end', '6')
        else:
            if Fresh and not Operation:
                clear()
            entScreen.delete(0, 'end')
            entScreen.insert('end', '6')
            Operation, Fresh = False, False
def numb7():
    global Operation, Fresh, Error
    if not Error:
        if not Fresh and not Operation:
            if entScreen.get() == '0':
                entScreen.delete(0, 'end')
            if len(entScreen.get()) < 24:
                entScreen.insert('end', '7')
        else:
            if Fresh and not Operation:
                clear()
            entScreen.delete(0, 'end')
            entScreen.insert('end', '7')
            Operation, Fresh = False, False
def numb8():
    global Operation, Fresh, Error
    if not Error:
        if not Fresh and not Operation:
            if entScreen.get() == '0':
                entScreen.delete(0, 'end')
            if len(entScreen.get()) < 24:
                entScreen.insert('end', '8')
        else:
            if Fresh and not Operation:
                clear()
            entScreen.delete(0, 'end')
            entScreen.insert('end', '8')
            Operation, Fresh = False, False
def numb9():
    global Operation, Fresh, Error
    if not Error:
        if not Fresh and not Operation:
            if entScreen.get() == '0':
                entScreen.delete(0, 'end')
            if len(entScreen.get()) < 24:
                entScreen.insert('end', '9')
        else:
            if Fresh and not Operation:
                clear()
            entScreen.delete(0, 'end')
            entScreen.insert('end', '9')
            Operation, Fresh = False, False
def numb0():
    global Operation, Fresh, Error
    if not Error:
        if not Fresh and not Operation:
            if entScreen.get() != '0' and len(entScreen.get()) < 24:
                entScreen.insert('end', '0')
        else:
            if Fresh and not Operation:
                clear()
            entScreen.delete(0, 'end')
            entScreen.insert('end', '0')
            Operation, Fresh = False, False
def numbdec():
    global Operation, Fresh, Error
    if not Error:
        if '.' not in entScreen.get() and not Operation and not Fresh:
            if entScreen.get() == '':
                entScreen.insert('end', '0.')
            elif len(entScreen.get()) < 23:
                entScreen.insert('end', '.')
        else:
            if Fresh and not Operation:
                clear()
            entScreen.delete(0, 'end')
            entScreen.insert('end', '0.')
            Operation, Fresh = False, False
def sign():
    global Operation, Fresh, Error
    if not Operation and not Error:
        if Fresh:
            clear()
            entScreen.delete(0, 'end')
            entScreen.insert(0, '-')
            Fresh = False
        else:
            if len(entScreen.get()) == 0:
                entScreen.insert(0, '0')
            elif entScreen.get()[0] == '-':
                entScreen.delete(0)
            elif entScreen.get() != '0':
                entScreen.insert(0, '-')
def plus():
    global Total, Operation, LastOp, LastEnt, LastEq, Error
    if not Operation and not Error:
        if not LastEq:
            Calculate()
        if not Error:
            try:
                LastEq = False
                LastEnt = Decimal(entScreen.get())
                entScreen.insert('end', '+')
                Operation = True
                LastOp = '+'
            except InvalidOperation:
                errored()
def minus():
    global Total, Operation, LastOp, LastEnt, LastEq, Error
    if not Operation and not Error:
        if not LastEq:
            Calculate()
        if not Error:
            try:
                LastEq = False
                LastEnt = Decimal(entScreen.get())
                entScreen.insert('end', '-')
                Operation = True
                LastOp = '-'
            except InvalidOperation:
                errored()
def times():
    global Total, Operation, LastOp, LastEnt, LastEq, Error
    if not Operation and not Error:
        if not LastEq:
            Calculate()
        if not Error:
            try:
                LastEq = False
                LastEnt = Decimal(entScreen.get())
                entScreen.insert('end', 'x')
                Operation = True
                LastOp = 'X'
            except InvalidOperation:
                errored()
def divide():
    global Total, Operation, LastOp, LastEnt, LastEq, Error
    if not Operation and not Error:
        if not LastEq:
            Calculate()
        if not Error:
            try:
                LastEq = False
                LastEnt = Decimal(entScreen.get())
                entScreen.insert('end', '/')
                Operation = True
                LastOp = '/'
            except InvalidOperation:
                errored()
def equals():
    global Total, Operation, LastOp, LastEnt, LastEq, Fresh, Error
    if not Error:
        Calculate()
        if Total > 999999999999999999999999 or Total < -999999999999999999999999:
            errored()
        if not Error:
            try:
                entScreen.delete(0, 'end')
                if Decimal(Total % 1) == 0:
                    entScreen.insert('end', str(int(Total)))
                else:
                    entScreen.insert('end', str(Total))
                Operation = False
                LastEq = True
                Fresh = True
            except InvalidOperation:
                errored()
def clear():
    global Total, Operation, LastOp, LastEnt, Fresh, LastEq, FreshTotal, Error, Memory
    entScreen.delete(0, 'end')
    entScreen.insert(0, '0')
    Total = 0
    Fresh, FreshTotal = True, True
    Operation, LastEq = False, False
    LastOp = 'none'
    LastEnt = 0
    Error = False
def remember():
    global Memory, MemoryFlag, Fresh
    if not Error:
        try:
            Memory = Decimal(entScreen.get())
            MemoryFlag, Fresh = True, True
            memorybg()
        except InvalidOperation:
            errored()
def recall():
    global Memory, MemoryFlag, Error, Fresh, LastEq, Operation
    if not Error and MemoryFlag:
        if not Operation:
            clear()
        entScreen.delete(0, 'end')
        if Memory % 1 == 0:
            entScreen.insert(0, str(int(Memory)))
        else:
            entScreen.insert(0, str(Memory))
        Operation, Fresh = False, False
def forget():
    global Memory, MemoryFlag
    Memory = 0.0
    MemoryFlag = False
    memorybg()
def memorybg():
    global MemoryFlag
    updatecolor = '#ECD6F6' if MemoryFlag else '#F6F1F9'
    btnmr['bg'] = updatecolor

#drawing the buttons
btn1 = tk.Button(master=frmButtons, activebackground='grey', borderwidth=2, padx=10, pady=10, text='1', command=numb1)
btn1.grid(row=0, column=0, padx=1, pady=1, ipadx=5, ipady=5, sticky='nsew')

btn2= tk.Button(master=frmButtons, activebackground='grey40', borderwidth=2, padx=10, pady=10, text='2', command=numb2)
btn2.grid(row=0, column=1, padx=1, pady=1, ipadx=5, ipady=5,sticky='nsew')

btn3 = tk.Button(master=frmButtons, activebackground='grey40', borderwidth=2, padx=10, pady=10, text='3', command=numb3)
btn3.grid(row=0, column=2, padx=1, pady=1, ipadx=5, ipady=5,sticky='nsew')

btn4 = tk.Button(master=frmButtons, activebackground='grey40', borderwidth=2, padx=10, pady=10, text='4', command=numb4)
btn4.grid(row=1, column=0, padx=1, pady=1, ipadx=5, ipady=5,sticky='nsew')

btn5 = tk.Button(master=frmButtons, activebackground='grey40', borderwidth=2, padx=10, pady=10, text='5', command=numb5)
btn5.grid(row=1, column=1, padx=1, pady=1, ipadx=5, ipady=5,sticky='nsew')

btn6 = tk.Button(master=frmButtons, activebackground='grey40', borderwidth=2, padx=10, pady=10, text='6', command=numb6)
btn6.grid(row=1, column=2, padx=1, pady=1, ipadx=5, ipady=5,sticky='nsew')

btn7 = tk.Button(master=frmButtons, activebackground='grey40', borderwidth=2, padx=10, pady=10, text='7', command=numb7)
btn7.grid(row=2, column=0, padx=1, pady=1, ipadx=5, ipady=5,sticky='nsew')

btn8 = tk.Button(master=frmButtons, activebackground='grey40', borderwidth=2, padx=10, pady=10, text='8', command=numb8)
btn8.grid(row=2, column=1, padx=1, pady=1, ipadx=5, ipady=5,sticky='nsew')

btn9 = tk.Button(master=frmButtons, activebackground='grey40', borderwidth=2, padx=10, pady=10, text='9', command=numb9)
btn9.grid(row=2, column=2, padx=1, pady=1, ipadx=5, ipady=5,sticky='nsew')

btn0 = tk.Button(master=frmButtons, activebackground='grey40', borderwidth=2, padx=10, pady=10, text='0', command=numb0)
btn0.grid(row=0, column=4, padx=1, pady=1, sticky='nsew')

btndec = tk.Button(master=frmButtons, activebackground='grey40', borderwidth=2, padx=10, pady=10, text='.', command=numbdec)
btndec.grid(row=1, column=4, padx=1, pady=1, sticky='nsew')

btnsign = tk.Button(master=frmButtons, activebackground='grey40', borderwidth=2, padx=10, pady=10, text='+/-', command=sign)
btnsign.grid(row=2, column=4, padx=1, pady=1, sticky='nsew')

btnplus = tk.Button(master=frmButtons, bg='#F9F9E4', activebackground='#5E5E51', borderwidth=2, padx=10, pady=10, text='+', command=plus)
btnplus.grid(row=0, column=5, padx=1, pady=1, ipadx=5, sticky='nsew')

btnminus = tk.Button(master=frmButtons, bg='#F9F9E4', activebackground='#5E5E51', borderwidth=2, padx=10, pady=10, text='-', command=minus)
btnminus.grid(row=1, column=5, padx=1, pady=1, ipadx=5, sticky='nsew')

btntimes = tk.Button(master=frmButtons, bg='#F9F9E4', activebackground='#5E5E51', borderwidth=2, padx=10, pady=10, text='X', command=times)
btntimes.grid(row=2, column=5, padx=1, pady=1, ipadx=5, sticky='nsew')

btndivide = tk.Button(master=frmButtons, bg='#F9F9E4', activebackground='#5E5E51', borderwidth=2, padx=10, pady=10, text='/', command=divide)
btndivide.grid(row=3, column=5, padx=1, pady=1, ipadx=5, sticky='nsew')

btnequals = tk.Button(master=frmButtons, bg='#E4EAF9', activebackground='#51535E', borderwidth=2, padx=10, pady=10, text='=', command=equals)
btnequals.grid(row=3, column=0, padx=1, pady=1, columnspan=2, sticky='nsew')

btnclear = tk.Button(master=frmButtons, bg='#F6E4E4', activebackground='#5E5151', borderwidth=2, padx=10, pady=10, text='CE', command=clear)
btnclear.grid(row=3, column=2, padx=1, pady=1, columnspan=3, sticky='nsew')

btnmem = tk.Button(master=frmButtons, bg='#F7EEFB', activebackground='#5C515E', borderwidth=2, padx=10, pady=10, text='M', command=remember)
btnmem.grid(row=0, column=6, padx=1, pady=1, ipadx=0, sticky='nsew')

btnmc = tk.Button(master=frmButtons, bg='#F7EEFB', activebackground='#5C515E', borderwidth=2, padx=10, pady=10, text='MC', command=forget)
btnmc.grid(row=1, column=6, padx=1, pady=1, ipadx=0, sticky='nsew')

btnmr = tk.Button(master=frmButtons, bg='#F6F1F9', activebackground='#5C515E', borderwidth=2, padx=10, pady=10, text='MR', command=recall)
btnmr.grid(row=2, column=6, rowspan=2, padx=1, pady=1, ipadx=0, sticky='nsew')

root.mainloop()