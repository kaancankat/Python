import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("python Turtle")
turtle.shape("turtle")
turtle_instance = turtle.Turtle()

def a():
    #for i in range(4):
    turtle_instance.forward(50)
        #turtle_instance
def right():
    turtle_instance.right(90)

def left():
    turtle_instance.left(90)
def b():
    turtle_instance.circle(50)
def clear():
    turtle_instance.clear()
drawing_board.listen()
drawing_board.onkey(fun=a , key="space")
drawing_board.onkey(fun=right , key="d")
drawing_board.onkey(fun=left , key="a")
drawing_board.onkey(fun=b , key="b")
drawing_board.onkey(fun=clear , key="c")
turtle.done()