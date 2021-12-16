from tkinter import *
import networkx as nx
import matplotlib.pyplot as pl
from random import *

root = Tk()
root.configure(width=500, height=600)
root.title("Window1")

# TASK

def print_name():
    label_name["text"]="Іванькова А.Р."
def print_group():
    label_group["text"]="IB-91"
def print_num():
    label_num["text"]="9111"
def print_var():
    Nmb = 9111%6+1
    label_var["text"]=Nmb

colors = ["red", "blue", "yellow","green", "orange",  "gray", "violet" , "brown", "black"]

lab_quantity = Label(root,text = "Введите количество вершин графа")
lab_quantity.grid(row=4,column = 0)

nod_quantity = Entry(root)
nod_quantity.grid(row = 5,column = 0)

list_edge = []
a = [[]]

def Rand_Inc_Matrix():
    global but_set,list_edge,a
    but_set["state"] = DISABLED
    win2 = Toplevel(root)
    win2.title("Matrix of incidence")

    for i in range(int(nod_quantity.get())):
        l = Label(win2,text=i)
        l.grid(row = 1,column = i+2)
    for i in range(int(nod_quantity.get())):
        l = Label(win2,text=i)
        l.grid(row = i+2,column = 1)
    a = [[0 for i in range(int(nod_quantity.get()))] for j in range(int(nod_quantity.get()))]

    but_graph = Button(win2, text="Build a colored graph", command=build_graph)
    but_graph.grid(row=1, column=10)
    for i in range(int(nod_quantity.get())):
        for j in range(int(nod_quantity.get())):
            e = Entry(win2,width = 3)
            if i<j:
                a[i][j] = randint(0, 1)
                a[j][i] = a[i][j]
            e.insert(INSERT, a[i][j])
            if e.get() == "1":
                list_edge.append([i,j])

            e.grid(row = i+2,column = j+2)

class Adj_Matrix:
    def __init__(self, r, c, window):
        self.edge = Entry(window, width=3)
        self.edge.grid(row=r, column=c)
        self.edge.bind("<Button-1>", self.insertion)

        self.edge.insert(END, "0")

    def insertion (self, event):
        if self.edge.get() == "0":
            self.edge.delete(0, END)
            self.edge.insert(END, "1")
        if self.edge.get() == "1":
            self.edge.delete(0, END)
            self.edge.insert(END, "0")

    def get(self):
        return self.edge.get()

def Set_Inc_Matrix():
    global nod_quantity, colors
    def Graph_Builder():
        global nod_quantity,colors
        list_edge = []
        k = []
        nodes=[]
        for i in range(int(nod_quantity.get())):
            nodes.append(i)
        for i in range(len(edges)):
            list_edge.append([])
            for j in range(len(edges[i])):
                list_edge[i].append(edges[i][j].get())

        for i in range(len(list_edge)):
            for j in range(len(list_edge[i])):
                if list_edge[i][j] == "1":
                    k.append([int(j), int(i)])

        list_edge = k

        ############### GRAPH BUILDER ##################

        graph = nx.Graph()
        graph.add_edges_from(list_edge)

        dict = {}
        dict.update({nodes[0]: "red"})

        for n in nodes:
            i = 0
            for e in list_edge:
                if n in e:
                    i += 1
            while n not in dict:
                for j in range(i):
                    color = 0
                    for e in list_edge:
                        if n in e:
                            if n == e[0]:
                                if e[1] in dict:
                                    while dict.get(e[1]) == colors[color]:
                                        color += 1
                            else:
                                if e[0] in dict:
                                    while dict.get(e[0]) == colors[color]:
                                        color += 1
                dict.update({n: colors[color]})
        color_value = [dict.get(n) for n in graph.nodes()]
        nx.draw(graph, node_color=color_value, with_labels=True)
        pl.show()

    win_adj = Toplevel(root)
    win_adj.title("Matrix of adjacent")

    edges = []

    for i in range(int(nod_quantity.get())):
        lab = Label(win_adj, text=i)
        lab.grid(row=0, column=i + 1)
    for i in range(int(nod_quantity.get())):
        lab = Label(win_adj, text=i)
        lab.grid(row=i + 1, column=0)
    for c in range(int(nod_quantity.get())):
        edges.append([])
        for r in range(int(nod_quantity.get())):
            edges[c].append(Adj_Matrix(r + 1, c + 1, win_adj))

    but_gr_adj = Button(win_adj, text="Build a colored graph", command=Graph_Builder)
    but_gr_adj.grid(row=13, column=0)

def build_graph():
    global nod_quantity, a, list_edge,colors
    R1 = []
    R2 = []
    global list_edge,nod_quantity
    for i in range(int(nod_quantity.get())):
        if [1,i+1] in list_edge or [i+1,1] in list_edge:
            R1.append(i+1)
    print(R1)
    for i in R1:
        for j in range(int(nod_quantity.get())):
            if ([i,j+1] in list_edge or [j+1,i] in list_edge) and (j+1 != 1 and [1,j+1] not in list_edge and [j+1,1] not in list_edge):
                R2.append(j+1)
    R2 = set(R2)
    print(R2)

    map = []
    ready = []
    i = 0
    for n in range(int(nod_quantity.get())):
        if n not in ready:
            i += 1
            map.append([n, i])
            ready.append(n)
            R1 = []
            R2 = []
            for i in range(int(nod_quantity.get())):
                if [1, i + 1] in list_edge or [i + 1, 1] in list_edge:
                    R1.append(i + 1)
            print(R1)
            for i in R1:
                for j in range(int(nod_quantity.get())):
                    if ([i, j + 1] in list_edge or [j + 1, i] in list_edge) and (
                            j + 1 != 1 and [1, j + 1] not in list_edge and [j + 1, 1] not in list_edge):
                        R2.append(j + 1)
            R2 = set(R2)
            R2=list(R2)
            for k in R2:
                for j in R2:
                    if [k,j] not in list_edge and [j,k] not in list_edge and k not in ready:
                        # print([r1,r2])
                        map.append([k, i])
                        ready.append(k)
    nodes=[]
    for i in range(int(nod_quantity.get())):
        nodes.append(i)
    graph = nx.Graph()
    graph.add_edges_from(list_edge)

    dict = {}
    dict.update({nodes[0]: "red"})

    for n in nodes:
        i = 0
        for e in list_edge:
             if n in e:
                 i += 1
        while n not in dict:
            for j in range(i):
                color = 0
                for e in list_edge:
                    if n in e:
                        if n == e[0]:
                            if e[1] in dict:
                                while dict.get(e[1]) == colors[color]:
                                    color += 1
                        else:
                            if e[0] in dict:
                                while dict.get(e[0]) == colors[color]:
                                    color += 1
            dict.update({n: colors[color]})
    color_value = [dict.get(n) for n in graph.nodes()]
    nx.draw(graph, node_color=color_value, with_labels=True)
    pl.show()

################## BUTTONS ############################

but_set = Button(root,text = "Задать самостоятельно",command = Set_Inc_Matrix)
but_set.grid(row=6,column=1)

but_rand = Button(root, text="Заполнить рандомно", command=Rand_Inc_Matrix)
but_rand.grid(row=6, column=0)

################## VARIANT #######################

label_name = Label(root, text="")
label_group = Label(root, text="")
label_num = Label(root, text="")
label_var = Label(root, text="")

but_name = Button(root, text="П.І.Б." ,command=print_name,width =15)
but_group = Button(root, text="Група",command=print_group,width =15)
but_num = Button(root, text="Залікова книжка", command=print_num,width =15)
but_var = Button(root, text="Варіант завдання",command=print_var,width =15)

but_name.grid(row=0)
but_group.grid(row=1)
but_num.grid(row=2)
but_var.grid(row=3)

label_name.grid(row=0, column=1)
label_group.grid(row=1, column=1)
label_num.grid(row=2, column=1)
label_var.grid(row=3, column=1)

######################## MENU ###########################

mainmenu = Menu(root)
root.config(menu=mainmenu)
windmenu=Menu(mainmenu)
mainmenu.add_cascade(label= "Windows", menu=windmenu)

root.mainloop()