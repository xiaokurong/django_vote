#turtle draw count back 9 -- 1
import turtle

def draw_line(tf):
    if tf == True :
        turtle.penup()
        turtle.fd(5)
        turtle.pendown()
        turtle.fd(30)
        turtle.penup()
        turtle.fd(5)
        
    else:
        turtle.penup()
        turtle.fd(40)
    turtle.right(90)
        
def draw_num(num):
    draw_line(True) if num in [2,3,4,5,6,8,9] else draw_line(False)
    draw_line(True) if num in [0,1,3,4,5,6,7,8,9] else draw_line(False)
    draw_line(True) if num in [0,2,3,5,6,8,9] else draw_line(False)
    draw_line(True) if num in [0,2,6,8] else draw_line(False)
    turtle.left(90)
    draw_line(True) if num in [0,4,5,6,8,9] else draw_line(False)
    draw_line(True) if num in [0,2,3,5,6,7,8,9,] else draw_line(False)
    draw_line(True) if num in [0,1,2,3,4,7,8,9] else draw_line(False)
    turtle.right(180)
    turtle.penup()
    turtle.bk(40)
    #turtle.right(180)

def main():
    turtle.setup(800,400,200,200)
    list_num=list(range(10))
    
    for i in list_num[::-1] :
        
        turtle.pencolor("red")
        turtle.pensize(10)
        turtle.speed(8)
        turtle.hideturtle()
        draw_num(i)
        turtle.clear()

main()
        
        
