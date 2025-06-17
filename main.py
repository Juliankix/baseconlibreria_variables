import sqlite3
import customtkinter as ctk
from tkinter import messagebox

conn = sqlite3.connect('basedatos.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL,
    direccion TEXT NOT NULL,
    telefono TEXT NOT NULL
);
""")
conn.commit()

def guardar_cliente():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()

    if nombre and correo and direccion and telefono:
        cursor.execute("INSERT INTO clientes (nombre, correo, direccion, telefono) VALUES (?, ?, ?, ?)",
                       (nombre, correo, direccion, telefono))
        conn.commit()
        messagebox.showinfo("Éxito", "Cliente guardado")
        limpiar_campos()
    else:
        messagebox.showwarning("Faltan datos", "Completa todos los campos")

def ver_clientes():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    texto = "\n".join([f"{c[0]} - {c[1]} - {c[2]}" for c in clientes])
    messagebox.showinfo("Clientes", texto if texto else "No hay clientes")

def detalle_cliente():
    id_cliente = entry_id.get()
    if id_cliente:
        cursor.execute("SELECT * FROM clientes WHERE id=?", (id_cliente,))
        cliente = cursor.fetchone()
        if cliente:
            texto = f"""
ID: {cliente[0]}
Nombre: {cliente[1]}
Correo: {cliente[2]}
Dirección: {cliente[3]}
Teléfono: {cliente[4]}
"""
            messagebox.showinfo("Detalle del Cliente", texto)
        else:
            messagebox.showwarning("No encontrado", "No existe cliente con ese ID")
    else:
        messagebox.showwarning("Falta ID", "Ingresa el ID para ver detalles")


def actualizar_cliente():
    id_cliente = entry_id.get()
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()

    if id_cliente and nombre and correo and direccion and telefono:
        cursor.execute("""UPDATE clientes SET nombre=?, correo=?, direccion=?, telefono=? WHERE id=?""",
                       (nombre, correo, direccion, telefono, id_cliente))
        conn.commit()
        messagebox.showinfo("Éxito", "Cliente actualizado")
        limpiar_campos()
    else:
        messagebox.showwarning("Faltan datos", "Completa todos los campos e ID")

def eliminar_cliente():
    id_cliente = entry_id.get()
    if id_cliente:
        cursor.execute("DELETE FROM clientes WHERE id=?", (id_cliente,))
        conn.commit()
        messagebox.showinfo("Éxito", "Cliente eliminado")
        entry_id.delete(0, ctk.END)
    else:
        messagebox.showwarning("Falta ID", "Ingresa el ID del cliente a eliminar")

def limpiar_campos():
    entry_id.delete(0, ctk.END)
    entry_nombre.delete(0, ctk.END)
    entry_correo.delete(0, ctk.END)
    entry_direccion.delete(0, ctk.END)
    entry_telefono.delete(0, ctk.END)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("CRUD Clientes")
ventana.geometry("400x600")

ctk.CTkLabel(ventana, text="ID (para actualizar o eliminar)").pack(pady=5)
entry_id = ctk.CTkEntry(ventana, width=300)
entry_id.pack()

ctk.CTkLabel(ventana, text="Nombre").pack(pady=5)
entry_nombre = ctk.CTkEntry(ventana, width=300)
entry_nombre.pack()

ctk.CTkLabel(ventana, text="Correo").pack(pady=5)
entry_correo = ctk.CTkEntry(ventana, width=300)
entry_correo.pack()

ctk.CTkLabel(ventana, text="Dirección").pack(pady=5)
entry_direccion = ctk.CTkEntry(ventana, width=300)
entry_direccion.pack()

ctk.CTkLabel(ventana, text="Teléfono").pack(pady=5)
entry_telefono = ctk.CTkEntry(ventana, width=300)
entry_telefono.pack()

ctk.CTkButton(ventana, text="Guardar Cliente", command=guardar_cliente).pack(pady=10)
ctk.CTkButton(ventana, text="Ver Clientes", command=ver_clientes).pack(pady=5)
ctk.CTkButton(ventana, text="Detalle Cliente", command=detalle_cliente).pack(pady=5)
ctk.CTkButton(ventana, text="Actualizar Cliente", command=actualizar_cliente).pack(pady=5)
ctk.CTkButton(ventana, text="Eliminar Cliente", command=eliminar_cliente).pack(pady=5)

ventana.mainloop()
