from turtle import *

t = Turtle()


#começo do plano cartesiano



t.color("blue")
t.pu()
t.goto(0, 0)
t.pd()


t.fd(300)
t.stamp()
t.goto(0, 0)
t.pd()
t.lt(90)
t.fd(300)
t.goto(0, 0)
t.pd()
t.lt(90)
t.fd(300)
t.goto(0, 0)
t.pd()
t.lt(90)
t.fd(300)

#figura geometrica 1

color = textinput("Obter cor","Digite a cor desejada:")

t.pu()
t.goto(150,150)
t.pd()
t.color("blue")
t.begin_fill()
t.fillcolor(color)
for _ in range(3):
      t.fd(100)
      t.lt(120)    
t.end_fill()

#figura geometrica 2

color = textinput("Obter cor","Digite a cor desejada:")

t.pu()
t.goto(-150,150)
t.pd()
t.stamp()
t.color("red")
t.begin_fill()
t.fillcolor(color)
for _ in range(6):
      t.right(60)
      t.fd(90)
t.end_fill()


#figura geometrica 3

color = textinput("Obter cor","Digite a cor desejada:")

t.pu()
t.goto(-150,-150)
t.pd()
t.stamp()
t.color("yellow")
t.begin_fill()
t.fillcolor(color)
for _ in range(5):
       t.fd(108)
       t.right(72)
t.end_fill()

#figura geometrica 4

color = textinput("Obter cor","Digite a cor desejada:")

t.pu()
t.goto(375,-150)
t.pd()
t.stamp()
t.color("green")
t.begin_fill()
t.fillcolor(color)
for _ in range(8):
       t.fd(135)
       t.right(45)
t.end_fill()


#espiral

# 1. MOVER PARA O NOVO LUGAR
t.penup()
t.goto(250, 250) 
t.pendown()

# 2. DESENHAR A ESPIRAL
for i in range(100):
    t.forward(i)
    t.right(45)

mainloop()