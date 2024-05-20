from tkinter import Tk, Frame, Label, Button

def select_file():
    # Implementar la lógica para seleccionar el archivo
    pass

def gui():
    root = Tk()
    root.title("Desafío VRP")
    
    # Configuración del marco principal
    frm = Frame(root)
    frm.config(width=400, height=300)
    frm.grid(sticky="nsew")
    
    # Configuración del grid para centrar los elementos
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    # Título grande con fuente modificada
    titulo = Label(frm, text="Desafío VRP", font=("Verdana", 20, "bold"))
    titulo.grid(row=0, column=0, pady=(50, 10), padx=10, sticky="n")
    
    # Botón centrado con estilo modificado
    boton = Button(frm, 
                   text="Seleccionar Archivo", 
                   command=select_file, 
                   font=("Verdana", 16, "bold"), 
                   bg="blue", 
                   fg="white", 
                   activebackground="lightblue", 
                   activeforeground="black", 
                   relief="raised", 
                   bd=5,
                   width=20,     # Ancho del botón
                   height=2,     # Altura del botón
                   padx=10,      # Espacio adicional horizontal
                   pady=10,      # Espacio adicional vertical
                   anchor="center"  # Alineación del texto en el centro
                   )
    boton.grid(row=1, column=0, pady=10)
    
    # Espaciador opcional para el botón (si quieres que el botón esté más centrado verticalmente)
    frm.grid_rowconfigure(3, weight=1)
    
    root.mainloop()

gui()
