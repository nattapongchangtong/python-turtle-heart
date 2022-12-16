import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('white')
t.hideturtle()
t.goto(0,-10)

t.pensize(3)
t.color('red')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()

t.penup()
t.goto(-150,130)
t.pendown()
t.color('white')


t.penup()
t.goto(-240,-100)
t.pendown()
t.color('black')
t.write("Nattapong Chnagtong",font=("Verdana",30,"bold"))

turtle.done()
