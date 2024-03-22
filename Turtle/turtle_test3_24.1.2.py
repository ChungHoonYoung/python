'''
#방법1
import turtle as t
my_t = t.Turtle()


#방법2 't.'안붙이고 함수들을 쓸 수 있음
from turtle import *
my_t2 = Turtle()
'''

#이벤트 처리

from turtle import *

screen = Screen()
t = Turtle()

size = 1

def myGo():
    t.forward(10)

def myBack():
    t.backward(10)

def myTurnRight():
    t.right(10)

def myTurnLeft():
    t.left(10)

def myPenUp():
    t.penup()

def myPenDown():
    t.pendown()

def myClearHome():
    t.home()
    t.clear()

def mySizeUp():
    global size
    size+=1
    t.pensize(size)

def mySizeDown():
    global size
    if size > 1 :
        size-=1
        t.pensize(size)


screen.title("my screen")
screen.listen()
screen.onkeypress(myGo, 'Up')
screen.onkeypress(myBack, 'Down')
screen.onkeypress(myTurnRight, 'Right')
screen.onkeypress(myTurnLeft, 'Left')
screen.onkeypress(myPenUp, 'q')
screen.onkeypress(myPenDown, 'w')
screen.onkeypress(myClearHome, 'c')
screen.onkeypress(t.undo, 'u')

screen.onkeypress(mySizeUp, '+')
screen.onkeypress(mySizeDown, '-')


















