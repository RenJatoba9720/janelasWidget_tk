import tkinter as tk
from tkinter import messagebox, PhotoImage

# Função para calcular a média
def calcular_media():
    try:
        numero1 = float(entry1.get())
        numero2 = float(entry2.get())
        numero3 = float(entry3.get())
        media = (numero1 + numero2 + numero3) / 3
        if media < 4:
            resultado_label.config(text=f"Média: {media:.2f} \n Reprovado")
        elif media > 4 and media <= 7:
            resultado_label.config(text=f"Média: {media:.2f} \n Recuperação")
        elif media > 7:
            resultado_label.config(text=f"Média: {media:.2f} \n Aprovado")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")
    

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de Média")
root.geometry("200x300")
root.configure(background='#f0f0f0')

#Inserir uma imagem
#i = PhotoImage(file=".\image1.png")
#imge = tk.Label(root, image= i)
#imge.pack()

# Criação dos widgets
label1 = tk.Label(root, text="Número 1:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Número 2:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Número 3:")
label3.pack()

entry3 = tk.Entry(root)
entry3.pack()

calcular_button = tk.Button(root, text="Calcular Média", command=calcular_media)
calcular_button.pack()

resultado_label = tk.Label(root, text="Média:")
resultado_label.pack()

# Execução do loop principal
root.mainloop()
