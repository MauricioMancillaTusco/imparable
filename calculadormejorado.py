import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        a = float(entrada1.get())
        b = float(entrada2.get())
        operacion = operacion_var.get()

        if operacion == "Sumar":
            resultado = a + b
        elif operacion == "Restar":
            resultado = a - b
        elif operacion == "Multiplicar":
            resultado = a * b
        elif operacion == "Dividir":
            if b == 0:
                raise ZeroDivisionError
            resultado = a / b
        else:
            resultado = "Operación no válida"

        resultado_var.set(f"Resultado: {resultado}")
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir entre cero.")
    except ValueError:
        messagebox.showerror("Error", "Introduce números válidos.")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.geometry("300x200")

# Variables
operacion_var = tk.StringVar(value="Sumar")
resultado_var = tk.StringVar()

# Entradas y etiquetas
tk.Label(ventana, text="Número 1:").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Número 2:").pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Label(ventana, text="Operación:").pack()
opciones = ["Sumar", "Restar", "Multiplicar", "Dividir"]
tk.OptionMenu(ventana, operacion_var, *opciones).pack()

tk.Button(ventana, text="Calcular", command=calcular).pack(pady=5)
tk.Label(ventana, textvariable=resultado_var, font=("Arial", 12)).pack()

# Ejecutar
ventana.mainloop()
