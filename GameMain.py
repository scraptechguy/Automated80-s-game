import turtle

# defining screen looks
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=1280, height=720)
wn.tracer(0)


# On screen objects

# The square
loc = turtle.Turtle()
loc.speed(0)
loc.shape("square")
loc.color("white")
loc.penup()
loc.goto(0, 0)


# Text-writing pen
txt = turtle.Turtle()
txt.speed(0)
txt.color("white")
txt.penup()
txt.hideturtle()
txt.goto(-600, 300)
txt.write(
    "Welcome! You've just woken up. Confused, lying the middle of a huge forest.",
    font=("Courier", 20, "normal"), 
)


# Coordinates (left down corner of the screen)
cor = turtle.Turtle()
cor.speed(0)
cor.color("white")
cor.penup()
cor.hideturtle()


# Number of coins (left corner of the screen)
cn = turtle.Turtle()
cn.speed(0)
cn.color("white")
cn.penup()
cn.hideturtle()


# Filling pen (fil position you've been to)
fill = turtle.Turtle()
fill.speed(0)
fill.color("white")
fill.hideturtle()


# Grid-writing pen
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

for i in range(12):
    pen.right(90)
    pen.forward(550)
    pen.right(180)
    pen.forward(550)
    pen.right(90)
    pen.forward(50)

pen.right(90)
pen.forward(550)

pen.penup()
pen.goto(-625, 275)
pen.pendown()

pen.right(90)

for i in range(11):
   pen.forward(1250)
   pen.right(180)
   pen.forward(1250)
   pen.left(90)
   pen.forward(50)
   pen.left(90)


# Defining coordinates and setting it's value to zero  
y_axis = 0
x_axis = 0

# Defining movement
def go_north():
    y = loc.ycor()
    y += 50             # Jumping by 50 pixels per click
    loc.sety(y)

def go_south():
    y = loc.ycor()
    y -= 50
    loc.sety(y)

def go_east():
    x = loc.xcor()
    x += 50
    loc.setx(x)

def go_west():
    x = loc.xcor()
    x -= 50
    loc.setx(x)


# Keyboard binding with movement functions
wn.listen()
wn.onkeypress(go_north, "w")
wn.onkeypress(go_south, "s")
wn.onkeypress(go_east, "d")
wn.onkeypress(go_west, "a")



# Square filling function (Yes, that's why all the squares are purple )
def draw():
    # Drawing a square that will be filled (The square is the same size as one grid square)
    def square():
        fill.goto(loc.xcor(), loc.ycor())       # Fill pen will follow loc object
        fill.penup()
        fill.forward(25)
        fill.right(90)
        fill.pendown()
        fill.forward(25)
        fill.right(90)
        fill.forward(50)
        fill.right(90)
        fill.forward(50)
        fill.right(90)
        fill.forward(50)
        fill.right(90)
        fill.forward(25)
        fill.penup()
        fill.right(90)
        fill.forward(25)
        fill.right(180)
        fill.penup()

    # Fill color + actual filling of the square  
    fill.fillcolor("purple")
    fill.begin_fill()
    square()
    fill.end_fill()


# Defining coin concerning variables and setting all of them equal to zero
coins = 0
# c1, c2, and c3 are places with coins. When the place is found by player for the first time, value increases by 1 ->
# -> program will be able to tell, whether you have already received a coin for that certain place  
c1 = 0
c2 = 0      # Coin collecting mechanism to avoid mistakes in number of coins
c3 = 0

# Game loop
while True:
    wn.update()
    draw()

    # Displaying coordinates info (left down corner of the screen)
    cor.clear()
    cor.goto(-600, -300)
    cor.write("X: {}       Y: {}".format(loc.xcor(), loc.ycor()))

    # Displaying coins info (left down corner of the screen)
    cn.clear()
    cn.goto(-600, -320)
    cn.write("Coins: {}   ".format(coins))

    # Boarders (As soon as boarder is hit, loc is moved back by one jump, 50 pixels.)
    
    # Left side
    if loc.xcor() < -625:
        loc.setx(-600)

    # Right side
    elif loc.xcor() > 625:
        loc.setx(600)
    
    # Bottom side 
    elif loc.ycor() < -275:
        loc.sety(-250)
    
    # Top side
    elif loc.ycor() > 275:
        loc.sety(250)

    # Places with actions (If you step on certain location, something will happen.)
    if loc.xcor() == 50 and loc.ycor() == 0:
        txt.clear()
        txt.goto(-600, 300)
        txt.write( 
            "Wow that was fast, you found something. Good for you!",
            font=("Courier", 24, "normal"),
        )

    elif loc.xcor() == 100 and loc.ycor() == -100:
        txt.clear()
        txt.write(
            "Heyy",
            font=("Courier", 24, "normal")
        )


    # Places with coins 

    # c1
    elif loc.xcor() == 50 and loc.ycor() == -50:

        # Coin collecting mechanism
        if coins == 0:
            txt.clear()
            txt.write(
            "Hm, something shiny's lying on the ground. Yes! It's a coin. ",
            font=("Courier", 24, "normal")
            )

            coins = 1

        elif coins == 1 and c2 == 1:
            txt.clear()
            txt.write(
            "Next one! Great.",
            font=("Courier", 24, "normal")
            )

            coins = 2

        elif coins == 1 and c3 == 1:
            txt.clear()
            txt.write(
            "Another one! Good for you.",
            font=("Courier", 24, "normal")
            )

            coins = 2

        elif coins == 2 and c2 == 1 and c3 == 1:
            coins = 3

        c1 = 1

    # c2
    elif loc.xcor() == -50 and loc.ycor() == -50:

        # Coin collecting mechanism
        if coins == 0:
            txt.clear()
            txt.write(
            "Hm, something shiny's lying on the ground. Yes! It's a coin. ",
            font=("Courier", 24, "normal")
            )

            coins = 1

        elif coins == 1 and c1 == 1:
            txt.clear()
            txt.write(
            "Another one! Good for you.",
            font=("Courier", 24, "normal")
            )
            coins = 2

        elif coins == 1 and c3 == 1:
            txt.clear()
            txt.write(
            "Next one! Great.",
            font=("Courier", 24, "normal")
            )

            coins = 2

        elif coins == 2 and c1 == 1 and c3 == 1:
            coins = 3

        c2 = 1

    # c3
    elif loc.xcor() == -100 and loc.ycor() == -50:

        # Coin collecting mechanism
        if coins == 0:
            txt.clear()
            txt.write(
            "Hm, something shiny's lying on the ground. Yes! It's a coin. ",
            font=("Courier", 24, "normal")
            )

            coins = 1

        elif coins == 1 and c1 == 1:
            txt.clear()
            txt.write(
            "Next one! Great.",
            font=("Courier", 24, "normal")
            )

            coins = 2

        elif coins == 1 and c2 == 1:
            txt.clear()
            txt.write(
            "Another one! Yaaay.",
            font=("Courier", 24, "normal")
            )

            coins = 2

        elif coins == 2 and c1 == 1 and c2 == 1:
            coins = 3

        c3 = 1

    elif coins == 3:
        break

txt.clear()
pen.clear()
cor.clear()
cn.clear()
fill.clear()
loc.hideturtle()

txt.goto(-70, 0)
txt._tracer(1)
txt.write(
    "You win!",
    font=("Courier", 24, "normal")
    )

blueRocket2 = turtle.Turtle()
blueRocket2.hideturtle()
blueRocket2.penup()
blueRocket2.color("blue")
blueRocket2.shape("square")
blueRocket2.shapesize(0.5, 0.5)
blueRocket2.goto(-400, -50)

blueRocket3 = turtle.Turtle()
blueRocket3.hideturtle()
blueRocket3.penup()
blueRocket3.color("blue")
blueRocket3.shape("square")
blueRocket3.shapesize(0.5, 0.5)
blueRocket3.goto(-400, -50)

blueRocket4 = turtle.Turtle()
blueRocket4.hideturtle()
blueRocket4.penup()
blueRocket4.color("blue")
blueRocket4.shape("square")
blueRocket4.shapesize(0.5, 0.5)
blueRocket4.goto(-400, -50)

blueRocket5 = turtle.Turtle()
blueRocket5.hideturtle()
blueRocket5.penup()
blueRocket5.color("blue")
blueRocket5.shape("square")
blueRocket5.shapesize(0.5, 0.5)
blueRocket5.goto(-400, -50)

blueRocket6 = turtle.Turtle()
blueRocket6.hideturtle()
blueRocket6.penup()
blueRocket6.color("blue")
blueRocket6.shape("square")
blueRocket6.shapesize(0.5, 0.5)
blueRocket6.goto(-400, -50)

blueRocket7 = turtle.Turtle()
blueRocket7.hideturtle()
blueRocket7.penup()
blueRocket7.color("blue")
blueRocket7.shape("square")
blueRocket7.shapesize(0.5, 0.5)
blueRocket7.goto(-400, -50)

blueRocket = turtle.Turtle()
blueRocket.hideturtle()
blueRocket.color("gray")
blueRocket.shape("square")
blueRocket.shapesize(0.3, 1.5)

while True:
    wn.update()

    blueRocket2.goto(-400, -50)
    blueRocket3.goto(-400, -50)
    blueRocket4.goto(-400, -50)
    blueRocket5.goto(-400, -50)
    blueRocket6.goto(-400, -50)
    blueRocket7.goto(-400, -50)

    blueRocket.penup()
    blueRocket.goto(-400, -450)
    blueRocket.showturtle()
    blueRocket.left(90)
    blueRocket.forward(400)
    blueRocket.hideturtle()

    blueRocket2.showturtle()
    blueRocket3.showturtle()
    blueRocket4.showturtle()
    blueRocket5.showturtle()
    blueRocket6.showturtle()
    blueRocket7.showturtle()


    for i in range(30):
        by2 = blueRocket2.ycor()
        by2 += 2
        blueRocket2.sety(by2)

        bx2 = blueRocket2.xcor()
        bx2 += 4
        blueRocket2.setx(bx2)


        by3 = blueRocket3.ycor()
        by3 += 2
        blueRocket3.sety(by3)

        bx3 = blueRocket3.xcor()
        bx3 -= 4
        blueRocket3.setx(bx3)


        by4 = blueRocket4.ycor()
        by4 += 2
        blueRocket4.sety(by4)

        bx4 = blueRocket4.xcor()
        bx4 += 3
        blueRocket4.setx(bx4)


        by5 = blueRocket5.ycor()
        by5 += 2
        blueRocket5.sety(by5)

        bx5 = blueRocket5.xcor()
        bx5 -= 4
        blueRocket5.setx(bx5)


        by6 = blueRocket6.ycor()
        by6 -= 2
        blueRocket6.sety(by6)

        bx6 = blueRocket6.xcor()
        bx6 -= 3
        blueRocket6.setx(bx6)


        by7 = blueRocket7.ycor()
        by7 -= 1
        blueRocket7.sety(by7)

        bx7 = blueRocket7.xcor()
        bx7 += 2
        blueRocket7.setx(bx7)



    blueRocket.hideturtle()
    blueRocket2.hideturtle()
    blueRocket3.hideturtle()
    blueRocket4.hideturtle()
    blueRocket5.hideturtle()
    blueRocket6.hideturtle()
    blueRocket7.hideturtle()
