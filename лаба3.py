from tkinter import *
import networkx as nx
import matplotlib.pyplot as pl
from random import *
from tkinter import messagebox
from copy import deepcopy
from networkx.drawing.nx_agraph import to_agraph



root = Tk()
root.configure(width=500, height=600)
root.title("Window1")

########################## VARIANT #########################

G=91
Num=11
M="ІВ"
NZK = 9111

def func_var():
    lab_var["text"] = '''Іванькова Анна Русланівна\n
                      Група:''' + str(M) + '''    Номер: ''' + str(Num) + str(G) + '''\n
                      Залікова книжка: ''' + str(NZK) + '''    Варіант: ''' + str((NZK%10)+1)


but_var = Button(root, text = "Показати варіант", command = func_var)
lab_var = Label(root, text="")

but_var.grid(row=1,column=7,rowspan=4)
lab_var.grid(row=5,column=7,rowspan=4)




class Adj_Matrix:
    def __init__(self, roo, r, c):
        self.edge = Entry(roo, width=3)
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


class Inc_Matrix:
    def __init__(self, roo, r, c):
        self.edge = Entry(roo, width=3)
        self.edge.grid(row=r, column=c)
        self.edge.bind("<Button-1>", self.insertion)

        self.edge.insert(END, "0")

    def insertion(self, event):
        if self.edge.get() == "0":
            self.edge.delete(0, END)
            self.edge.insert(END, "1")

        elif self.edge.get() == "1":
            self.edge.delete(0, END)
            self.edge.insert(END, "-1")

        elif self.edge.get() == "-1":
            self.edge.delete(0, END)
            self.edge.insert(END, "±1")

        else:
            self.edge.delete(0, END)
            self.edge.insert(END, "0")

    def get(self):
        return self.edge.get()


edges = []


# class Entr_edg_random:
#     def __init__(self, r, c):
#         self.edge = Entry(root, width=3)
#         self.edge.grid(row=r, column=c)
#         self.edge['text'] = random.randint(1, 10)
#
# def randomizer():
#     global edges
#     for i in range(10):
#         edges.append([])
#         for j in range(2):
#             edges[i].append(Entr_edg_random(i + 2, j + 1))


class Entr_edg:
    def __init__(self, r, c):
        self.edge = Entry(root, width=3)
        self.edge.grid(row=r, column=c)
        self.edge.insert(END, "0")

    def return_edge(self):
        return self.edge.get()





#
# but_rand = Button(root,text = "Randomizer",command= randomizer)
#
# but_rand.grid(row=8,column=7)


# ENTRY EDGES

lab_edg = Label(root, text="Список ребер")
lab_edg.grid(row=0, column=0, columnspan=5)

for i in range(10):
    l = Label(root, text=str(i+1))
    l.grid(row=i + 2, column=0, sticky=E)
    edges.append([])
    for j in range(2):
        edges[i].append(Entr_edg(i + 2, j + 1))


# BUILD MATRIXES AND GRAPH FROM EDGES

def Inc_M_and_Gr():
    list_edg = []
    for i in range(len(edges)):
        list_edg.append([])
        for j in range(len(edges[i])):
            list_edg[i].append(edges[i][j].edge.get())
    for i in range(len(list_edg) - 1, -1, -1):
        if "0" in list_edg[i] or list_edg.count(list_edg[i]) > 1:
            del list_edg[i]


    win_inc_m = Toplevel(root)
    win_inc_m.title("Matrix of incidence")
    for i in range(len(list_edg)):
        lab_inc_edge = Label(win_inc_m, text="a" + str(i + 1))
        lab_inc_edge.grid(row=0, column=i + 1)

    set_of_set_of_nodes = set()
    for i in list_edg:
        for j in i:
            set_of_set_of_nodes.add(j)
    set_of_set_of_nodes = list(set_of_set_of_nodes)
    set_of_set_of_nodes.sort()
    for i in range(len(set_of_set_of_nodes)):
        l = Label(win_inc_m, text=set_of_set_of_nodes[i])
        l.grid(row=i + 1, column=0, sticky=E)

    for row in range(len(set_of_set_of_nodes)):
        for column in range(len(list_edg)):
            if list_edg[column][0] == set_of_set_of_nodes[row] and list_edg[column][1] == set_of_set_of_nodes[row]:
                l = Label(win_inc_m, text="±1")
                l.grid(row=row + 1, column=column + 1)
            elif list_edg[column][0] == set_of_set_of_nodes[row]:
                l = Label(win_inc_m, text="+1")
                l.grid(row=row + 1, column=column + 1)
            elif list_edg[column][1] == set_of_set_of_nodes[row]:
                l = Label(win_inc_m, text="-1")
                l.grid(row=row + 1, column=column + 1)
            else:
                l = Label(win_inc_m, text="0")
                l.grid(row=row + 1, column=column + 1)

    win_adj_m = Toplevel(root)
    win_adj_m.title("Matrix of adjacent")
    for i in range(len(set_of_set_of_nodes)):
        l = Label(win_adj_m, text=set_of_set_of_nodes[i])
        l.grid(row=i + 1, column=0, sticky=E)
        l = Label(win_adj_m, text=set_of_set_of_nodes[i])
        l.grid(row=0, column=i + 1, sticky=E)

    for row in range(len(set_of_set_of_nodes)):
        for column in range(len(set_of_set_of_nodes)):
            if [set_of_set_of_nodes[row], set_of_set_of_nodes[column]] in list_edg:
                l = Label(win_adj_m, text="1")
                l.grid(row=row + 1, column=column + 1)
            else:
                l = Label(win_adj_m, text="0")
                l.grid(row=row + 1, column=column + 1)

    graph = nx.DiGraph()


    for i in list_edg:
        if i[0] == i[1]:
            messagebox.showinfo("Error", "There is a loop in the graph! Please avoid it!")
            for i in range(10):
                edge.insert(END, "0")


        else:
            nx.draw(graph, with_labels=True)
            graph.add_edges_from(list_edg)
            nx.draw_circular(graph, with_labels=True)
            pl.show()



but_gr = Button(root, text="Show a graph and matrixes", command=Inc_M_and_Gr)
but_gr.grid(row=13, column=0, columnspan=13)


# BUILD GRAPH FROM INC.MATRIX

def Inc_M():
    def graph_builder():
        list_edg = []
        for i in range(len(edges)):
            list_edg.append([])
            for j in range(len(edges[i])):
                list_edg[i].append(edges[i][j].get())
        k = []
        for i in range(len(list_edg) - 1, -1, -1):
            if list_edg[i].count("0") == 10:
                list_edg.pop(i)
            elif "±1" in list_edg[i] and ("1" in list_edg[i] or "-1" in list_edg[i]):
                list_edg.pop(i)
            elif "1" in list_edg[i] and "-1" not in list_edg[i] or "-1" in list_edg[i] and "1" not in \
                    list_edg[i]:
                list_edg.pop(i)
            elif list_edg[i].count("1") > 1 or list_edg[i].count("-1") > 1 or list_edg[i].count("±1") > 1:
                list_edg.pop(i)
            else:
                if "±1" in list_edg[i]:
                    k = [list_edg[i].index("±1") + 1, list_edg[i].index("±1") + 1]
                    list_edg[i] = k
                elif "1" in list_edg[i] and "-1" in list_edg[i]:
                    k = [list_edg[i].index("1") + 1, list_edg[i].index("-1") + 1]
                    list_edg[i] = k
                else:
                    list_edg.pop(i)
        list_edg2 = deepcopy(list_edg)
        win_adj_m2 = Toplevel(root)
        win_adj_m2.title("Матриця суміжності")
        set_of_nodes = set()
        for i in list_edg2:
            for j in i:
                set_of_nodes.add(j)
        set_of_nodes = list(set_of_nodes)
        set_of_nodes.sort()
        for i in range(len(set_of_nodes)):
            lab_nodes = Label(win_adj_m2, text=set_of_nodes[i])
            lab_nodes.grid(row=i + 1, column=0, sticky=E)
            lab_nodes = Label(win_adj_m2, text=set_of_nodes[i])
            lab_nodes.grid(row=0, column=i + 1, sticky=E)
            for i in range(len(set_of_nodes)):
                for j in range(len(set_of_nodes)):
                    if [set_of_nodes[i], set_of_nodes[j]] in list_edg:
                        lab_nodes = Label(win_adj_m2)
                        lab_nodes.config(text="1")
                        lab_nodes.grid(row=i + 1, column=j + 1)
                    else:
                        lab_nodes = Label(win_adj_m2)
                        lab_nodes.config(text="0")
                        lab_nodes.grid(row=i + 1, column=j + 1)

        graph2 = nx.DiGraph()
        graph2.add_nodes_from(set_of_nodes)
        graph2.add_edges_from(list_edg)
        val_map = {}
        for i in list_edg:
            if i[0] == i[1]:
                val_map.update({i[0]: "b"})
        values = [val_map.get(node, "r") for node in graph2.nodes()]
        nx.draw(graph2, node_color=values, with_labels=True)
        pl.show()

    win_inc_m2 = Toplevel(root)
    win_inc_m2.title("Matrix of incidence")
    edges = []
    for i in range(20):
        l = Label(win_inc_m2, text="e" + str(i + 1), font=("Arial", 12))
        l.grid(row=0, column=i + 1)
    for i in range(10):
        l = Label(win_inc_m2, text=i + 1, font=("Arial", 12))
        l.grid(row=i + 1, column=0, sticky=E)
    for column in range(20):
        edges.append([])
        for row in range(10):
            edges[column].append(Inc_Matrix(win_inc_m2, row + 1, column + 1))
    but_gr = Button(win_inc_m2, text="Build a graph", command=graph_builder)
    but_gr.grid(row=13, column=0, columnspan=20)


# BUILD GRAPH FROM ADJ.MATRIX

def Adj_M():
    def graph_builder():
        list_edg = []
        for i in range(len(edges)):
            list_edg.append([])
            for j in range(len(edges[i])):
                list_edg[i].append(edges[i][j].get())
        k = []
        for i in range(len(list_edg)):
            for j in range(len(list_edg[i])):
                if list_edg[i][j] == "1":
                    k.append([str(j+1), str(i+1)])
        list_edg = k
        print(list_edg)

        graph3 = nx.DiGraph()

        graph3.add_edges_from(list_edg)
        val_map = {}
        for i in list_edg:
            if i[0] == i[1]:
                val_map.update({i[0]: "b"})
        values = [val_map.get(node, "r") for node in graph3.nodes()]
        nx.draw(graph3, node_color=values, with_labels=True)
        pl.show()

    Adjacent_mat = Toplevel(root)
    Adjacent_mat.title("Матрця суміжності")
    edges = []
    for i in range(10):
        lab = Label(Adjacent_mat, text=i + 1, font=("Arial", 12))
        lab.grid(row=0, column=i + 1)
    for i in range(10):
        lab = Label(Adjacent_mat, text=i + 1, font=("Arial", 12))
        lab.grid(row=i + 1, column=0, sticky=E)
    for column in range(10):
        edges.append([])
        for row in range(10):
            edges[column].append(Adj_Matrix(Adjacent_mat, row + 1, column + 1))
    but_gr_in = Button(Adjacent_mat, text="Build a graph", command=graph_builder)
    but_gr_in.grid(row=13, column=0, columnspan=20)


# MENU

mainmenu = Menu(root)
root.config(menu=mainmenu)
windmenu=Menu(mainmenu)
windmenu.add_command(label = "Matrix of incidence",command=Inc_M)
windmenu.add_command(label = "Matrix of adjacent",command=Adj_M)
mainmenu.add_cascade(label= "Windows", menu=windmenu)

root.mainloop()
