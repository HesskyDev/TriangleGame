import os, turtle, time
en = turtle.Screen()
en.title("TriangleGame")
en.bgcolor("#405012")

def lost_game():
    en.clearscreen()
    turtle.color("#992020")
    turtle.write("--You Lost--", font=("Verdana", 20, "bold"), align="center")
    turtle.hideturtle()
    
#Micanje
def move_right():
    igrac.rt(90)
def move_left():
    igrac.lt(90)
def boja():
    igrac.color("lightblue")
turtle.listen()
turtle.onkey(move_right, "d")
turtle.onkey(boja, "Return")
turtle.onkey(move_left, "a")
#-----------------


#Border
ravno = 500
ta = turtle.Turtle()
ta.penup()
ta.color("black")
ta.speed(0)
ta.pensize(10)
ta.hideturtle()
ta.setposition(-250, -250)
ta.pendown()
for i in range(4):
    ta.fd(ravno)
    ta.lt(90)
ta.penup()
#-----------------
#Igrac
igrac = turtle.Turtle()
igrac.shape("triangle")
igrac.shapesize(2)
igrac.penup()
igrac.speed(0)
igrac.lt(90)
igrac.color("yellowgreen")
wrong = 170
#-----------------
#Glavna masina
live = True
while (live):

    tax = ta.xcor()
    tay = ta.ycor()
    x = igrac.xcor()
    y = igrac.ycor()
    igrac.fd(2.5)
    if x >= wrong:
        live = False
        igrac.setposition(0, 0)
        ta.penup()
        wrong + 75
        ta.setposition(tax + 25, tay + 25)
        ta.pendown()
        for i in range(4):
            ta.fd(ravno - 50)
            ta.lt(90)
        ravno = ravno - 50
        if ravno <= 350:
            lost_game()
            time.sleep(7)
            turtle.bye()
        time.sleep(1)
        live = True
    if x <= -wrong:
        live = False
        igrac.setposition(0, 0)
        ta.penup()
        ta.setposition(tax + 25, tay + 25)
        ta.pendown()
        for i in range(4):
            ta.fd(ravno - 50)
            ta.lt(90)
        ravno = ravno - 50
        wrong + 75
        if ravno <= 350:
            lost_game()
            time.sleep(7)
            turtle.bye()
        time.sleep(1)
        live = True
#----------
    if y >= wrong:
        live = False
        igrac.setposition(0, 0)
        ta.penup()
        ta.setposition(tax + 25, tay + 25)
        ta.pendown()
        for i in range(4):
            ta.fd(ravno - 50)
            ta.lt(90)
        ravno = ravno - 50
        wrong + 75
        if ravno <= 350:
            lost_game()
            time.sleep(7)
            turtle.bye()
        time.sleep(1)
        live = True
#-----------
    if y <= -wrong:
        live = False
        igrac.setposition(0, 0)
        ta.penup()
        ta.setposition(tax + 25, tay + 25)
        ta.pendown()
        for i in range(4):
            ta.fd(ravno - 50)
            ta.lt(90)
        ravno = ravno - 50
        wrong + 75
        if ravno <= 350:
            lost_game()
            time.sleep(7)
            turtle.bye()
        time.sleep(1)
        live = True
#-----------------d
