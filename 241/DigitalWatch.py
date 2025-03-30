import turtle
import time
from Watch import *


class DigitalWatch(Watch):
    def __init__(self, radius=200, format_24h=True):
        super().__init__()
        self.radius = radius
        self.format_24h = format_24h
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        self.t.penup()
        self.t.goto(0, -radius * 0.7)

    def draw(self):
        self.update()

    def update(self):
        now = time.localtime()
        hours = now.tm_hour
        minutes = now.tm_min
        seconds = now.tm_sec

        if not self.format_24h:
            period = "AM" if hours < 12 else "PM"
            hours = hours % 12
            if hours == 0:
                hours = 12
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d} {period}"
        else:
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        self.t.clear()
        self.t.color("hot pink")
        self.t.write(time_str, align="center", font=("Arial", 24, "bold"))

    def toggle_format(self):
        self.format_24h = not self.format_24h
        self.update()


if __name__ == "__main__":
    def test_digital_watch():
        screen = turtle.Screen()
        screen.title("Тест DigitalWatch")
        screen.bgcolor("white")


        watch24 = DigitalWatch(200, format_24h=True)
        watch24.t.goto(-150, 0)
        watch24.draw()

        watch12 = DigitalWatch(200, format_24h=False)
        watch12.t.goto(150, 0)
        watch12.draw()


        def update_time():
            watch24.update()
            watch12.update()
            screen.ontimer(update_time, 1000)

        update_time()
        screen.mainloop()


    test_digital_watch()