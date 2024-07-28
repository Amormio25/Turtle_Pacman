import turtle as trtl
import random as rand


#       to-do: add more green circles, add more red circles and one more red circle with chance of big boost, more speed boosts, set time higher
#   screen setup
wn = trtl.Screen()
wn.setup(500,500)
wn.tracer = True

#   timer setup
font_setup = ("Comic Sans MS", 20, "normal")                                                                                                                                                                                                                                                                          
timer = 60                                                                                                                                                                                                                                                                         
counter_interval = 1000   #1000 represents 1 second                                                                                                                                                                                                                                                                         
timer_up = False                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                            
counter = trtl.Turtle()   
counter.hideturtle()                                                                                                                                                                                                                                                                       
counter.color("black")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
counter.speed(20)

#   user turtle
turtle = trtl.Turtle("turtle")
turtle.color("darkgreen")
turtle.penup()
turtle.setpos(0,0)
turtle_speed = 0
turtle.speed(1.3)

#   score_writer
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.pu()
score_writer.color("black")
score_writer.goto(-60,0)

#   circles

#   r = red
r1 = trtl.Turtle("circle")
r1.shapesize(0.5)
r1.color("red")
r1.penup()
r1.setpos(rand.randint(-230,230), rand.randint(-230,230))

r2 = trtl.Turtle("circle")
r2.shapesize(0.5)
r2.color("red")
r2.penup()
r2.setpos(rand.randint(-230,230), rand.randint(-230,230))

r3 = trtl.Turtle("circle")
r3.shapesize(0.5)
r3.color("red")
r3.penup()
r3.setpos(rand.randint(-230,230), rand.randint(-230,230))

r4 = trtl.Turtle("circle")
r4.shapesize(0.5)
r4.color("red")
r4.penup()
r4.setpos(rand.randint(-230,230), rand.randint(-230,230))

r5 = trtl.Turtle("circle")
r5.shapesize(0.5)
r5.color("red")
r5.penup()
r5.setpos(rand.randint(-230,230), rand.randint(-230,230))

r6 = trtl.Turtle("circle")
r6.shapesize(0.5)
r6.color("red")
r6.penup()
r6.setpos(rand.randint(-230,230), rand.randint(-230,230))

r7 = trtl.Turtle("circle")
r7.shapesize(0.5)
r7.color("red")
r7.penup()
r7.setpos(rand.randint(-230,230), rand.randint(-230,230))

r8 = trtl.Turtle("circle")
r8.shapesize(0.5)
r8.color("red")
r8.penup()
r8.setpos(rand.randint(-230,230), rand.randint(-230,230))

r9 = trtl.Turtle("circle")
r9.shapesize(0.5)
r9.color("red")
r9.penup()
r9.setpos(rand.randint(-230,230), rand.randint(-230,230))

r10 = trtl.Turtle("circle")
r10.shapesize(0.5)
r10.color("red")
r10.penup()
r10.setpos(rand.randint(-230,230), rand.randint(-230,230))

#   g = green
g1 = trtl.Turtle("circle")
g1.shapesize(0.5)
g1.color("green")
g1.penup()
g1.setpos(rand.randint(-230,230), rand.randint(-230,230))

g2 = trtl.Turtle("circle")
g2.shapesize(0.5)
g2.color("green")
g2.penup()
g2.setpos(rand.randint(-230,230), rand.randint(-230,230))

g3 = trtl.Turtle("circle")
g3.shapesize(0.5)
g3.color("green")
g3.penup()
g3.setpos(rand.randint(-230,230), rand.randint(-230,230))

g4 = trtl.Turtle("circle")
g4.shapesize(0.5)
g4.color("green")
g4.penup()
g4.setpos(rand.randint(-230,230), rand.randint(-230,230))

g5 = trtl.Turtle("circle")
g5.shapesize(0.5)
g5.color("green")
g5.penup()
g5.setpos(rand.randint(-230,230), rand.randint(-230,230))

g6 = trtl.Turtle("circle")
g6.shapesize(0.5)
g6.color("green")
g6.penup()
g6.setpos(rand.randint(-230,230), rand.randint(-230,230))

g7 = trtl.Turtle("circle")
g7.shapesize(0.5)
g7.color("green")
g7.penup()
g7.setpos(rand.randint(-230,230), rand.randint(-230,230))

g8 = trtl.Turtle("circle")
g8.shapesize(0.5)
g8.color("green")
g8.penup()
g8.setpos(rand.randint(-230,230), rand.randint(-230,230))

g9 = trtl.Turtle("circle")
g9.shapesize(0.5)
g9.color("green")
g9.penup()
g9.setpos(rand.randint(-230,230), rand.randint(-230,230))

g10 = trtl.Turtle("circle")
g10.shapesize(0.5)
g10.color("green")
g10.penup()
g10.setpos(rand.randint(-230,230), rand.randint(-230,230))

g11 = trtl.Turtle("circle")
g11.shapesize(0.5)
g11.color("green")
g11.penup()
g11.setpos(rand.randint(-230,230), rand.randint(-230,230))

g12 = trtl.Turtle("circle")
g12.shapesize(0.5)
g12.color("green")
g12.penup()
g12.setpos(rand.randint(-230,230), rand.randint(-230,230))

g13 = trtl.Turtle("circle")
g13.shapesize(0.5)
g13.color("green")
g13.penup()
g13.setpos(rand.randint(-230,230), rand.randint(-230,230))

g14 = trtl.Turtle("circle")
g14.shapesize(0.5)
g14.color("green")
g14.penup()
g14.setpos(rand.randint(-230,230), rand.randint(-230,230))

g15 = trtl.Turtle("circle")
g15.shapesize(0.5)
g15.color("green")
g15.penup()
g15.setpos(rand.randint(-230,230), rand.randint(-230,230))

#   y = yellow
y1 = trtl.Turtle("circle")
y1.shapesize(0.5)
y1.color("yellow")
y1.penup()
y1.setpos(rand.randint(-230,230), rand.randint(-230,230))

y2 = trtl.Turtle("circle")
y2.shapesize(0.5)
y2.color("yellow")
y2.penup()
y2.setpos(rand.randint(-230,230), rand.randint(-230,230))

y3 = trtl.Turtle("circle")
y3.shapesize(0.5)
y3.color("yellow")
y3.penup()
y3.setpos(rand.randint(-230,230), rand.randint(-230,230))

y4 = trtl.Turtle("circle")
y4.shapesize(0.5)
y4.color("yellow")
y4.penup()
y4.setpos(rand.randint(-230,230), rand.randint(-230,230))

y5 = trtl.Turtle("circle")
y5.shapesize(0.5)
y5.color("yellow")
y5.penup()
y5.setpos(rand.randint(-230,230), rand.randint(-230,230))

y6 = trtl.Turtle("circle")
y6.shapesize(0.5)
y6.color("yellow")
y6.penup()
y6.setpos(rand.randint(-230,230), rand.randint(-230,230))

y7 = trtl.Turtle("circle")
y7.shapesize(0.5)
y7.color("yellow")
y7.penup()
y7.setpos(rand.randint(-230,230), rand.randint(-230,230))

y8 = trtl.Turtle("circle")
y8.shapesize(0.5)
y8.color("yellow")
y8.penup()
y8.setpos(rand.randint(-230,230), rand.randint(-230,230))

y9 = trtl.Turtle("circle")
y9.shapesize(0.5)
y9.color("yellow")
y9.penup()
y9.setpos(rand.randint(-230,230), rand.randint(-230,230))

y10 = trtl.Turtle("circle")
y10.shapesize(0.5)
y10.color("yellow")
y10.penup()
y10.setpos(rand.randint(-230,230), rand.randint(-230,230))

#   p = purple
p1 = trtl.Turtle("circle")
p1.shapesize(0.5)
p1.color("purple")
p1.penup()
p1.setpos(rand.randint(-230,230), rand.randint(-230,230))

p2 = trtl.Turtle("circle")
p2.shapesize(0.5)
p2.color("purple")
p2.penup()
p2.setpos(rand.randint(-230,230), rand.randint(-230,230))

p3 = trtl.Turtle("circle")
p3.shapesize(0.5)
p3.color("purple")
p3.penup()
p3.setpos(rand.randint(-230,230), rand.randint(-230,230))

p4 = trtl.Turtle("circle")
p4.shapesize(0.5)
p4.color("purple")
p4.penup()
p4.setpos(rand.randint(-230,230), rand.randint(-230,230))

p5 = trtl.Turtle("circle")
p5.shapesize(0.5)
p5.color("purple")
p5.penup()
p5.setpos(rand.randint(-230,230), rand.randint(-230,230))

p6 = trtl.Turtle("circle")
p6.shapesize(0.5)
p6.color("purple")
p6.penup()
p6.setpos(rand.randint(-230,230), rand.randint(-230,230))

p7 = trtl.Turtle("circle")
p7.shapesize(0.5)
p7.color("purple")
p7.penup()
p7.setpos(rand.randint(-230,230), rand.randint(-230,230))

p8 = trtl.Turtle("circle")
p8.shapesize(0.5)
p8.color("purple")
p8.penup()
p8.setpos(rand.randint(-230,230), rand.randint(-230,230))

p9 = trtl.Turtle("circle")
p9.shapesize(0.5)
p9.color("purple")
p9.penup()
p9.setpos(rand.randint(-230,230), rand.randint(-230,230))

p10 = trtl.Turtle("circle")
p10.shapesize(0.5)
p10.color("purple")
p10.penup()
p10.setpos(rand.randint(-230,230), rand.randint(-230,230))


#   functions
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    score_writer.write("Your Score " + str(turtle_size), font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)



def quitThis():
       wn.bye()

def collision(a, b):
        return abs(a.xcor() - b.xcor()) < 15 and abs(a.ycor() - b.ycor()) < 15
  
turtle_size = 1  
def red_circles():
    global turtle_size
    while collision(r1, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        r1.setpos(newx, newy)
        r1.showturtle()
        turtle_size = turtle_size + 0.25
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(r2, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        r2.setpos(newx, newy)
        r2.showturtle()
        turtle_size = turtle_size + 0.6
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(r3, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        r3.setpos(newx, newy)
        r3.showturtle()
        choice = rand.randint(1,4)
        if choice == 4:
            size = rand.randint(2,5)
        else:
            size = 0.1
        turtle_size = turtle_size + size
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(r4, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        r4.setpos(newx, newy)
        r4.showturtle()
        turtle_size = turtle_size + 0.2
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(r5, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        r5.setpos(newx, newy)
        r5.showturtle()
        turtle_size = turtle_size + 0.3
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size

    while collision(r6, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        r6.setpos(newx, newy)
        r6.showturtle()
        turtle_size = turtle_size + 0.25
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(r7, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        r7.setpos(newx, newy)
        r7.showturtle()
        turtle_size = turtle_size + 0.6
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(r8, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        r8.setpos(newx, newy)
        r8.showturtle()
        choice = rand.randint(1,4)
        if choice == 4:
            size = rand.randint(2,5)
        else:
            size = 0.1
        turtle_size = turtle_size + size
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(r9, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        r9.setpos(newx, newy)
        r9.showturtle()
        turtle_size = turtle_size + 0.2
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(r10, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        r10.setpos(newx, newy)
        r10.showturtle()
        turtle_size = turtle_size + 0.3
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size

def green_circles():
    global turtle_size
    while collision(g1, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        g1.setpos(newx, newy)
        g1.showturtle()
        if turtle_size - 0.5 != 0:
            turtle_size = turtle_size - 0.5
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(g2, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        g2.setpos(newx, newy)
        g2.showturtle()
        if turtle_size - 1 != 0:
            turtle_size = turtle_size - 1
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(g3, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        g3.setpos(newx, newy)
        g3.showturtle()
        if turtle_size - 0.4 != 0:
            turtle_size = turtle_size - 0.4
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(g4, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        g4.setpos(newx, newy)
        g4.showturtle()
        if turtle_size - 0.2 != 0:
            turtle_size = turtle_size - 0.2
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(g5, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        g5.setpos(newx, newy)
        g5.showturtle()  
        if turtle_size - 0.3 != 0:
            turtle_size = turtle_size - 0.3
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size

    while collision(g6, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        g6.setpos(newx, newy)
        g6.showturtle()
        if turtle_size - 0.5 != 0:
            turtle_size = turtle_size - 0.5
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(g7, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        g7.setpos(newx, newy)
        g7.showturtle()
        if turtle_size - 1 != 0:
            turtle_size = turtle_size - 1
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(g8, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        g8.setpos(newx, newy)
        g8.showturtle()
        if turtle_size - 0.4 != 0:
            turtle_size = turtle_size - 0.4
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(g9, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        g9.setpos(newx, newy)
        g9.showturtle()
        if turtle_size - 0.2 != 0:
            turtle_size = turtle_size - 0.2
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(g10, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        g10.setpos(newx, newy)
        g10.showturtle()  
        if turtle_size - 0.3 != 0:
            turtle_size = turtle_size - 0.3
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size

    while collision(g11, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        g11.setpos(newx, newy)
        g11.showturtle()
        if turtle_size - 0.5 != 0:
            turtle_size = turtle_size - 0.5
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(g12, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        g12.setpos(newx, newy)
        g12.showturtle()
        if turtle_size - 1 != 0:
            turtle_size = turtle_size - 1
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(g13, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        g13.setpos(newx, newy)
        g13.showturtle()
        if turtle_size - 0.4 != 0:
            turtle_size = turtle_size - 0.4
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(g14, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        g14.setpos(newx, newy)
        g14.showturtle()
        if turtle_size - 0.2 != 0:
            turtle_size = turtle_size - 0.2
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size
    while collision(g15, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        g15.setpos(newx, newy)
        g15.showturtle()  
        if turtle_size - 0.3 != 0:
            turtle_size = turtle_size - 0.3
        turtle.shapesize(turtle_size)
        turtle_size = turtle_size

def speed():
    turtle.speed(1.3)

def yellow_circles():
    global turtle_speed
    while collision(y1, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        y1.setpos(newx, newy)
        y1.showturtle()
        turtle.speed(0)
        wn.ontimer(speed, 650)
    while collision(y2, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        y2.setpos(newx, newy)
        y2.showturtle()
        turtle.speed(0)
        wn.ontimer(speed, 650)
    while collision(y3, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        y3.setpos(newx, newy)
        y3.showturtle()
        turtle.speed(0)
        wn.ontimer(speed, 650)
    while collision(y4, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        y4.setpos(newx, newy)
        y4.showturtle()
        turtle.speed(0)
        wn.ontimer(speed, 650)
    while collision(y5, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        y5.setpos(newx, newy)
        y5.showturtle()  
        turtle.speed(0)
        wn.ontimer(speed, 650)
    while collision(y6, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        y6.setpos(newx, newy)
        y6.showturtle()
        turtle.speed(0)
        wn.ontimer(speed, 650)
    while collision(y7, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        y7.setpos(newx, newy)
        y7.showturtle()
        turtle.speed(0)
        wn.ontimer(speed, 650)
    while collision(y8, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        y8.setpos(newx, newy)
        y8.showturtle()
        turtle.speed(0)
        wn.ontimer(speed, 650)
    while collision(y9, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        y9.setpos(newx, newy)
        y9.showturtle()
        turtle.speed(0)
        wn.ontimer(speed, 650)
    while collision(y10, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        y10.setpos(newx, newy)
        y10.showturtle()  
        turtle.speed(0)
        wn.ontimer(speed, 650)

def slow():
    turtle.speed(1.3)

def purple_circles():
    global turtle_speed
    while collision(p1, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        p1.setpos(newx, newy)
        p1.showturtle()
        turtle.speed(0.6)
        wn.ontimer(slow, 650)
    while collision(p2, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        p2.setpos(newx, newy)
        p2.showturtle()
        turtle.speed(0.6)
        wn.ontimer(slow, 650)
    while collision(p3, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        p3.setpos(newx, newy)
        p3.showturtle()
        turtle.speed(0.6)
        wn.ontimer(slow, 650)
    while collision(p4, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        p4.setpos(newx, newy)
        p4.showturtle()
        turtle.speed(0.6)
        wn.ontimer(slow, 650)
    while collision(p5, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        p5.setpos(newx, newy)
        p5.showturtle() 
        turtle.speed(0.6)
        wn.ontimer(slow, 650)
    while collision(p6, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        p6.setpos(newx, newy)
        p6.showturtle()
        turtle.speed(0.6)
        wn.ontimer(slow, 650)
    while collision(p7, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        p7.setpos(newx, newy)
        p7.showturtle()
        turtle.speed(0.6)
        wn.ontimer(slow, 650)
    while collision(p8, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        p8.setpos(newx, newy)
        p8.showturtle()
        turtle.speed(0.6)
        wn.ontimer(slow, 650)
    while collision(p9, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        p9.setpos(newx, newy)
        p9.showturtle()
        turtle.speed(0.6)
        wn.ontimer(slow, 650)
    while collision(p10, turtle):
        newx = rand.randint(-230,230)
        newy = rand.randint(-230,230)
        p10.setpos(newx, newy)
        p10.showturtle() 
        turtle.speed(0.6)
        wn.ontimer(slow, 650)


def exit():
    if turtle.xcor() < -250 or turtle.xcor() > 250 or turtle.ycor() < -250 or turtle.ycor() > 250:
        counter.clear()
        

def trun():
    turtle.forward(5)
    if turtle.xcor() < -250 or turtle.xcor() > 250 or turtle.ycor() < -250 or turtle.ycor() > 250:
        quitThis()
    red_circles()
    green_circles()
    yellow_circles()
    purple_circles()
    if timer_up == True:
        x = turtle.xcor()
        y = turtle.ycor()
        turtle.setpos(x,y)
    else:
        wn.ontimer(trun, 1)

def Up():
    if turtle.heading() != 90:
       turtle.speed(0)
       turtle.setheading(90)
       turtle.speed(1.3)
def UpRight():
    if turtle.heading() != -45:
       turtle.speed(0)
       turtle.setheading(45)
       turtle.speed(1.3)
def UpLeft():
    if turtle.heading() != -135:
       turtle.speed(0)
       turtle.setheading(135)
       turtle.speed(1.3)
def Down():
    if turtle.heading() != 270:
       turtle.speed(0)
       turtle.setheading(270)
       turtle.speed(1.3)
def DownRight():
    if turtle.heading() != 45:
       turtle.speed(0)
       turtle.setheading(-45)
       turtle.speed(1.3)
def DownLeft():
    if turtle.heading() != 135:
       turtle.speed(0)
       turtle.setheading(-135)
       turtle.speed(1.3)
def Left():
    if turtle.heading() !=180:
       turtle.speed(0)
       turtle.setheading(180)
       turtle.speed(1.3)
def Right():
    if turtle.heading() != 0:
       turtle.speed(0)
       turtle.setheading(0)
       turtle.speed(1.3)

#   display timer
counter.penup()
counter.goto(100, 200)
counter.pendown()
wn.ontimer(countdown, counter_interval)
        
#   call on functions
wn.onkeypress(Up, "w")
wn.onkeypress(Down, "s")
wn.onkeypress(Left, "a")
wn.onkeypress(Right, "d")
wn.onkeypress(UpRight, "e")
wn.onkeypress(UpLeft, "q")
wn.onkeypress(DownRight, "c")
wn.onkeypress(DownLeft, "z")
wn.listen()

trun()
wn.mainloop()