from tkinter import *
import tkinter.messagebox

# ***************************************************** settings *******************************************************

root = Tk()
root.geometry("250x400")
root.resizable(width=False, height=False)
root.title("Calculator")
root.configure(bg="gray")

# ***************************************************** Variables ******************************************************

num1 = StringVar()
num2 = StringVar()
res = StringVar()
switch = IntVar()
switch.set(0)

# ***************************************************** Frames *********************************************************

frame_1 = Frame(root, width=400, height=50, bg='gray')
frame_1.pack(side=TOP)

frame_2 = Frame(root, width=400, height=50, bg='gray')
frame_2.pack(side=TOP)

frame_3 = Frame(root, width=400, height=50, bg='gray')
frame_3.pack(side=TOP)

frame_4 = Frame(root, width=400, height=90, bg='gray')
frame_4.pack(side=TOP)

frame_5 = Frame(root, width=400, height=50, bg='gray')
frame_5.pack(side=TOP)

# ******************* Frame Button ****************************

frame_row_1 = Frame(frame_4, width=400, height=30, bg='gray')
frame_row_1.pack(side=TOP)

frame_row_2 = Frame(frame_4, width=400, height=30, bg='gray')
frame_row_2.pack(side=TOP)

frame_row_3 = Frame(frame_4, width=400, height=30, bg='gray')
frame_row_3.pack(side=TOP)

frame_row_4 = Frame(frame_4, width=400, height=30, bg='gray')
frame_row_4.pack(side=TOP)


# ***************************************************** Function *******************************************************
def errorMsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror("Error", 'something went wrong')
    elif ms == "division zero error":
        tkinter.messagebox.showerror("Division Error", 'Can Not Divide By 0')


def num(n):
    try:
        if switch.get() == 0:
            val = num1.get() + n
            num1.set(val)
        elif switch.get() == 1:
            val = num2.get() + n
            num2.set(val)
    except:
        errorMsg('error')


def plus():
    try:
        val = float(num1.get()) + float(num2.get())
        res.set(val)
    except:
        errorMsg('error')


def minus():
    try:
        val = float(num1.get()) - float(num2.get())
        res.set(val)
    except:
        errorMsg('error')


def mul():
    try:
        val = float(num1.get()) * float(num2.get())
        res.set(val)
    except:
        errorMsg('error')


def div():
    if num2.get() == '0':
        errorMsg("division zero error")
    else:
        try:
            val = float(num1.get()) / float(num2.get())
            res.set(val)
        except:
            errorMsg('error')


def Enter():
    if num1.get() != '':
        switch.set(1)


def Clr():
    switch.set(0)
    num1.set('')
    num2.set('')
    res.set('')


# ***************************************************** Buttons ********************************************************

# ******************** Number Buttons ************************

btn_1 = Button(frame_row_1, text="1", width=3, height=1, command=lambda: num('1'))
btn_1.pack(side=LEFT, padx=10, pady=10)

btn_2 = Button(frame_row_1, text="2", width=3, height=1, command=lambda: num('2'))
btn_2.pack(side=LEFT, padx=10, pady=10)

btn_3 = Button(frame_row_1, text="3", width=3, height=1, command=lambda: num('3'))
btn_3.pack(side=LEFT, padx=10, pady=10)

btn_4 = Button(frame_row_2, text="4", width=3, height=1, command=lambda: num('4'))
btn_4.pack(side=LEFT, padx=10, pady=10)

btn_5 = Button(frame_row_2, text="5", width=3, height=1, command=lambda: num('5'))
btn_5.pack(side=LEFT, padx=10, pady=10)

btn_6 = Button(frame_row_2, text="6", width=3, height=1, command=lambda: num('6'))
btn_6.pack(side=LEFT, padx=10, pady=10)

btn_7 = Button(frame_row_3, text="7", width=3, height=1, command=lambda: num('7'))
btn_7.pack(side=LEFT, padx=10, pady=10)

btn_8 = Button(frame_row_3, text="8", width=3, height=1, command=lambda: num('8'))
btn_8.pack(side=LEFT, padx=10, pady=10)

btn_9 = Button(frame_row_3, text="9", width=3, height=1, command=lambda: num('9'))
btn_9.pack(side=LEFT, padx=10, pady=10)

btn_clr = Button(frame_row_4, text="Clear", width=3, height=1, command=lambda: Clr())
btn_clr.pack(side=LEFT, padx=10, pady=10)

btn_0 = Button(frame_row_4, text="0", width=3, height=1, command=lambda: num('0'))
btn_0.pack(side=LEFT, padx=10, pady=10)

btn_enter = Button(frame_row_4, text="Enter", width=3, height=1, command=lambda: Enter())
btn_enter.pack(side=LEFT, padx=10, pady=10)

# ******************** Operators Buttons **********************

btn_plus = Button(frame_3, text="+", width=5, command=lambda: plus())
btn_plus.pack(side=LEFT, padx=8, pady=10)

btn_minus = Button(frame_3, text="-", width=5, command=lambda: minus())
btn_minus.pack(side=LEFT, padx=8, pady=10)

btn_mul = Button(frame_3, text="*", width=5, command=lambda: mul())
btn_mul.pack(side=LEFT, padx=8, pady=10)

btn_div = Button(frame_3, text="/", width=5, command=lambda: div())
btn_div.pack(side=LEFT, padx=8, pady=10)

# ***************************************************** Entries and Labels *********************************************
label_first_num = Label(frame_1, text="Input Number 1 :", bg='gray')
label_first_num.pack(side=LEFT, padx=10, pady=10)

first_num = Entry(frame_1, textvariable=num1)
first_num.pack(side=LEFT)

label_second_num = Label(frame_2, text="Input Number 2 :", bg='gray')
label_second_num.pack(side=LEFT, padx=10, pady=10)

second_num = Entry(frame_2, textvariable=num2)
second_num.pack(side=LEFT)

result_second_num = Label(frame_5, text="Result :", bg='gray')
result_second_num.pack(side=LEFT, padx=0, pady=10)

result_num = Entry(frame_5, textvariable=res)
result_num.pack(side=LEFT)

root.mainloop()
