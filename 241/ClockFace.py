
from AnalogWatch import AnalogWatch
from DigitalWatch import DigitalWatch
from Hand import *


class ClockFace:
    def __init__(self, radius=200):
        self.radius = radius
        self.analog_watch = AnalogWatch(radius)
        self.digital_watch = DigitalWatch(radius)
        self.current_watch = self.analog_watch  # default to analog
        self.screen = turtle.Screen()
        self.setup_key_bindings()

    def setup_key_bindings(self):
        self.screen.onkey(self.toggle_watch, "w")  # 'w' to switch watch type
        self.screen.onkey(self.toggle_format, "f")  # 'f' to toggle 12/24 hour format
        self.screen.listen()

    def toggle_watch(self):
        if isinstance(self.current_watch, AnalogWatch):
            self.current_watch = self.digital_watch
        else:
            self.current_watch = self.analog_watch
        self.screen.clear()
        self.current_watch.draw()

    def toggle_format(self):
        if isinstance(self.current_watch, DigitalWatch):
            self.current_watch.toggle_format()

    def draw(self):
        self.current_watch.draw()

    def update(self):
        self.current_watch.update()


def main():
    screen = turtle.Screen()
    screen.title("Розширений годинник")
    clock = ClockFace(200)
    clock.draw()

    while True:
        clock.update()
        screen.update()
        time.sleep(1)


if __name__ == "__main__":
    main()