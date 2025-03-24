import turtle
import time
import math

class ClockFace:
    def __init__ (self, radius = 200):
        self.radius = radius
        self.digits = []
        for i in range(1, 13):
            digit = Digits(i, radius * 0.8)
            self.digits.append(digit)

    def draw(self):
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)
        t.penup()
        t.goto(0, -self.radius)
        t.pendown()
        t.circle(self.radius)
        t.penup()

        for digit in self.digits:
            digit.draw()