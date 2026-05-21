from turtle import *
import tkinter as tk
from time import sleep
from random import randint


t = Turtle()
t.speed(0)
screen = Screen()

def randomColor():
  return (randint(0, 255), randint(0, 255), randint(0, 255))

colormode(255)
t.pu()
t.goto(0,-50)
t.pd()



def formadificil(t,size,angle,nivel):
    if size < 20 or nivel<1:
        return
    t.pd()
    t.fd(size)

    #down
    t.rt(120)
    t.fd(size)
    formadificil(t, size * 0.8, angle, nivel - 1)
    t.back(size)

    t.lt(120)

    t.lt(90)
    t.fd(size)
    formadificil(t, size * 0.8, angle, nivel - 1)
    t.back(size)

    t.rt(90)
    
    # right tree
    t.rt(angle)
    t.fd(size)
    formadificil(t, size * 0.8, angle, nivel - 1)
    t.back(size)

    t.pencolor(0, 255 // nivel, 0)

    # left tree
    t.lt(2 * angle)
    t.fd(size)
    formadificil(t, size * 0.8, angle, nivel - 1)
    t.back(size)

    t.pencolor(randomColor())
    t.lt(-angle)
    t.back(size)

#t.goto(0, -200)
t.lt(90)
formadificil(t, 60, 40, 5)
tracer(0)


def redesenhar_arvore(valor_do_slider):
    
    angulo = int(valor_do_slider)

    t.clear()

    t.pu()
    t.goto(0, -50)
    t.setheading(90)
    t.pd()
    
    formadificil(t, 60, angulo, 5)
    
    update()

tela_principal = getcanvas().winfo_toplevel()

meu_slider = tk.Scale(
    tela_principal, 
    from_=0,
    to=360,
    orient="horizontal", 
    label="Mude a abertura da árvore aqui", 
    command=redesenhar_arvore, 
    length=300
)

meu_slider.pack(side="bottom")
meu_slider.set(40)

mainloop()