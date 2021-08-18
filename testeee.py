from tkinter import *
from selenium import webdriver

# Classe Tela
class Tela:
    def __init__(self):
        self.root = root 
        self.configura_tela()
        self.widgets()
        root.mainloop()

    def configura_tela(self):
        self.root.configure(bg='#00a896')
        self.root.geometry('375x667')


    def widgets(self):
        ola = Label(
            self.root,
            text='Melhor Canal ',
            bg='#ea698b',
            fg='#acd8aa',
            font=('times', 30, 'bold'))


        ola2 = Label(
            self.root,
            text='brota ',
            bg='#ff5d8f',
            fg='yellow')


        ola.place(x=60 ,y=100)
        ola2.place(x=170, y=200)


        self.btn_insta = Button(self.root,
            text= 'Araxxta pra cima bb!',
            bg='#a01a58',
            fg='#2e6f95',
            command=self.clica,
            font=('times', 15, 'bold'))
        self.btn_insta.place(x=97 , y=250, width=200, height=90)

        self.btn_fecha = Button(
            self.root,
            text='X',
            bg='red',
            command=self.fechar
        )
        self.btn_fecha.place(x=10, y=10, height=30, width=30)


    def clica(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.youtube.com/user/advance2')

    def fechar(self):
        self.root.destroy()

# Progama Principal
root = Tk()
Tela()
