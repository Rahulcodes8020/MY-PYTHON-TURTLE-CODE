import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("red")
a = 0
b = 0
t.speed(0)
t.penup()
t.goto(2,200)
t.pendown()
while True:
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b ==200:
        break
    t.hideturtle()
t.done()
    

    

