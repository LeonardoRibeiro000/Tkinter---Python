import tkinter as tk
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

#dialogos simples - simpledialog

#3 tipos de classes para dialogo simples

#valores do tipo float
valor = tk.simpledialog.askfloat(title="Valor", prompt="Digite o valor do produto")
tk.messagebox.showinfo(title="Resultado", message= f"O valor do produto é: {valor}")

#valores do tipo int
idade = tk.simpledialog.askinteger(title="Idade", prompt="Qual a sua idade?")
tk.messagebox.showinfo(title="Idade", message=f"a idade do funcionário é: {idade}")


#valores do tipo string
nome = tk.simpledialog.askstring(title="Nome", prompt="Digite seu nome completo")
tk.messagebox.showinfo(title="Nome do funcionário", message=f"O nome do funcionário é: {nome}")

tk.messagebox.askquestion(title = "Dados", message= f"Os dados abaixo estão corretos? \nValor: {valor} \nIdade: {idade} \nNome: {nome}")


#As três funções acima fornecem caixas de diálogo que solicitam que o usuário insira um valor do tipo desejado.