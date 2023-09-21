from tkinter import *

def salvar():
    text = texto.get(1.0, END)

    with open('arquivo.txt', 'w') as file:
        file.write(text)
        texto.delete(1.0, END)
        print('Arquivo salvo com sucesso!')


def abrir():
    with open('arquivo.txt', 'r') as file:
        text = file.read()
        texto.insert(1.0, text)



window = Tk()
window.geometry("720x580+250+100")
window.title("Notepad")

panel = Frame(window, height=30)
panel.pack()

texto = Text(window, font='lucida 14')
texto.pack(expand=True, fill='both')

menubar = Menu(window)
filemenu = Menu(menubar)

filemenu.add_command(label='Abrir', command=abrir)
filemenu.add_command(label='Salvar', command=salvar)
menubar.add_cascade(label='Opções', menu=filemenu)
filemenu.add_command(label='Sair', command=window.quit)
filemenu.add_separator()

window.config(menu=menubar)

window.mainloop()