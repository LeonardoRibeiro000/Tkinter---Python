#messagebox
import tkinter as tk
from tkinter import messagebox


#exibir informações
tk.messagebox.showinfo(title="Info", message="Se liga nessa informação quentinha")

#exibir alerta/aviso/erro

tk.messagebox.showwarning(title="Alerta", message="Cuidado nas costas")
tk.messagebox.showerror(title="Erro", message="Cuidado nas costas")


#perguntas
continuar = tk.messagebox.askquestion(title="Pergunta", message="Deseja continuar?")
print(continuar)

#recuperar valores 
if continuar == 'yes':
    tk.messagebox.showerror(title="Error", message="tu é twonga")
else:
    tk.messagebox.showerror(title="Error", message="tu é twonga de novo")
    
tk.messagebox.askokcancel(title="ok", message="Deseja continuar?")