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
        angle = math.radians(90 - 30 * self.number)
        x = self.radius * math.cos(angle)
        y = self.radius * math.sin(angle)


        if self.number > 9:
            self.t.goto(x, y - 10)  # Для чисел 10,11,12
        else:
            self.t.goto(x, y - 5)  # Для чисел 1-9

        self.t.color("hot pink")
        self.t.write(str(self.number), align="center", font=("Arial", 14, "bold"))




if __name__ == "__main__":
    def test_digit():
        screen = turtle.Screen()
        screen.title("Тест Digit")
        screen.bgcolor("mistyrose")

        for i in range(1, 13):
            digit1 = Digit(i, 150)
            digit1.draw()
        screen.mainloop()
    test_digit()







