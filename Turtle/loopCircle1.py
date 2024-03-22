import random
import turtle as t

t.speed(1000)
t.pensize(1)
t.colormode(255)

def random_color() :
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    random_color = (r, g, b)
    return random_color

y=1
for i in range(100) :
    t.color(random_color())
    t.begin_fill()
    t.circle(i+i)
    t.end_fill()
    t.penup()
    t.goto(0,y)
    t.pendown()
    y=y-2
t.mainloop()
