from tkinter import *

root = Tk()
root.title("python GUI")
root.geometry('400x300')  # sizei ke az aval  baz mishe
root.resizable(width=False, height=False)  # bry sabet mondan arz va ertefa safe

label = Label(root, text="please enter your name : ")
label.place(x=0, y=50)

nameInput = Entry(root)
nameInput.place(x=150, y=50)


def getName():
    print(nameInput.get())  # dar console print mishavad


btn_1 = Button(root, text="Get Name", command=lambda: getName())
btn_1.place(x=300, y=47)

myName = StringVar()


def printMyName():
    # print("my name is armin :)") # dar console print mishavad
    myName.set(nameInput.get())

def exit_app():
    root.destroy()

label = Label(root, text="""Hello user""")
label.place(x=0, y=0)  # makan label

btn_2 = Button(root, text="Show My Name : ", command=printMyName)
btn_2.place(x=0, y=125)  # makan button

label_btn_2 = Label(root, textvariable=myName)
label_btn_2.place(x=100, y=127)

btn_ex = Button(root, text = 'Exit', font = ('tahoma', 19),
                fg = 'red', bg = 'black', command = exit_app, cursor = 'hand2')
btn_ex.place(x =170 , y = 200)

root.mainloop()
