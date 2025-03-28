import turtle
import time


class Hand:
    def __init__(self, radius):
        self.radius = radius
        self.hand_turtles = {
            'hour': self.create_hand(radius * 0.5, 6, 'black'),
            'minute': self.create_hand(radius * 0.7, 4, 'black'),
            'second': self.create_hand(radius * 0.9, 2, 'red')
        }

    def create_hand(self, length, width, color):
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)
        t.pensize(width)
        t.color(color)
        t.length = length
        return t

    def update(self):
        now = time.localtime()
        hours = now.tm_hour % 12
        minutes = now.tm_min
        seconds = now.tm_sec

        hour_angle = 90 - (hours * 30 + minutes * 0.5)
        minute_angle = 90 - minutes * 6
        second_angle = 90 - seconds * 6

        self.draw_hand(self.hand_turtles['hour'], hour_angle)
        self.draw_hand(self.hand_turtles['minute'], minute_angle)
        self.draw_hand(self.hand_turtles['second'], second_angle)

    def draw_hand(self, hand, angle):
        hand.clear()
        hand.penup()
        hand.goto(0, 0)
        hand.setheading(angle)
        hand.pendown()
        hand.forward(hand.length)




