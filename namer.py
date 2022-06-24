from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Arial", 8, "normal")

class Namer(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def place_name(self, text, x, y):
        self.write(text, align=ALLIGNMENT, font=FONT)
        self.goto(x, y)
