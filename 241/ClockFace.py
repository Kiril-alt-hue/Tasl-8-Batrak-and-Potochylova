import turtle
import time
import math
from Digits import *

class ClockFace:
    def __init__ (self, radius = 200):
        self.radius = radius
        self.digits = []
        for i in range(1, 13):
            digit = Digit(i, radius * 0.8)
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
            digit.draw()# Тестовий приклад для класу ClockFace

def test_clockface():
    screen = turtle.Screen()
    screen.title("Тест ClockFace")
    screen.bgcolor("white")

    # Тест 1: Стандартний циферблат
    clock1 = ClockFace(200)
    clock1.draw()


    screen.mainloop()

# Виклик тесту
test_clockface()

