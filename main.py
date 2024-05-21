import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import *


def get_location(df):
    return df["Location"].tolist()


def get_notation(df):
    return df["Notation"].tolist()


def get_dis_warehouse(df):
    return df["Distance from Warehouse (in kms)"].tolist()


def get_dis_a(df):
    return df["Distance from A"].tolist()


def get_dis_b(df):
    return df["Distance from B"].tolist()


def get_dis_c(df):
    return df["Distance from C"].tolist()


def get_dis_d(df):
    return df["Distance from D"].tolist()


def get_dis_e(df):
    return df["Distance from E"].tolist()


def get_dis_f(df):
    return df["Distance from F"].tolist()


def get_dis_g(df):
    return df["Distance from G"].tolist()


def get_dis_h(df):
    return df["Distance from H"].tolist()


def get_dis_i(df):
    return df["Distance from I"].tolist()


def select_file():
    global file, location, notation, dis, dis_w

    cwd = os.getcwd()
    file_types = [
        ("CSV", "*.csv"),
        ("All files", "*.*"),
    ]

    file = filedialog.askopenfilename(
        title="Select a file", initialdir=cwd, filetypes=file_types
    )
    nombre_data.insert(END, file)

    if file:
        df = pd.read_csv(file, header=0)

        location = get_location(df)
        notation = get_notation(df)

        dis_w = get_dis_warehouse(df)  # w of Warehouse
        dis = [get_dis_a(df)]
        dis.append(get_dis_b(df))
        dis.append(get_dis_c(df))
        dis.append(get_dis_d(df))
        dis.append(get_dis_e(df))
        dis.append(get_dis_f(df))
        dis.append(get_dis_g(df))
        dis.append(get_dis_h(df))
        dis.append(get_dis_i(df))

        print_matrix(dis)
        gen_savings()


def print_matrix(mat):
    for row in mat:
        for element in row:
            print(element, end="\t")

        print()


def gen_savings():
    global dis, dis_w, savings

    savings = []

    for i, rows in enumerate(dis):
        for j, element in enumerate(rows):
            if i >= j:
                continue
            max = dis_w[i] + dis_w[j]
            save = max - element
            savings.append((i, j, save))

    savings = sorted(savings, key=lambda x: x[2], reverse=True)

    for element in savings:
        print(element)


root = Tk()
root.title("Problema del Enrutamiento del Vehículo")
frm = Frame(root)
frm.config(width=450, height=250)
frm.grid()
titulo = Label(
    frm,
    text="Proyecto Final VRP",
    font=("Verdana", 20, "bold"),
    bg="#031373",
    fg="white",
)
titulo.place(x=0, y=0, width=450, height=50)
marco = Label(frm, bg="#031373")
marco.place(x=0, y=0, height=250, width=25)
marco = Label(frm, bg="#031373")
marco.place(x=425, y=0, height=250, width=25)
marco = Label(frm, bg="#031373")
marco.place(x=0, y=225, height=25, width=450)
image = tk.PhotoImage(file="Carro2.png")
FotoCar = Label(image=image)
FotoCar.place(x=185, y=60)


Texto_data = Label(frm, text="Dirección del archivo: ")
Texto_data.place(x=25, y=165, width=150, height=20)
nombre_data = Text(frm)
nombre_data.place(x=160, y=165, width=200, height=20)

boton = Button(
    frm,
    text="Select File",
    command=select_file,
    font=("Arial", 10, "bold"),
    fg="white",
    activeforeground="black",
    bg="#43444A",
    activebackground="lightblue",
    relief="raised",
)
boton.place(x=195, y=195)
root.mainloop()
