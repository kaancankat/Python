import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("python Turtle")
FONT= ("arial",30,"normal")
#score turtle
score_turtle = turtle.Turtle()

score_turtle.color("dark blue")
score_turtle.hideturtle()
score_turtle.write(arg="score: 0", move=False, align="center",font=FONT)






turtle.mainloop()