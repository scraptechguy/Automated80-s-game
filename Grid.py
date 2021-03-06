import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=1280, height=720)
wn.tracer(0)

pen = turtle.Turtle()
pen.color("white")
pen.hideturtle()

pen.penup()
pen.goto(0, -275)
pen.pendown()
pen.forward(25)

for i in range(12):
    pen.left(90)
    pen.forward(550)
    pen.left(180)
    pen.forward(550)
    pen.left(90)
    pen.forward(50)

pen.left(90)
pen.forward(550)
    

pen.penup()
pen.goto(0, -275)
pen.pendown()

pen.left(90)
pen.forward(25)
