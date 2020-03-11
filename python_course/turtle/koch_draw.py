#kochdraw
import turtle

def koch(size,n):
    if n == 0 :
        turtle.fd(size)
    else :
        for angle in [0,60,-120,60] :
            turtle.left(angle)
            koch(size/3,n-1)

def main() :
    turtle.setup(800,800)
    turtle.penup()
    turtle.pensize(5)
    turtle.pencolor("green")
    turtle.goto(-300,200)
    turtle.pendown()
    koch(400,3)
    turtle.right(120)
    koch(400,3)
    turtle.right(120)
    koch(400,3)
    turtle.hideturtle()
    

main()
