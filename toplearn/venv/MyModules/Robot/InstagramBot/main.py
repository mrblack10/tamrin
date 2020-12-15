from tkinter import *
import tkinter.messagebox
from MyModules.Robot.InstagramBot.Instagram_Bot import InstagramBot
import time

# ***************************************************** settings *******************************************************

root = Tk()
root.title('instagram bot')
root.geometry('400x300')
root.resizable(width=False, height=False)
root.configure(bg="gray")

# ***************************************************** Frames *********************************************************

frame_1 = Frame(root, width=400, height=50, bg='gray')
frame_1.pack(side=TOP)
frame_1_right = Frame(frame_1, width=60, height=50, bg='gray')
frame_1_right.pack(side=RIGHT)

frame_2 = Frame(root, width=400, height=50, bg='gray')
frame_2.pack(side=TOP)
frame_2_right = Frame(frame_2, width=60, height=50, bg='gray')
frame_2_right.pack(side=RIGHT)

frame_3 = Frame(root, width=400, height=50, bg='gray')
frame_3.pack(side=TOP)

frame_4 = Frame(root, width=400, height=50, bg='gray')
frame_4.pack(side=TOP)
frame_4_right = Frame(frame_4, width=10, height=40, bg='gray')
frame_4_right.pack(side=RIGHT)
frame_4_left = Frame(frame_4, width=380, height=40, bg='gray')
frame_4_left.pack(side=LEFT)

frame_5 = Frame(root, width=400, height=50, bg='gray')
frame_5.pack(side=TOP)
frame_5_left = Frame(frame_5, width=340, height=40, bg='gray')
frame_5_left.pack(side=LEFT)
frame_5_right = Frame(frame_5, width=120, height=40, bg='gray')
frame_5_right.pack(side=LEFT)

line = Frame(root, width=500, height=4, bg='black')
line.pack(side=TOP)

frame_6 = Frame(root, width=400, height=100, bg='gray')
frame_6.pack(side=TOP)

# ***************************************************** Variables ******************************************************

username = StringVar()
password = StringVar()
tags = StringVar()
comment = StringVar()
bool_cm = BooleanVar()
state_comment = BooleanVar()
state_comment.set(False)
num = IntVar()
num.set(1)

# *************************************************** Entries and Labels *********************************************

# *********** frame 1 ***********

username_label = Label(frame_1, text="* Username :", font=('nazanin', 11), width=15, bg='gray')
username_label.pack(side=LEFT, padx=1, pady=10)
username_input = Entry(frame_1, width=25)
username_input.pack(side=LEFT, padx=10, pady=10)

password_label = Label(frame_2, text="* Password :", font=('nazanin', 11), width=15, bg='gray')
password_label.pack(side=LEFT, padx=1, pady=10)
password_input = Entry(frame_2, width=25)
password_input.pack(side=LEFT, padx=10, pady=10)

# *********** frame 2 ***********

tags_label = Label(frame_3, text="* Tags :", font=('nazanin', 11), width=15, bg='gray')
tags_label.pack(side=LEFT, padx=0, pady=10)
tags_input = Entry(frame_3, width=35)
tags_input.pack(side=LEFT, padx=10, pady=10)

# *********** frame 4 ***********

cm_label = Label(frame_4_right, text=" Comment :       ", font=('nazanin', 11), width=10, bg='gray', state=DISABLED)
cm_label.pack(side=LEFT, padx=7, pady=10)
cm_input = Entry(frame_4_right, width=35, state=DISABLED)
cm_input.pack(side=LEFT, padx=10, pady=10)

# *********** frame 5 ***********

num_label = Label(frame_5_left, text="Number :", font=('nazanin', 11), width=10, bg='gray')
num_label.pack(side=LEFT, padx=14, pady=10)
num_input = Entry(frame_5_left, width=13)
num_input.pack(side=LEFT, padx=15, pady=10)

# *********** frame 6 ***********




# ***************************************************** Function *******************************************************

def enter():
    if username_input.get() != '' and password_input.get() != '' and tags_input.get() != '':
        username.set(username_input.get())
        password.set(password_input.get())
        if ' ' in tags_input.get():
            tkinter.messagebox.showerror("Tags Error", "Please separate tag with ',' ! ")
        else:
            tags.set(tags_input.get())
        if num_input.get() != '':
            try:
                num.set(int(num_input.get()))
            except:
                tkinter.messagebox.showerror("Error", "Number Error! ")
        if cm_input.get() != '':
            comment.set(cm_input.get())
        else:
            comment.set('❤')

        user = InstagramBot(username.get(), password.get())
        user.Login()
        user.Like(tags.get(), bool_Comment=state_comment.get(), Comment=comment.get(), num=num.get())
        user.Quit()
        finish_output = Label(frame_6, bg='gray', bd=-10, fg='green', width=50,text = "Done! 😍", font=('nazanin', 11))
        finish_output.pack(side=TOP)
    else:
        tkinter.messagebox.showerror("Error", "username and password and tags must be filled! ")


def box_cm():
    if bool_cm.get():
        state_comment.set(True)
        cm_label.config(state=NORMAL)
        cm_input.config(state=NORMAL)
    else:
        state_comment.set(False)
        cm_label.config(state=DISABLED)
        cm_input.config(state=DISABLED)


# ***************************************************** Buttons ********************************************************

btn_cm = Checkbutton(frame_4_left, variable=bool_cm, bg='gray', activebackground='green',
                     command=lambda: box_cm())
btn_cm.pack()

btn_enter = Button(frame_5_right, text='Enter', width=7, activebackground='green', bd=5,
                   command=lambda: enter())
btn_enter.place(x=55, y=5)

root.mainloop()


#
# test.Quit()
# btn_enter.mainloop()
