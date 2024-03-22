import turtle as t

t.shape("turtle")
t.pensize(5)
t.color("green")
t.speed(10)

#사각형
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

#위치 이동
t.goto(0,100)

#삼각형
t.color("orange")
t.begin_fill()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.end_fill()

#객체 추가
t1 = t.Turtle()

t1.penup()
t1.goto(200, 0)
t1.pendown()

t1.shape("turtle")
t1.pensize(5)
t1.speed(10)
t1.color("blue")

t1.begin_fill()
t1.forward(100)
t1.left(90)
t1.forward(100)
t1.left(90)
t1.forward(100)
t1.left(90)
t1.forward(100)
t1.left(90)
t1.end_fill()

t1.goto(200,100)

t1.color("red")
t1.begin_fill()
t1.forward(100)
t1.left(120)
t1.forward(100)
t1.left(120)
t1.forward(100)
t1.left(120)
t1.end_fill()

#글씨 쓰기

t2 = t.Turtle()
t2.speed(10)
t2.penup()
t2.goto(-200, 0)
t2.pendown()
t2.shape("turtle")
t2.color("black")
t2.write("파이썬 시작! 터틀 참 쉽죠?", font=('Arial', 10, 'normal'))
