from turtle import *
from time import sleep
from random import randint
import tkinter as tk


t = Turtle()
t.speed(0)

def randomColor():
  return (randint(0, 255), randint(0, 255), randint(0, 255))

colormode(255)

def forma_facil(t,size,step):
    if size == 0 or step == 0:
       return
    t.begin_fill()
    t.color(randomColor())
    for i in range(6):
        t.fd(size)
        t.lt(60)
    t.end_fill()
    forma_facil(t,size-5,step)

forma_facil(t,100,50)
tracer(0)

def redesenhar_forma(valor_do_slider):
    
    size = int(valor_do_slider)

    t.clear()


    t.goto(-200,-200)
    forma_facil(t,size,50)
    
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
meu_slider.set(100)

mainloop()