import turtle

turtle.width(8)
turtle.color("green")
for i in range(18):
    turtle.penup()
    turtle.goto(0,0)
    turtle.seth(i*20)
    turtle.pendown()
    for j in range(5):
        turtle.circle(40,80)
        turtle.circle(-40,80)
    
