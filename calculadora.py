import tkinter as tk
from tkinter import * 

#Corpo da calculadora
root = tk.Tk()
root.title('Protótipo_Calculadora')
root.geometry('408x400')
root.minsize(408, 400)
root.maxsize(408, 400)
root.configure(background='#212e44')
root.resizable(False, False)
root.attributes('-alpha', 0.9) #Grau de transparência

numero1 = ''
divisao = False
multiplicacao = False
adicao = False
subtracao = False

#Entrada da calculadora
e = Entry(root, width= 15, relief = FLAT, borderwidth= 4, bg='#008FFF', font=('futura', 25, 'bold'), justify= CENTER)

e.grid(row=0,
        column=0,
        columnspan=4,
        pady=2,
)
#Função de mudança de cor protótipo
def new_tema():
    root.configure(background ='#000000')
    return

tema = Button(root,
                text ="TE",
                padx = 85,
                pady = 8,
                command = new_tema,
                fg ='#FFFFFF',
                activeforeground ='#0080FF',
                bg ='#320064',
                activebackground ='#240046',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
tema.grid(row = 5, column = 1, columnspan = 2)

def tema_padrao():
    root.configure(background='#FFFFFF')
    return

padrao = Button(root,
                text ="TP",
                padx = 85,
                pady = 8,
                command = tema_padrao,
                fg ='#FFFFFF',
                activeforeground ='#0080FF',
                bg ='#320064',
                activebackground ='#240046',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
padrao.grid(row = 5, column = 3, columnspan= 5)

#Funções das operações
def botao_click(num):
    e.insert(END, num)
    return

def botao_divisao():
    global numero1
    global divisao
    divisao = True
    numero1 = e.get()
    e.delete(0, END)
    return

def botao_multiplicacao():
    global numero1
    global multiplicacao
    multiplicacao = True
    numero1 = e.get()
    e.delete(0, END)
    return

def botao_subtracao():
    global numero1
    global subtracao
    subtracao = True
    numero1 = e.get()
    e.delete(0, END)
    return

def botao_adicao():
    global numero1
    global adicao
    adicao = True
    numero1 = e.get()
    e.delete(0, END)
    return

def botao_clear():
    multiplicacao = False
    divisao = False
    adicao = False
    subtracao = False
    e.delete(0, END)
    return

def botao_igual():
    global divisao
    global multiplicacao
    global subtracao
    global adicao
    numero2 =e.get()
    e.delete(0, END)
    if divisao == True:
        e.insert(0, float(numero1) / float(numero2))
        divisao = False
    
    if multiplicacao == True:
        e.insert(0, float(numero1) * float(numero2))
        multiplicacao = False
    
    if subtracao == True:
        e.insert(0, float(numero1) - float(numero2))
        subtracao = False
    
    if adicao == True:
        e.insert(0, float(numero1) + float(numero2))
        adicao = False
    return


#Botões das operações
divisao = Button(root,
                text ="÷",
                padx = 40,
                pady = 20,
                command = botao_divisao,
                fg ='#FFFFFF',
                activeforeground ='#0080FF',
                bg ='#320064',
                activebackground ='#240046',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
divisao.grid(row = 0, column = 4)

multiplicacao = Button(root,
                text ="×",
                padx = 40,
                pady = 20,
                command = botao_multiplicacao,
                fg ='#FFFFFF',
                activeforeground ='#0080FF',
                bg ='#320064',
                activebackground ='#240046',
                relief = FLAT,
                font = ('futura',12, 'bold')
)
multiplicacao.grid(row = 1, column = 4)

adicao = Button(root,
                text = "+",
                padx = 40,
                pady = 20,
                command = botao_adicao,
                fg ='#FFFFFF',
                activeforeground ='#0080FF',
                bg ='#320064',
                activebackground ='#240046',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
adicao.grid(row = 3, column = 4)

subtracao = Button(root,
                text = "-",
                padx = 41.5,
                pady = 20,
                command = botao_subtracao,
                fg ='#FFFFFF',
                activeforeground ='#0080FF',
                bg ='#320064',
                activebackground ='#240046',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
subtracao.grid(row = 2, column = 4)

clear = Button(root,
                text = "C",
                padx = 39,
                pady = 20,
                command = botao_clear,
                fg ='#FFFFFF',
                activeforeground ='#0080FF',
                bg ='#320064',
                activebackground ='#240046',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
clear.grid(row = 4, column = 4)

igual = Button(root,
                text = "=",
                padx = 40,
                pady = 20,
                command = botao_igual,
                fg ='#FFFFFF',
                activeforeground ='#0080FF',
                bg ='#320064',
                activebackground ='#240046',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
igual.grid(row = 4, column = 3)

#Botões das numerações
um = Button(root,
                text = "1",
                padx = 40,
                pady = 20,
                command = lambda: botao_click(1),
                fg ='#FFFFFF',
                activeforeground ='#0080FF',
                bg ='#320064',
                activebackground ='#240046',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
um.grid(row = 3, column = 1)

dois = Button(root,
                text = "2",
                padx = 40,
                pady = 20,
                command = lambda: botao_click(2),
                fg ='#FFFFFF',
                activeforeground ='#0080FF',
                bg ='#320064',
                activebackground ='#240046',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
dois.grid(row = 3, column = 2)

tres = Button(root,
                text = "3",
                padx = 40,
                pady = 20,
                command = lambda: botao_click(3),
                fg ='#FFFFFF',
                activeforeground ='#0080FF',
                bg ='#320064',
                activebackground ='#240046',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
tres.grid(row = 3, column = 3)

quatro = Button(root,
                text = "4",
                padx = 40,
                pady = 20,
                command = lambda: botao_click(4),
                fg ='#FFFFFF',
                activeforeground ='#0080FF',
                bg ='#320064',
                activebackground ='#240046',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
quatro.grid(row = 2, column = 1)

cinco = Button(root,
                text = "5",
                padx = 40,
                pady = 20,
                command = lambda: botao_click(5),
                fg ='#FFFFFF',
                activeforeground ='#0080FF',
                bg ='#320064',
                activebackground ='#240046',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
cinco.grid(row = 2, column = 2)

seis = Button(root,
                text = "6",
                padx = 40,
                pady = 20,
                command = lambda: botao_click(6),
                fg ='#FFFFFF',
                activeforeground ='#0080FF',
                bg ='#320064',
                activebackground ='#240046',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
seis.grid(row = 2, column = 3)

sete = Button(root,
                text = "7",
                padx = 40,
                pady = 20,
                command = lambda: botao_click(7),
                fg ='#FFFFFF',
                activeforeground ='#0080FF',
                bg ='#320064',
                activebackground ='#240046',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
sete.grid(row = 1, column = 1)

oito = Button(root,
                text = "8",
                padx = 40,
                pady = 20,
                command = lambda: botao_click(8),
                fg ='#FFFFFF',
                activeforeground ='#0080FF',
                bg ='#320064',
                activebackground ='#240046',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
oito.grid(row = 1, column = 2)

nove = Button(root,
                text = "9",
                padx = 40,
                pady = 20,
                command = lambda: botao_click(9),
                fg ='#FFFFFF',
                activeforeground ='#0080FF',
                bg ='#320064',
                activebackground ='#240046',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
nove.grid(row = 1, column = 3)

zero = Button(root,
                text = "0",
                padx = 91,
                pady = 20,
                command = lambda: botao_click(0),
                fg ='#FFFFFF',
                activeforeground ='#0080FF',
                bg ='#320064',
                activebackground ='#240046',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
zero.grid(row = 4, column = 1, columnspan = 2)

root.mainloop()