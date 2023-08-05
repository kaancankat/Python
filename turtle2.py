import turtle
import datetime

turt = turtle.Turtle()

today = datetime.datetime.now()
turt.hideturtle()
turt.penup()
turt.backward((turt.getscreen().window_width() / 2) - 10)
message = "Hello Turtle! \nToday is " + today.strftime("%A") + ', ' + today.strftime("%d") \
           + ', ' + today.strftime("%B") + ', ' + today.strftime("%Y") 

turt.write(message,move=False, font=('monaco',30,'bold'),align='left')
turtle.done()