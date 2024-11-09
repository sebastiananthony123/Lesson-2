from turtle import *

bgcolor("#305c5a")
pencolor("#1f46c4")
pensize(6)
fillcolor("red")

begin_fill()
for i in range(5):
    forward(100)
    right(360/5)
end_fill()

penup()
goto(-100,-100)
pendown()

pencolor("green")
fillcolor("black")
pensize(7)
begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill

penup()
goto(200,100)
pendown()

pencolor("black")
fillcolor("yellow")
pensize(3)
begin_fill()
for i in range(4):
    forward(100)
    left(120)
end_fill()

mainloop()
