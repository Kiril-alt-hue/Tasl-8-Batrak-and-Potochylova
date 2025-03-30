
from AnalogWatch import AnalogWatch
from DigitalWatch import DigitalWatch
import turtle
import time


class ClockFace:
    def __init__(self, analog_radius=200, digital_radius=200):
        self.analog = AnalogWatch(analog_radius)

        self.digital_12h = DigitalWatch(digital_radius, format_24h=False)
        self.digital_24h = DigitalWatch(digital_radius, format_24h=True)
        self.digital_12h.t.goto(analog_radius + 150, 0)
        self.digital_24h.t.goto(analog_radius - 550, 0)

        self.screen = turtle.Screen()


    def toggle_analog(self):
        self.analog.draw()
        self.screen.update()

    def toggle_digital(self):
        self.digital_12h.draw()
        self.digital_24h.draw()
        self.screen.update()

    def draw(self):
        self.analog.draw()
        self.digital_12h.draw()
        self.digital_24h.draw()

    def update(self):
        self.analog.update()
        self.digital_12h.update()
        self.digital_24h.update()

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.tracer(0)

    clock_face = ClockFace()
    clock_face.draw()
    screen.update()

    while True:
        clock_face.update()
        screen.update()
        time.sleep(1)

