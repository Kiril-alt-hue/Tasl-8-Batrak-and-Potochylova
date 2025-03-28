from Digits import *
from Hand import *


class ClockFace:
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
        t.circle(self.radius)


        for digit in self.digits:
            digit.draw()

        #малюємо стрілки
        self.hands.update()


def main():
    screen = turtle.Screen()
    screen.title("Простий годинник")
    clock = ClockFace(200)
    clock.draw()


    while True:
        clock.hands.update()
        screen.update()
        time.sleep(1)


if __name__ == "__main__":
    main()