import turtle
import random

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("python Turtle")
FONT= ("arial",30,"normal")
score=0

turtlelist=[]

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
    
    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="score: {}".format(score), move=False, align="center",font=FONT)
    
    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x*grid_size, y*grid_size)
    turtlelist.append(t)

x_coordinates =[-20,-10,0,10,20]
y_coordinates=[20,10,0,-10]

def setup_turtle():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)
            
def hide_turtless():
    for t in turtlelist:
        t.hideturtle()
        
def random_turtle():
    random.choice(turtlelist).showturtle()
        
turtle.tracer(0)

setup_turtle()
score_table()
hide_turtless()
random_turtle()

turtle.tracer(1)


turtle.mainloop()