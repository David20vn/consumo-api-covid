import tkinter as tk
from tkinter import ttk

def display_ui(df):
    """
    Crea una interfaz gráfica con Tkinter para mostrar los datos en una tabla.
    
    :param df: DataFrame de pandas a mostrar.
    """
    # Crear la ventana principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Datos de la API - Tkinter")
    ventana_principal.geometry("800x400")
    
    # Crear un frame para la tabla
    frame = ttk.Frame(ventana_principal)
    frame.pack()
    
    # Obtener las columnas del DataFrame
    columnas = list(df.columns)
    
    # Crear la tabla (Treeview)
    tabla = ttk.Treeview(frame, columns=columnas, show="headings")
    
    # Configurar los encabezados de la tabla
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=120)
    
    # Insertar cada fila del DataFrame en la tabla
    for _, row in df.iterrows():
        tabla.insert("", tk.END, values=list(row))
    
    tabla.pack()
    
    # Ejecutar la UI
    ventana_principal.mainloop()
