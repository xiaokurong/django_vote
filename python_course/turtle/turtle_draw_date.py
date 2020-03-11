#coding=utf-8
#draw date
import turtle
import time

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
    turtle.fd(40)

def draw_date(date):
    
    for i in date:
        if i == "=" :
            turtle.pencolor("green")
            turtle.write("年",font=("Arial",18))
            turtle.fd(40)
        elif i == "+" :
            turtle.pencolor("yellow")
            turtle.write("月",font=("Arial",18))
            turtle.fd(40)
        elif i == "-" :
            turtle.pencolor("red")
            turtle.write("日",font=("Arial",18))
            turtle.fd(40)
        else:
            turtle.pencolor("black")
            draw_num(eval(i))

def main():
    turtle.setup(900,350,200,200)
    turtle.penup()
    turtle.bk(400)
    turtle.pensize(5)
    draw_date(time.strftime("%Y=%m+%d-",time.gmtime()))

    turtle.hideturtle()
    turtle.done()

main()




        
