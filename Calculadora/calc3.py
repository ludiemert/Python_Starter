# Calculadora com Interface Gráfica usando tkinter

# executar o programa PS C:\Users\user\Downloads\Computer_Vision_Py\Calculadora> python calc3.py

# Cria uma interface gráfica com botões numéricos e operadores matemáticos.
#Usa o evento de clique para capturar entradas e realizar operações, Exibe o resultado na tela da interface gráfica.

import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result.set(eval(screen.get()))
            screen.update()
        except Exception:
            result.set("Erro")
    elif text == "C":
        result.set("")
        screen.update()
    else:
        result.set(result.get() + text)
        screen.update()

# Configuração da janela
root = tk.Tk()
root.title("Calculadora")

result = tk.StringVar()
result.set("")
screen = tk.Entry(root, textvar=result, font="Arial 20", justify="right")
screen.grid(row=0, column=0, columnspan=4)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Criar botões
row, col = 1, 0
for button in buttons:
    b = tk.Button(root, text=button, font="Arial 15", height=2, width=5)
    b.grid(row=row, column=col, padx=5, pady=5)
    b.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
