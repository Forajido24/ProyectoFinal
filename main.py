import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, Toplevel, Canvas, Frame, Label, Text, Button, PhotoImage, END
import math
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
    file_types = [("CSV", "*.csv"), ("All files", "*.*")]
    file = filedialog.askopenfilename(title="Select a file", initialdir=cwd, filetypes=file_types)
    nombre_data.insert(END, file)

    if file:
        df = pd.read_csv(file, header=0)
        location = get_location(df)
        notation = get_notation(df)
        dis_w = get_dis_warehouse(df)
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
            max_distance = dis_w[i] + dis_w[j]
            save = max_distance - element
            savings.append((i, j, save, max_distance))

    savings = sorted(savings, key=lambda x: x[2], reverse=True)
    for element in savings:
        print(element)

    solve_vrp()

def solve_vrp():
    global dis_w, savings, location, selected_connections, notation, used_nodes,total_save,total_dis

    selected_connections = []
    used_nodes = {}
    total_dis = 0
    total_save = 0

    for i, j, save, max_distance in savings:
        if i not in used_nodes:
            used_nodes[i] = 0
        if j not in used_nodes:
            used_nodes[j] = 0

        if used_nodes[i] < 2 and used_nodes[j] < 2:
            used_nodes[i] += 1
            used_nodes[j] += 1
            ij_dis = max_distance - save
            total_dis += ij_dis
            total_save += save
            selected_connections.append((i, j, ij_dis))

    independ_nodes = [key for key, value in used_nodes.items() if value == 0]
    total_dis += (sum(dis_w[i] for i in independ_nodes)) * 2

    print("Used Nodes:", used_nodes)
    print("Selected Nodes:", selected_connections)
    print("Total Distance:", total_dis)
    print("Total Save:", total_save)
    print("Independent Nodes:", independ_nodes)

    display_graph(used_nodes)

def display_graph(used_nodes):
    global location, notation, selected_connections, dis_w, dis,total_dis,total_save

    graph_window = Toplevel(root)
    graph_window.title("VRP Solution Graph")
    canvas_width = 600
    canvas_height = 600
    canvas = Canvas(graph_window, width=canvas_width, height=canvas_height, bg="#58C90E")
    canvas.pack()

    n = len(location)
    radius = 200
    center_x = canvas_width // 2
    center_y = canvas_height // 2
    angle_gap = 2 * math.pi / n
    node_positions = []

    for i in range(n):
        angle = i * angle_gap
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        node_positions.append((x, y))
        canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="#071671",width=3)
        canvas.create_text(x, y - 15, text=notation[i], fill="black",width=3)
	
    # Dibujar el nodo central (Warehouse)
    print("Total Distance:", total_dis)
    print("Total Save:", total_save)
    
    canvas.create_rectangle(450, 450, 650, 650, fill="white")
    canvas.create_text(492, 465, text="Ahorro total:", fill="black",font=("Arial",10,"bold"))
    canvas.create_text(500, 480, text=total_save, fill="black",font=("Arial",10,"bold"))
    canvas.create_text(500, 495, text="Distancia total:", fill="black",font=("Arial",10,"bold"))
    canvas.create_text(500, 510, text=total_dis, fill="black",font=("Arial",10,"bold"))
    canvas.create_oval(center_x - 10, center_y - 10, center_x + 10, center_y + 10, fill="#7B1799",width=3)
    canvas.create_text(center_x, center_y - 15, text="Warehouse", fill="black",font=("Arial",10,"bold"))

    # Conectar Warehouse con nodos G, A y F y mostrar distancias
    connections = [(center_x, center_y, node_positions[6][0], node_positions[6][1], dis_w[6], "G"),
                   (center_x, center_y, node_positions[0][0], node_positions[0][1], dis_w[0], "A"),
                   (center_x, center_y, node_positions[5][0], node_positions[4][1], dis_w[5], "E")]

    for (x1, y1, x2, y2, distance, label) in connections:
        canvas.create_line(x1, y1, x2, y2, fill="#3B3B2F",width=6)
        canvas.create_line(x1, y1, x2, y2, fill="#E7DD0A",width=1, dash=(4, 4))
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        canvas.create_text(mid_x, mid_y, text=f"{distance} km", fill="black",font=("Arial",14,"bold"))

    for i, j, distance in selected_connections:
        x1, y1 = node_positions[i]
        x2, y2 = node_positions[j]
        canvas.create_line(x1, y1, x2, y2, fill="#3B3B2F",width=6)
        canvas.create_line(x1, y1, x2, y2, fill="#E7DD0A",width=1, dash=(4, 4))
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        canvas.create_text(mid_x, mid_y, text=f"{distance} km", fill="black",font=("Arial",10,"bold"))

    for i in range(len(location)):
        if used_nodes[i] == 0:
            x, y = node_positions[i]
            canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="#071671")
            canvas.create_text(x, y - 15, text=notation[i], fill="black",width=2)

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
nombre_data = Text(frm)
nombre_data.place(x=160, y=165, width=200, height=20)

boton = Button(frm, text="Seleccionar archivo", command=select_file, font=("Arial", 10, "bold"), fg="white", activeforeground="black", bg="#43444A", activebackground="lightblue", relief="raised")
boton.place(x=180, y=195)
root.mainloop()
