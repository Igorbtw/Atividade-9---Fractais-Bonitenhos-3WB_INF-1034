from turtle import *
from time import sleep
from random import randint
import tkinter as tk

t = Turtle()
t.speed(0)

def randomColor():
  return (randint(0, 255), randint(0, 255), randint(0, 255))

#funcao abaixo:
#ola tudo bem
#ola tudo be
#ola tudo b ...
def mostra_palavra_for(palavra):
    for i in range(len(palavra)):
        print(palavra[:len(palavra) - i])

mostra_palavra_for("ola, tudo bem?")


xgui = 0
def mostra_palavra_recursivo_gui(palavra):
    global xgui
    while xgui<len(palavra):
        print(palavra[:len(palavra) - xgui])
        xgui+=1
        mostra_palavra_recursivo_gui(palavra)

mostra_palavra_recursivo_gui("aiiii caralho")

def mostra_palavra_recursivo(palavra):
    if palavra == "":
        return
    print("antes da chamada recursiva:", palavra)
    mostra_palavra_recursivo(palavra[:-1])
    print("depois da chamada recursiva:", palavra)
    return

mostra_palavra_recursivo("bicalho-o-o-o-o-o-o-o-o-o")

#def fibonacci(n):
#    if n == 0 or n == 1:
#        return
#    return fibonacci(n-1) + fibonacci(n-2)

#fibonacci(10)


colormode(255)


def drawsquare(t, size):
    t.pd()
    t.begin_fill()
    t.fillcolor(randomColor())
    for i in range(4):
        t.fd(size)
        t.rt(90)
    t.end_fill()
    t.pu()

t.pu()
t.goto(-50,-50)
t.pd()

def drawsquarefractal(t,size,step = 50):
    if size == 0:
        return
    t.fd(size / 1.5)
    t.lt(10)
    drawsquare(t, size) 
    t.lt(120)
    drawsquarefractal(t,size-1,step-1)


drawsquarefractal(t,200,100)
tracer(0)

def redesenhar_forma(valor_do_slider):
    
    size = int(valor_do_slider)

    t.clear()

    t.pu()
    t.goto(0, -50)
    t.setheading(90)
    t.pd()
    
    drawsquarefractal(t,size,100)
    
    update()

tela_principal = getcanvas().winfo_toplevel()

meu_slider = tk.Scale(
    tela_principal, 
    from_=0,
    to=360,
    orient="horizontal", 
    label="Mude o tamanho aqui", 
    command=redesenhar_forma, 
    length=300
)

meu_slider.pack(side="bottom")
meu_slider.set(200)

mainloop()