from tkinter import *
janelaPrincipal = Tk()
janelaPrincipal.title('Calculadora')

#funcoes
def inserir(valor):
    visor.insert(END, valor)


def limpar():
    visor.delete(0, END)

def calcular():
    texto_visor = visor.get() #pegar os numeros
    resultado = eval(texto_visor) #calcular o que tiver dentro do valor
    visor.delete(0, END)
    visor.insert(0, str(resultado))



#Visor - EXIBIR OS NUMEROS
visor = Entry(janelaPrincipal, font= 'Arial 20 bold',
              bg = '#000000', fg='#FFFFFF', width=25)
visor.pack()

#Criar um painel para inserir os botoes
painel = Frame(janelaPrincipal)

#Criar Butoes
botao0 = Button(painel, bg='#000000',
                bd= 1, text='0', font='Arial 16 bold', fg= '#FFFFFF',
                width=5, height=3,
                command= lambda: inserir('0'))

botao1 = Button(painel, bg='#000000',
                bd= 1, text='1', font='Arial 16 bold', fg= '#FFFFFF',
                width=5, height=3,
                command= lambda: inserir('1'))

botao2 = Button(painel, bg='#000000',
                bd= 1, text='2', font='Arial 16 bold', fg= '#FFFFFF',
                width=5, height=3,
                command= lambda: inserir('2'))
botao3 = Button(painel, bg='#000000',
                bd= 1, text='3', font='Arial 16 bold', fg= '#FFFFFF',
                width=5, height=3,
                command= lambda: inserir('3'))
botao4 = Button(painel, bg='#696969',
                bd= 1, text='4', font='Arial 16 bold', fg= '#FFFFFF',
                width=5, height=3,
                command= lambda: inserir('4'))
botao5 = Button(painel, bg='#000000',
                bd= 1, text='5', font='Arial 16 bold', fg= '#FFFFFF',
                width=5, height=3,
                command= lambda: inserir('5'))
botao6 = Button(painel, bg='#000000',
                bd= 1, text='6', font='Arial 16 bold', fg= '#FFFFFF',
                width=5, height=3,
                command= lambda: inserir('6'))
botao7 = Button(painel, bg='#000000',
                bd= 1, text='7', font='Arial 16 bold', fg= '#FFFFFF',
                width=5, height=3,
                command= lambda: inserir('7'))
botao8 = Button(painel, bg='#000000',
                bd= 1, text='8', font='Arial 16 bold', fg= '#FFFFFF',
                width=5, height=3,
                command= lambda: inserir('8'))
botao9 = Button(painel, bg='#000000',
                bd= 1, text='9', font='Arial 16 bold', fg= '#FFFFFF',
                width=5, height=3,
                command= lambda: inserir('9'))
botaoSubtrair = Button(painel, bg='#FF8C00',
                bd= 1, text='-', font='Arial 16 bold', fg= '#000000',
                width=5, height=3,
                command= lambda: inserir('-'))

botaoDividir = Button(painel, bg='#FF8C00',
                bd= 1, text='/', font='Arial 16 bold', fg= '#000000',
                width=5, height=3,
                command= lambda: inserir('/'))
botaoMultiplicar = Button(painel, bg='#FF8C00',
                bd= 1, text='*', font='Arial 16 bold', fg= '#000000',
                width=5, height=3,
                command= lambda: inserir('*'))

botaoSoma = Button(painel, bg='#FF8C00',
                bd= 1, text='+', font='Arial 16 bold', fg= '#000000',
                width=5, height=3,
                command= lambda: inserir('+'))

botaoIgual = Button(painel, bg='#FF8C00',
                bd= 1, text='=', font='Arial 16 bold', fg= '#000000',
                width=5, height=3,
                command= lambda: calcular())

botaoZerar = Button(painel, bg='#FF8C00',
                bd= 1, text='C', font='Arial 16 bold', fg= '#000000',
                width=5, height=3,
                command=lambda: limpar())


#Ativar Painel
painel.pack()

#Primeira Linha
botao7.grid(row=0,column=0)
botao8.grid(row=0,column=1)
botao9.grid(row=0,column=2)
botaoDividir.grid(row=0,column=3)
#Segunda Linha
botao4.grid(row=1,column=0)
botao5.grid(row=1,column=1)
botao6.grid(row=1,column=2)
botaoMultiplicar.grid(row=1,column=3)


#Terceira Linha
botao1.grid(row=2, column=0)
botao2.grid(row=2, column=1)
botao3.grid(row=2, column=2)
botaoSoma.grid(row=2, column=3)
#Quarta Linha
botao0.grid(row=3, column=0)
botaoIgual.grid(row=3, column=1)
botaoZerar.grid(row=3,column=2)
botaoSubtrair.grid(row=3, column=3)



mainloop()