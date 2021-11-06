from tkinter import *
from math import *
import sys
from errop import Erro

class Calculadora:
    def __init__(self, toplevel):

        # Janela
        toplevel.title('Calculadora')
        toplevel.geometry("300x350")

        # Espaçamento
        self.frame1 = Frame(toplevel)
        self.frame1.pack()
    
        # Box 1
        self.frame2 = Frame(toplevel)
        self.frame2.pack()

        # Box 2
        self.frame3 = Frame(toplevel)
        self.frame3.pack()

        # Operações
        self.frame4 = Frame(toplevel, pady=20)
        self.frame4.pack()

        # Resultado
        self.frame5 = Frame(toplevel)
        self.frame5.pack()

        # Botões
        self.frame6 = Frame(toplevel, pady=20)
        self.frame6.pack()
        
        # Cor e tamanho das letras 
        Label(self.frame1,text='', fg='black',
        font=('Verdana','10'), height=5).pack()
        fonte1=('Verdana','15')

        # Botão somar
        somar=Button(self.frame4,font=fonte1, text='+',command=self.somar)
        somar.pack(side=LEFT)

        # Botão subtrair
        subtrair=Button(self.frame4,font=fonte1, text='-',command=self.subtrair)
        subtrair.pack(side=LEFT)
        
        # Botão multiplicar
        multiplicar=Button(self.frame4,font=fonte1, text='*',command=self.multiplicar)
        multiplicar.pack(side=LEFT)

        # Botão dividir
        dividir=Button(self.frame4,font=fonte1, text='/',command=self.dividir)
        dividir.pack(side=LEFT)

        # Botão raiz
        raiz=Button(self.frame4,font=fonte1, text='Sqrt',command=self.sqrt)
        raiz.pack(side=LEFT)

        # Botão Limpar
        limpar=Button(self.frame6, font=fonte1, text= 'Limpar', command=self.limpar)
        limpar.pack(side=LEFT)

        # Botão Sair
        sair=Button(self.frame6, font=fonte1, text= 'Sair', command=self.sair)
        sair.pack(side=LEFT)
        
        # Box 1 para entrada de número
        Label(self.frame2,text='Valor1 :', font=fonte1,width=8).pack(side=LEFT)
        self.valor1=Entry(self.frame2,width=10,font=fonte1)
        self.valor1.focus_force()
        self.valor1.pack(side=LEFT)

        # Box 2 para entrada de número
        Label(self.frame3,text='Valor2 :',font=fonte1,width=8).pack(side=LEFT)
        self.valor2=Entry(self.frame3,width=10,font=fonte1)
        self.valor2.pack(side=LEFT)

        # Resultado
        Label(self.frame5,text=' = ',font=fonte1,width=8).pack(side=LEFT)
        self.msg=Label(self.frame5,width=20,font=fonte1)
        self.msg.pack(side=LEFT)

    def somar(self):
        try:
            valor1 = self.valor1.get()
            valor2 = self.valor2.get()
            valor1 = float(valor1)
            valor2 = float(valor2)
            c = valor1 + valor2
            c = float(c)
            self.msg['text']= '%f' %(c)
        except:
           self.msg['text']= 'Digite dados válidos!!'
             


    def subtrair(self):
        try:
            valor1 = self.valor1.get()
            valor2 = self.valor2.get()
            valor1 = float(valor1)
            valor2 = float(valor2)
            c = valor1 - valor2
            c = float(c)
            self.msg['text']= '%f' %(c)
        except: 
            self.msg['text']= 'Digite dados válidos!!'
            
    
    def multiplicar(self):
        try:
            valor1 = self.valor1.get()
            valor2 = self.valor2.get()
            valor1 = float(valor1)
            valor2 = float(valor2)
            c = valor1 * valor2
            c = float(c)
            self.msg['text']= '%f' %(c)
        except:
            self.msg['text']= 'Digite dados válidos!!'
    def dividir(self):
        
        try:
            valor1 = self.valor1.get()
            valor2 = self.valor2.get()
            valor1 = float(valor1)
            valor2 = float(valor2)
            c = valor1 / valor2
            c = float(c)
            self.msg['text']= '%f' %(c)
        except:
            self.msg['text']= 'Digite dados válidos!!'
    def sqrt(self):
        try:
            valor1 = self.valor1.get()
            valor1 = float(valor1)
            c = sqrt(valor1)
            c = float(c)
            self.msg['text']= '%f' %(c)
        except:
            self.msg['text']= 'Digite dados válidos!!'
   
    def limpar(self):
        pass
    
    def sair(self):
        app.destroy()
        
app=Tk()
Calculadora(app)
app.mainloop()