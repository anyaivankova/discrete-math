from tkinter import *
from random import *
root = Tk()
root.geometry("800x400")
root.title("Main Menu")
root.configure(bg="paleturquoise")

A = set()
B = set()
C = set()
D = set()

U = set()

X = set()
Y = set()
Z = set()

l=0
s=0
j=0



# U-SET
U=set(range(0,256))
def set_U():
    U.clear()
    if (int(range_U1.get())<int(range_U2.get())):
        for i in range(int(range_U1.get()),int(range_U2.get())+1):
            U.add(i)

def accept():
    global a, b, c
    if radio.get() == 1:
        global A,B,C
        A = str(A_enter.get()).split()
        for k in range(len(A)):
            A[k] = int(A[k])
        B = str(B_enter.get()).split()
        for k in range(len(B)):
            B[k] = int(B[k])
        C = str(C_enter.get()).split()
        for k in range(len(C)):
            C[k] = int(C[k])

def input():

    A_random["state"]=DISABLED
    B_random["state"] = DISABLED
    C_random["state"] = DISABLED

def random():
    global a,b,c
    A_enter["state"]=DISABLED
    B_enter["state"] = DISABLED
    C_enter["state"] = DISABLED

    while len(A) != int(A_capacity.get()):
        A.add(randint(0,256))
    A_random.delete(0, END)
    A_random.insert(INSERT, list(A))
    while len(B) != int(B_capacity.get()):
        B.add(randint(0,256))
    B_random.delete(0, END)
    B_random.insert(INSERT, list(B))
    while len(C) != int(C_capacity.get()):
        C.add(randint(0,256))
    C_random.delete(0, END)
    C_random.insert(INSERT, list(C))


# TASK

def print_name():
    label_name["text"]="Іванькова А.Р."
def print_group():
    label_group["text"]="IB-91"
def print_num():
    label_num["text"]="11"
def print_var():
    g = 91
    n = 11
    m = "ІВ"
    if m == "ІО": n += 2
    Nmb = (n + g % 60) % 30 + 1
    label_var["text"]=Nmb

# CAPACITY

cap_label = Label(root, text = "Потужність",bg="darkturquoise")
A_cap_label = Label(root, text = "A:",bg="darkturquoise")
B_cap_label = Label(root, text = "B:",bg="darkturquoise")
C_cap_label = Label(root, text = "C:",bg="darkturquoise")
A_capacity = Entry(root)
B_capacity = Entry(root)
C_capacity = Entry(root)




but_U = Button(root, text = "Задати діапазон множини U:", command=set_U,bg="darkturquoise")
label_from = Label(root, text = "від",bg="darkturquoise")
label_till = Label(root, text = "до",bg="darkturquoise")
range_U1 = Entry(root)
range_U2 = Entry(root)


cap_label.place(relx=0.35,rely=0.05)
A_cap_label.place(relx = 0.5, rely= 0.05)
B_cap_label.place(relx = 0.5, rely= 0.10)
C_cap_label.place(relx = 0.5, rely= 0.15)
A_capacity.place(relx = 0.6, rely= 0.05)
B_capacity.place(relx = 0.6, rely= 0.10)
C_capacity.place(relx = 0.6, rely= 0.15)

but_U.place(relx = 0.20, rely= 0.25)
label_from.place(relx = 0.5, rely= 0.25)
label_till.place(relx = 0.75, rely= 0.25)
range_U1 .place(relx = 0.55, rely= 0.25)
range_U2.place(relx = 0.8, rely= 0.25)


# ABC INPUT


but_accept = Button(root, text="Прийняти", command=accept,bg="darkturquoise")
but_accept.place(relx=0.9,rely=0.1)

A_hi_label = Label(root, text = "A:",bg="darkturquoise")
B_hi_label = Label(root, text = "B:",bg="darkturquoise")
C_hi_label = Label(root, text = "C:",bg="darkturquoise")

A_enter = Entry(root,width=95)
B_enter = Entry(root,width=95)
C_enter = Entry(root,width=95)

A_rand_label = Label(root, text = "A:",bg="darkturquoise")
B_rand_label = Label(root, text = "B:",bg="darkturquoise")
C_rand_label = Label(root, text = "C:",bg="darkturquoise")

A_random = Entry(root,width=95)
B_random = Entry(root,width=95)
C_random = Entry(root,width=95)

A_hi_label.place(relx = 0.1, rely= 0.45)
B_hi_label.place(relx = 0.1, rely= 0.5)
C_hi_label.place(relx = 0.1, rely= 0.55)

A_enter.place(relx = 0.15, rely= 0.45)
B_enter.place(relx = 0.15, rely= 0.5)
C_enter.place(relx = 0.15, rely= 0.55)

A_rand_label.place(relx = 0.1, rely= 0.75)
B_rand_label.place(relx = 0.1, rely= 0.8)
C_rand_label.place(relx = 0.1, rely= 0.85)

A_random.place(relx = 0.15, rely= 0.75)
B_random.place(relx = 0.15, rely= 0.8)
C_random.place(relx = 0.15, rely= 0.85)





#WINDOW 2

def window2():

    win2 = Toplevel(root)
    win2.title("Window 2")
    win2.geometry("800x400")
    win2.configure(bg="lemonchiffon")
    def long():
        global l, A, B, C
        A = set(A)
        B = set(B)
        C = set(C)
        if l == 0:
            one = A | (U - B)
            text_task1.delete(1.0, END)
            text_task1.insert(INSERT, "(A∪¬B)={0}".format(one))
            text_operation.delete(1.0, END)
            text_operation.insert(INSERT, "(A∪¬B)")
            l += 1
        elif l == 1:
            two = U - ((U - A) & (A | (U - B)))
            text_task1.delete(1.0, END)
            text_task1.insert(INSERT, "¬(¬A∩(A∪¬B))={0}".format(two))
            text_operation.delete(1.0, END)
            text_operation.insert(INSERT, "¬(¬A∩(A∪¬B))")
            l += 1
        elif l == 2:
            three = U - ((U - A) & (A | (U - B))) & (U - C)
            text_task1.delete(1.0, END)
            text_task1.insert(INSERT, "¬(¬A∩(A∪¬B))∩¬C={0}".format(three))
            text_operation.delete(1.0, END)
            text_operation.insert(INSERT, "¬(¬A∩(A∪¬B))∩¬C")
            l += 1
        else:
            text_task1.delete(1.0, END)
            text_operation.delete(1.0, END)
            l = 0

    def save1():
        with open(r"C:\Users\Анна\Desktop\дискретка\lab1\window2.txt", "w", encoding="utf-8") as w:
            w.write(str(text_task1.get(1.16, END)))

    menu2 = Menu(win2)
    win2.config(menu=menu2)
    wind2menu = Menu(menu2)
    wind2menu.add_command(label="Window 3", command=window3)
    wind2menu.add_command(label="Window 4", command=window4)
    wind2menu.add_command(label="Window 5", command=window5)
    wind2menu.add_command(label="Save",command=save1)
    menu2.add_cascade(label="Windows", menu=wind2menu)

    label_seta2 = Label(win2, text="Множина А:",bg="gold")
    label_setb2 = Label(win2, text="Множина B:",bg="gold")
    label_setc2 = Label(win2, text="Множина C:",bg="gold")
    seta2 = Label(win2, text=list(A),bg="lemonchiffon")
    setb2 = Label(win2, text=list(B),bg="lemonchiffon")
    setc2 = Label(win2,text=list(C),bg="lemonchiffon")


    label_seta2.place(relx=0.05,rely=0.05)
    label_setb2.place(relx=0.05,rely=0.10)
    label_setc2.place(relx=0.05,rely=0.15)
    seta2.place(relx=0.15,rely=0.05)
    setb2.place(relx=0.15,rely=0.10)
    setc2.place(relx=0.15,rely=0.15)

    label_task1=Label(win2, text="D=¬(¬A∩(A∪¬B))∩¬C",bg="gold")
    label_task1.place(relx=0.4,rely=0.23)

    label_D = Label(win2,text="D:",bg="gold")
    label_D.place(relx=0.02,rely=0.35)

    text_task1=Text(win2,width=70,height=5)
    text_task1.place(relx=0.05, rely=0.3)

    but_step=Button(win2,text="Крок",command=long,bg="gold")
    but_step.place(relx=0.9,rely=0.35)

    label_operation=Label(win2,text="Операція",bg="gold")
    label_operation.place(relx=0.45,rely=0.55)

    text_operation = Text(win2, width=70, height=5)
    text_operation.place(relx=0.05, rely=0.65)

# WINDOW 3

def window3():
    win3 = Toplevel(root)
    win3.title("Window 3")
    win3.geometry("800x500")
    win3.configure(bg="palegreen")

    def save2():
        with open(r"C:\Users\Анна\Desktop\дискретка\lab1\window3.txt", "w", encoding="utf-8") as w:
            w.write(str(text_task2.get(1.7, END)))

    def short():
        global s, A, B, C
        A = set(A)
        B = set(B)
        C = set(C)

        if s == 0:
            one = A | B
            text_task2.delete(1.0, END)
            text_task2.insert(INSERT, "A∪B={0}".format(one))
            text_operation2.delete(1.0, END)
            text_operation2.insert(INSERT, "A∪B")
            s += 1
        elif s == 1:
            second = (A | B) & (U - C)
            text_task2.delete(1.0, END)
            text_task2.insert(INSERT, "A∪B∩¬C={0}".format(second))
            text_operation2.delete(1.0, END)
            text_operation2.insert(INSERT, "A∪B∩¬C")
            s += 1
        else:
            text_task2.delete(1.0, END)
            text_operation2.delete(1.0, END)
            s = 0

    menu3 = Menu(win3)
    win3.config(menu=menu3)
    wind3menu = Menu(menu3)
    wind3menu.add_command(label="Window 2", command=window2)
    wind3menu.add_command(label="Window 4", command=window4)
    wind3menu.add_command(label="Window 5", command=window5)
    wind3menu.add_command(label="Save",command=save2)
    menu3.add_cascade(label="Windows", menu=wind3menu)

    label_seta3 = Label(win3, text="Множина А:",bg="seagreen")
    label_setb3 = Label(win3, text="Множина B:",bg="seagreen")
    label_setc3 = Label(win3, text="Множина C:",bg="seagreen")
    seta3 = Label(win3, text=list(A),bg="palegreen")
    setb3 = Label(win3, text=list(B),bg="palegreen")
    setc3 = Label(win3, text=list(C),bg="palegreen")

    label_seta3.place(relx=0.05, rely=0.05)
    label_setb3.place(relx=0.05, rely=0.10)
    label_setc3.place(relx=0.05, rely=0.15)
    seta3.place(relx=0.15, rely=0.05)
    setb3.place(relx=0.15, rely=0.10)
    setc3.place(relx=0.15, rely=0.15)

    label_task2 = Label(win3, text="D=A∪B∩¬C",bg="seagreen")
    label_task2.place(relx=0.4, rely=0.25)

    label_D = Label(win3, text="D:",bg="seagreen")
    label_D.place(relx=0.02, rely=0.35)

    text_task2 = Text(win3, width=70, height=5)
    text_task2.place(relx=0.05, rely=0.3)

    but_step = Button(win3, text="Крок", command=short,bg="seagreen")
    but_step.place(relx=0.9, rely=0.35)

    label_operation2 = Label(win3, text="Операція",bg="seagreen")
    label_operation2.place(relx=0.45, rely=0.55)

    text_operation2 = Text(win3, width=70, height=5)
    text_operation2.place(relx=0.05, rely=0.65)

# WINDOW 4

def window4():

    win4 = Toplevel(root)
    win4.title("Window 4")
    win4.geometry("1000x600")
    win4.configure(bg="peachpuff")

    def save3():
        with open(r"C:\Users\Анна\Desktop\дискретка\lab1\window4.txt", "w", encoding="utf-8") as w:
            w.write(str(text_Z.get(1.0, END)))

    def count_Z():
        global X, Y, Z, A, B, C, U
        B=set(B)
        C=set(C)
        Z = C - (U - B)
        text_Z.delete(1.0, END)
        text_Z.insert(INSERT, list(Z))



    menu4 = Menu(win4)
    win4.config(menu=menu4)
    wind4menu = Menu(menu4)
    wind4menu.add_command(label="Window 2", command=window2)
    wind4menu.add_command(label="Window 3", command=window3)
    wind4menu.add_command(label="Window 5", command=window5)
    wind4menu.add_command(label="Save",command=save3)

    menu4.add_cascade(label="Windows", menu=wind4menu)

    label_X=Label(win4,text="X=C",bg="tomato")
    label_Y=Label(win4,text="Y=¬B",bg="tomato")
    label_Z=Label(win4,text="Z=X\Y",bg="tomato")

    label_X.place(relx=0.1,rely=0.15)
    label_Y.place(relx=0.1,rely=0.45)
    label_Z.place(relx=0.1,rely=0.8)

    text_X = Text(win4, height=5, width=80)
    text_X.insert(INSERT,list(C))
    text_X.place(relx=0.2,rely=0.1)

    text_Y = Text(win4, height=5, width=80 )
    text_Y.insert(INSERT, list(U-B))
    text_Y.place(relx=0.2,rely=0.4)

    text_Z = Text(win4, height=5, width=80 )
    text_Z.place(relx=0.2,rely=0.75)

    but_Z=Button(win4,text="Oбрахувати Z", command=count_Z,bg="tomato")
    but_Z.place(relx=0.45,rely=0.62)

# WINDOW 5

def window5():
    win5 = Toplevel(root)
    win5.title("Window 5")
    win5.geometry("800x500")
    win5.configure(bg="plum")

    def resD1():
        with open(r"C:\Users\Анна\Desktop\дискретка\lab1\window2.txt", "r", encoding="utf-8") as w:
            text_D1.insert(INSERT,(w.read()))

    def resD2():
        with open(r"C:\Users\Анна\Desktop\дискретка\lab1\window3.txt", "r", encoding="utf-8") as w:
            text_D2.insert(INSERT, (w.read()))

    def resZ1():
        with open(r"C:\Users\Анна\Desktop\дискретка\lab1\window4.txt", "r", encoding="utf-8") as w:
            text_Z1.insert(INSERT, (w.read()))


    def resZ2():
        global C,B,U,j
        Q=list(C)
        W=list(U-B)
        q=set()
        for i in Q:
            for j in W:
                if i not in W:
                    q.add(i)
        text_Z2.insert(INSERT,list(q))

    def comp2():
        if list(text_Z1.get(1.0,END)) == list(text_Z2.get(1.0,END)+"\n"):
            entry_Z1Z2.delete(0,END)
            entry_Z1Z2.insert(INSERT, "Рівні")
        else:
            entry_Z1Z2.delete(0,END)
            entry_Z1Z2.insert(INSERT, "Не рівні")



    def comp1():

        if text_D1.get(1.0,END) == text_D2.get(1.0,END):
            entry_D1D2.delete(0,END)
            entry_D1D2.insert(INSERT, "Рівні")
        else:
            entry_D1D2.delete(0,END)
            entry_D1D2.insert(INSERT, "Не рівні")

    menu5 = Menu(win5)
    win5.config(menu=menu5)
    wind5menu = Menu(menu5)
    wind5menu.add_command(label="Window 2", command=window2)
    wind5menu.add_command(label="Window 3", command=window3)
    wind5menu.add_command(label="Window 4", command=window4)
    menu5.add_cascade(label="Windows", menu=wind5menu)

    label_D1=Label(win5,text="D1:",bg="mediumpurple")
    label_D2 = Label(win5, text="D2:",bg="mediumpurple")
    label_Z1 = Label(win5, text="Z1:",bg="mediumpurple")
    label_Z2 = Label(win5, text="Z2:",bg="mediumpurple")

    label_D1.place(relx=0.05,rely=0.1)
    label_D2.place(relx=0.05,rely=0.25)
    label_Z1.place(relx=0.05,rely=0.5)
    label_Z2.place(relx=0.05,rely=0.65)

    but_D1=Button(win5,text="Прийняти",command=resD1,bg="mediumpurple")
    but_D2 = Button(win5, text="Прийняти",command=resD2,bg="mediumpurple")
    but_Z1 = Button(win5, text="Прийняти",command=resZ1,bg="mediumpurple")
    but_Z2 = Button(win5, text="Прийняти",command=resZ2,bg="mediumpurple")

    but_D1.place(relx=0.02,rely=0.15)
    but_D2.place(relx=0.02,rely=0.3)
    but_Z1.place(relx=0.02,rely=0.55)
    but_Z2.place(relx=0.02,rely=0.7)

    text_D1=Text(win5,height=4,width=80)
    text_D2 = Text(win5, height=4, width=80)
    text_Z1 = Text(win5, height=4, width=80)
    text_Z2 = Text(win5, height=4, width=80)

    text_D1.place(relx=0.15,rely=0.1)
    text_D2.place(relx=0.15,rely=0.25)
    text_Z1.place(relx=0.15,rely=0.5)
    text_Z2.place(relx=0.15,rely=0.65)

    but_D1D2=Button(win5,text="Порівняти D1 i D2",command=comp1,bg="mediumpurple")
    but_Z1Z2 = Button(win5, text="Порівняти Z1 i Z2",command=comp2,bg="mediumpurple")

    but_D1D2.place(relx=0.3,rely=0.4)
    but_Z1Z2.place(relx=0.3,rely=0.8)

    entry_D1D2=Entry(win5)
    entry_Z1Z2 = Entry(win5)

    entry_D1D2.place(relx=0.45,rely=0.407)
    entry_Z1Z2.place(relx=0.45,rely=0.807)



# MENU

mainmenu = Menu(root)
root.config(menu=mainmenu)
windmenu=Menu(mainmenu)
windmenu.add_command(label = "Window 2", command = window2)
windmenu.add_command(label = "Window 3", command = window3)
windmenu.add_command(label = "Window 4", command = window4)
windmenu.add_command(label = "Window 5", command = window5)
mainmenu.add_cascade(label= "Windows", menu=windmenu)


label_name = Label(root, text="",bg="paleturquoise")
label_group = Label(root, text="",bg="paleturquoise")
label_num = Label(root, text="",bg="paleturquoise")
label_var = Label(root, text="",bg="paleturquoise")

but_name = Button(root, text="П.І.Б." ,command = print_name, width =15,bg="darkturquoise")
but_group = Button(root, text="Група",command =print_group, width =15,bg="darkturquoise")
but_num = Button(root, text="Номер у списку",command =print_num, width =15,bg="darkturquoise")
but_var = Button(root, text="Варіант завдання",command =print_var, width =15,bg="darkturquoise")

but_name.grid(row=0)
but_group.grid(row=1)
but_num.grid(row=2)
but_var.grid(row=3)

label_name.grid(row=0, column=1)
label_group.grid(row=1, column=1)
label_num.grid(row=2, column=1)
label_var.grid(row=3, column=1)

# RADIO
radio=IntVar()
input_radio = Radiobutton(text="Ввести самостійно", value =1,variable=radio,command = input,bg="darkturquoise")
random_radio = Radiobutton(text="Згенерувати", value =2,variable=radio,command=random,bg="darkturquoise")
input_radio.place(relx=0.45,rely=0.35)
random_radio.place(relx=0.45,rely=0.65)






root.mainloop()