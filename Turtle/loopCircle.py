import turtle as t

t.hideturtle()
t.speed(1000)
t.pensize(1)

y=1
for i in range(100) :
    t.circle(i+i)
    t.penup()
    t.goto(0,y)
    t.pendown()
    y=y-2
t.mainloop()
