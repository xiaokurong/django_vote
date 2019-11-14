import turtle

turtle.width(8)
turtle.color("green")
for i in range(18):
    turtle.penup()
    turtle.goto(0,0)
    turtle.seth(i*20)
    turtle.pendown()
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(100)
        
    
