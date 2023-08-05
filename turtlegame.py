import turtle
import random

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("python Turtle")
FONT= ("arial",30,"normal")
#score turtle
def score_table():
    score_turtle = turtle.Turtle()
    score_turtle.color("dark blue")
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.left(90)
    score_turtle.forward(350)
    score_turtle.write(arg="score: 0", move=False, align="center",font=FONT)

grid_size=10
def make_turtle(x,y):
    t=turtle.Turtle()
    
    
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x*grid_size, y*grid_size)

make_turtle(-20,20)
make_turtle(0,30)
make_turtle(10,10)
make_turtle(10,10)
make_turtle(10,10)
make_turtle(10,10)


score_table()
turtle.mainloop()