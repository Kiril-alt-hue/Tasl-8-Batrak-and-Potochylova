from pygame.draw import circle

from Watch import Watch
import turtle
import time
from Digits import Digit
from Hand import Hand

class AnalogWatch(Watch):
    def __init__(self, radius=200):
        self.radius = radius
        self.digits = []
        for i in range(1, 13):
            digit = Digit(i, radius * 0.8)
            self.digits.append(digit)
        self.hands = Hand(radius)

    def draw(self):
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)
        t.penup()
        t.goto(0, -self.radius)
        t.pendown()
        t.color("hot pink", "white")  # Контур чорний, заливка біла
        t.begin_fill()
        t.circle(self.radius)
        t.end_fill()


        screen = turtle.Screen()
        screen.bgcolor("mistyrose")

        for digit in self.digits:
            digit.draw()

        self.hands.update()

    def update(self):
        self.hands.update()

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.tracer(0) #вимкнення автооновлення для плавності

    test_watch = AnalogWatch(200)

    test_watch.draw()
    screen.update()

    while True:
        test_watch.update()
        screen.update()
        time.sleep(1)
