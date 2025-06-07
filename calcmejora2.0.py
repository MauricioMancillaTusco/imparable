import tkinter as tk
from math import sqrt

# Función para actualizar la entrada
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "√":
        try:
            result = sqrt(float(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "^":
        entry.insert(tk.END, "**")
    else:
        entry.insert(tk.END, text)

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Crear la entrada (pantalla de la calculadora)
entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, ipady=10)

# Definir los botones
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C", "√", "^"
]

# Crear los botones en la ventana
row = 1
col = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, font="Arial 18", width=5, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Iniciar el bucle principal de la interfaz
root.mainloop()