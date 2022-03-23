#############################################################################
# Nome: Aula 25 (Teoria) - GUI 
# Autor: Rafael Machado                                               
# Data: 03/11/2021                                                    
# Resumo: Exercícios sobre Interface Gráfica
#############################################################################
from tkinter import *
from tkinter import messagebox
##############
# Exemplo
#
# Cria a janela
janela = Tk()
# Tamanho da Janela
janela.geometry("400x400")
# Título
janela.title("Exemplo")
#
rotulo = Label(janela, text="Primeiro texto, GUI!", font=("Arial Bold", 20))
rotulo.place(relx = 0.5, rely = 0.25, anchor = CENTER),
#
def Clique():
    rotulo["text"] = entrada.get()
    messagebox.showinfo("Aviso!", "Botão Pressionado!")
    resposta = messagebox.askyesno("Pergunta", "Python é legal?")
    print (resposta)

botao = Button(janela, text = "Clique aqui!", font = 20, command = Clique)
botao.place(relx = 0.5, rely = 0.75, anchor = CENTER)
#
entrada = Entry(janela, width = 20, font = ("Times New Roman", 20))
entrada.place(relx = 0.5, rely = 0.5, anchor = CENTER)
# Mantém a janela aberta até clicar no "x"
janela.mainloop()

##############
# Exemplo 2
#
window = Tk()
window.title("Soma 2 números")
window.geometry("600x300")

rot1 = Label(window, text = "Digite o 1º número:", font = ("Arial", 16))
rot1.place(relx = 0.5, rely = 0.2, anchor = NE)

rot2 = Label(window, text = "Digite o 2º número:", font = ("Arial", 16))
rot2.place(relx = 0.5, rely = 0.4, anchor = NE)

rot3 = Label(window, text = "Resultado:", font = ("Arial", 16))
rot3.place(relx = 0.5, rely = 0.6, anchor = NE)

ent1 = Entry(window, width = 10, font = ("Arial", 16))
ent1.place(relx = 0.55, rely = 0.2)

ent2 = Entry(window, width = 10, font = ("Arial", 16))
ent2.place(relx = 0.55, rely = 0.4)

ent3 = Entry(window, width = 10, font = ("Arial", 16), state = DISABLED)
ent3.place(relx = 0.55, rely = 0.6)

def soma ():
    ent3["state"] = NORMAL
    ent3.delete(0, END)
    resultado = int(ent1.get()) + int(ent2.get())
    ent3.insert(0, resultado)
    ent3["state"] = DISABLED
botao = Button(window, text = "Somar", font = ("Arial", 16), command = soma)
botao.place(relx = 0.4, rely = 0.8, anchor = CENTER)
def clear ():
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
botao = Button(window, text = "Clear", font = ("Arial", 16), command = clear)
botao.place(relx = 0.6, rely = 0.8, anchor = CENTER)

window.mainloop()

##############
# Exercício 1
# Resumo: Conversor de bases
from functools import partial
window = Tk()
window.title("Conversor de Bases")
window.geometry("600x300")

texto1 = Label(window, text = "Número decimal:", font = ("Arial", 16))
texto1.place(relx = 0.25, rely = 0.2, anchor = W)

caixa1 = Entry(window, width = 10, font = ("Arial", 16), justify = CENTER)
caixa1.place(relx = 0.53, rely = 0.2, anchor = W)

texto2 = Label(window, text = "Resposta:", font = ("Arial", 16))
texto2.place(relx = 0.31, rely = 0.8, anchor = W)

caixa2 = Entry(window, width = 10, font = ("Arial", 16), justify = CENTER, state = DISABLED)
caixa2.place(relx = 0.49, rely = 0.8, anchor = W)

def conversao (base):
    caixa2["state"] = NORMAL
    caixa2.delete(0, END)
    numero = int(caixa1.get())
    numero = eval(base)(numero)
    caixa2.insert(0, numero)
    caixa2["state"] = DISABLED 

botao = Button(window, text = "Binário", font = ("Arial", 16), command = partial(conversao, "bin"))
botao.place(relx = 0.2, rely = 0.5, anchor = W)

botao = Button(window, text = "Hexadecimal", font = ("Arial", 16), command = partial(conversao, "hex"))
botao.place(relx = 0.51, rely = 0.5, anchor = CENTER)

botao = Button(window, text = "Octal", font = ("Arial", 16), command = partial(conversao, "oct"))
botao.place(relx = 0.8, rely = 0.5, anchor = E)

window.mainloop()

##############
# Exercício 2
# Resumo: 
from functools import partial
window = Tk()
window.title("Conversor de Bases")
window.geometry("600x300")

texto1 = Label(window, text = "Digite uma Letra:", font = ("Arial", 16))
texto1.place(relx = 0.5, rely = 0.3, anchor = E)

caixa1 = Entry(window, width = 10, font = ("Arial", 16), justify = CENTER)
caixa1.place(relx = 0.5, rely = 0.3, anchor = W)
vogais = ["a", "e", "i", "o", "u"]
def testar ():
    letra = str(caixa1.get()).lower()
    if 0 >= len(letra) > 1:
        messagebox.showerror("Erro!", "Digite apenas uma letra!")
    else:
        if letra in vogais:
            messagebox.showinfo("Vogal", "A letra digitada foi uma vogal!")
        elif letra == "y":
            messagebox.showinfo("Corta pros dois lados", "A letra é usada como vogal ou consoante, dependendo da língua!")
        else:
            messagebox.showinfo("Consoante", "A letra digitada foi uma consoante!")
    entrada.delete(0, END)

botao = Button(window, text = "Testar", font = ("Arial", 16), command = testar)
botao.place(relx = 0.5, rely = 0.7, anchor = CENTER)

window.mainloop()

##############
# Exercício 3
# Resumo: Não Finalizado
from functools import partial
window = Tk()
window.title("Conversor de Bases")
window.geometry("500x500")

caixa = Entry(window, width = 10, font = ("Arial", 16), justify = CENTER)
caixa.place(relx = 0.53, rely = 0.2, anchor = W)

def conversao (base):
    caixa2["state"] = NORMAL
    caixa2.delete(0, END)
    numero = int(caixa1.get())
    numero = eval(base)(numero)
    caixa2.insert(0, numero)
    caixa2["state"] = DISABLED 

botao1 = Button(window, text = "1", font = ("Arial", 16))
botao1.place(relx = 0.2, rely = 0.5, anchor = CENTER)

botao2 = Button(window, text = "2", font = ("Arial", 16))
botao2.place(relx = 0.51, rely = 0.5, anchor = CENTER)

botao3 = Button(window, text = "3", font = ("Arial", 16))
botao3.place(relx = 0.8, rely = 0.5, anchor = CENTER)

botao4 = Button(window, text = "4", font = ("Arial", 16))
botao4.place(relx = 0.2, rely = 0.5, anchor = CENTER)

botao5 = Button(window, text = "5", font = ("Arial", 16))
botao5.place(relx = 0.51, rely = 0.5, anchor = CENTER)

botao6 = Button(window, text = "6", font = ("Arial", 16))
botao6.place(relx = 0.8, rely = 0.5, anchor = CENTER)

botao7 = Button(window, text = "7", font = ("Arial", 16))
botao7.place(relx = 0.2, rely = 0.5, anchor = CENTER)

botao8 = Button(window, text = "8", font = ("Arial", 16))
botao8.place(relx = 0.51, rely = 0.5, anchor = CENTER)

botao9 = Button(window, text = "9", font = ("Arial", 16))
botao9.place(relx = 0.8, rely = 0.5, anchor = CENTER)

botao0 = Button(window, text = "0", font = ("Arial", 16))
botao0.place(relx = 0.2, rely = 0.5, anchor = CENTER)
#########################################################################
botao_igual = Button(window, text = "=", font = ("Arial", 16))
botao_igual.place(relx = 0.51, rely = 0.5, anchor = CENTER)

botao_mais = Button(window, text = "+", font = ("Arial", 16))
botao_mais.place(relx = 0.8, rely = 0.5, anchor = CENTER)

botao_menos = Button(window, text = "-", font = ("Arial", 16))
botao_menos.place(relx = 0.2, rely = 0.5, anchor = CENTER)

botao_vezes = Button(window, text = "x", font = ("Arial", 16))
botao_vezes.place(relx = 0.51, rely = 0.5, anchor = CENTER)

botao_dividir = Button(window, text = "/", font = ("Arial", 16))
botao_dividir.place(relx = 0.8, rely = 0.5, anchor = CENTER)

botao_apagar = Button(window, text = "C", font = ("Arial", 16))
botao_apagar.place(relx = 0.2, rely = 0.5, anchor = CENTER)

botao_seno = Button(window, text = "sen", font = ("Arial", 16))
botao_seno.place(relx = 0.51, rely = 0.5, anchor = CENTER)

botao_cosseno = Button(window, text = "cos", font = ("Arial", 16))
botao_cosseno.place(relx = 0.8, rely = 0.5, anchor = CENTER)

botao_tangente = Button(window, text = "tan", font = ("Arial", 16))
botao_tangente.place(relx = 0.8, rely = 0.5, anchor = CENTER)

botao_log = Button(window, text = "log", font = ("Arial", 16))
botao_log.place(relx = 0.2, rely = 0.5, anchor = CENTER)

botao_elevado = Button(window, text = "^", font = ("Arial", 16))
botao_elevado.place(relx = 0.51, rely = 0.5, anchor = CENTER)

botao_raiz = Button(window, text = "√", font = ("Arial", 16))
botao_raiz.place(relx = 0.8, rely = 0.5, anchor = CENTER)

window.mainloop()