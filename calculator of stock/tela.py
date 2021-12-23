from tkinter import *
import numpy as np
import rentabilidade
import matplotlib.pyplot as plt
import os
c = ["#3B2E8C", "#5D4AD9","#222340", " #151626", "#F2F2F2"]
app = Tk()
app.title("calculadora")
app.geometry("1200x680")
app.configure(background= c[0])


def aplicar():
    v_i = float(vi.get())
    tmp = int(te.get())
    v_m = float(vm.get())
    tx = float(ta.get())/100
    a,b,c = rentabilidade.graf(v_i,tx,tmp,v_m)
    rentabilidade.plot(b,a,c)
    imgLogo.config(file = pastaApp+"\\grafico.png")


pastaApp = os.path.dirname(__file__)
imgLogo = PhotoImage("")
l_logo = Label(app, image = imgLogo)
l_logo.place(x = 310, y= 10)



Label(app, text ="valor inicial", background =c[4], foreground = c[1], anchor = W).place(x =10, y =10, width = 100, height = 20)
vi = Entry(app)
vi.place(x=111, y = 10, width = 200, height =20)

Label(app, text ="tempo(meses)", background =c[4], foreground = c[1], anchor = W).place(x =10, y =31, width = 100, height = 20)
te = Entry(app)
te.place(x=111, y = 31, width = 200, height =20)

Label(app, text ="taxa %", background =c[4], foreground = c[1], anchor = W).place(x =10, y =52, width = 100, height = 20)
ta = Entry(app)
ta.place(x=111, y = 52, width = 200, height =20)

Label(app, text ="aporte mensal", background =c[4], foreground = c[1], anchor = W).place(x =10, y =73, width = 100, height = 20)
vm = Entry(app)
vm.place(x=111, y = 73, width = 200, height =20)

botao = Button(app,height = 20, width = 20, text = "aplicar", command = aplicar, foreground = c[4], background =c[1])
botao.place(x = 10, y=94, width = 301, height = 20)


app.wm_iconbitmap('Python.ico')
app.mainloop()

