from turtle import Turtle, Screen
import colorgram
import random

screen = Screen()
turtle = Turtle()

colors = []
x = -200
y = -205

screen.colormode(255)
screen.title("Hirst Painting Simulator")
screen.setup(510, 510)
screen.bgcolor("#333333")
screen.screensize(400, 400)

turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.setposition(x, y)
turtle.speed("fastest")

color_pallete = colorgram.extract("image.jpg", 60)

for color in color_pallete:
    colors.append((color.rgb.r, color.rgb.g, color.rgb.b))


def drawDots():

    for i in range(15):
        turtle.setposition(x, y + (30 * i))
        for j in range(14):
            turtle.dot(20, random.choice(colors))
            turtle.forward(30)


drawDots()

screen.exitonclick()
