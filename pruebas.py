import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import*
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def get_location(df):
    return df['Location'].tolist()

def get_notation(df):
    return df['Notation'].tolist()

def get_dis_warehouse(df):
    return df['Distance from Warehouse (in kms)'].tolist()

def get_dis_a(df):
    return df['Distance from A'].tolist()

def get_dis_b(df):
    return df['Distance from B'].tolist()

def get_dis_c(df):
    return df['Distance from C'].tolist()

def get_dis_d(df):
    return df['Distance from D'].tolist()

def get_dis_e(df):
    return df['Distance from E'].tolist()

def get_dis_f(df):
    return df['Distance from F'].tolist()

def get_dis_g(df):
    return df['Distance from G'].tolist()

def get_dis_h(df):
    return df['Distance from H'].tolist()

def get_dis_i(df):
    return df['Distance from I'].tolist()

def select_file():
    global file, location, notation, dis, dis_w, selected_connections

    cwd = os.getcwd()
    file_types = [
        ("CSV", "*.csv"),
        ("All files", "*.*"),
    ]

    file = filedialog.askopenfilename(
        title="Select a file", initialdir=cwd, filetypes=file_types
    )
    nombre_data.insert(tk.END, file)

    if file:
        df = pd.read_csv(file, header=0)

        location = get_location(df)
        notation = get_notation(df)

        dis_w = get_dis_warehouse(df) # w of Warehouse
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
        solve_vrp()

def print_matrix(mat):
    print("Matriz de distancias:")
    for row in mat:
        for element in row:
            print(element, end='\t')
        print()

def gen_savings():
    global dis, dis_w, savings

    savings = []

    for i, rows in enumerate(dis):
        for j, element in enumerate(rows):
            if i >= j:
                continue
            max_dis = dis_w[i] + dis_w[j]
            save = max_dis - element
            savings.append((i, j, save))

    savings.sort(key=lambda x: x[2], reverse=True)

    for element in savings:
        print(element)

def solve_vrp():
    global savings, location, selected_connections

    selected_connections = []
    nodos_usados = set()

    for i, j, save in savings:
        if i in nodos_usados or j in nodos_usados:
            continue
        selected_connections.append((i, j, save))
        nodos_usados.add(i)
        nodos_usados.add(j)

    print("Conexiones seleccionadas para la solución del VRP:")
    for i, j, save in selected_connections:
        print(f"{location[i]} - {location[j]}: {save} de ahorro")

def animate_connections():
    global selected_connections, location

    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    locations = {i: (i % 5, i // 5) for i in range(len(location))}
    scat = ax.scatter([loc[0] for loc in locations.values()], [loc[1] for loc in locations.values()])

    lines = []
    annotations = []

    def update(num):
        if num < len(selected_connections):
            i, j, save = selected_connections[num]
            line, = ax.plot([locations[i][0], locations[j][0]], [locations[i][1], locations[j][1]], color='blue', linewidth=2, linestyle='-', marker='o', markersize=8)
            lines.append(line)
            annotation = ax.annotate(f"Save: {save}", ((locations[i][0] + locations[j][0]) / 2, (locations[i][1] + locations[j][1]) / 2), fontsize=8, ha='center')
            annotations.append(annotation)
        return scat, lines, annotations

    ani = animation.FuncAnimation(fig, update, frames=len(selected_connections) + 1, interval=1000, blit=False, repeat=False)

    plt.pause(0.1)  # Pausar para asegurar que la figura se muestre antes de animar
    plt.show()

root = Tk()
root.title("Problema del Enrutamiento del Vehículo")
frm = Frame(root)
frm.config(width=450, height=250)
frm.grid()
titulo = Label(frm, text="Proyecto Final VRP", font=("Verdana", 20, "bold"), bg="#031373", fg="white")
titulo.place(x=0, y=0, width=450, height=50)
marco = Label(frm, bg="#031373")
marco.place(x=0, y=0, height=250, width=25)
marco = Label(frm, bg="#031373")
marco.place(x=425, y=0, height=250, width=25)
marco = Label(frm, bg="#031373")
marco.place(x=0, y=225, height=25, width=450)
image = PhotoImage(file="Carro2.png")
FotoCar = Label(image=image)
FotoCar.place(x=185, y=60)

Texto_data = Label(frm, text="Dirección del archivo: ")
Texto_data.place(x=25, y=165, width=150, height=20)
nombre_data =Text(frm)
nombre_data.place(x=160, y=165, width=200, height=20)

boton = Button(frm, text="Select Archivo", command=select_file, font=("Arial", 8, "bold"), fg="white", activeforeground="black", bg="#43444A", activebackground="lightblue", relief="raised")
boton.place(x=160, y=195)
boton_visualizar = Button(frm, text="Visualizar Animación", command=animate_connections, font=("Arial", 8, "bold"), fg="white", activeforeground="black", bg="#43444A", activebackground="lightblue", relief="raised")
boton_visualizar.place(x=245, y=195)

root.mainloop()
