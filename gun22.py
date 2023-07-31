import turtle
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

for i in range(10):
    turtle_instance.circle(100)
    turtle_instance.circle(-100)

turtle.done()