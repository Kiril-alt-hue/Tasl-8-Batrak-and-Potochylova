import time
import math
import turtle
class Digit:
    def __init__(self, number, radius):
        self.number = number
        self.radius = radius
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        self.t.penup()

    def draw(self):
        angle = math.radians(-90 + 30 * self.number)
        x = self.radius * math.cos(angle)
        y = self.radius * math.sin(angle)

if __name__ == "__main__":
    def test_digit():
        screen = turtle.Screen()
        screen.title("Тест Digit")
        screen.bgcolor("white")


        digit1 = Digit(3, 150)
        digit1.draw()
        screen.mainloop()
    test_digit()




