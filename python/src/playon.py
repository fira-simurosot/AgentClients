from src.utilities import ROBOTS_NUM, WheelSpeed


class PlayOn():
    def __init__(self):
        self.wheel_speeds = []
        for i in range(ROBOTS_NUM):
            self.wheel_speeds.append(WheelSpeed())
        self.cnt = 0

    def playon(self, wm):
        self.cnt += 1
        print(self.cnt)
        if self.cnt < 50:
            self.set_wheel_speed(0, 10, 10)
            self.set_wheel_speed(1, 10, 10)
            self.set_wheel_speed(2, 10, 10)
            self.set_wheel_speed(3, 10, 10)
            self.set_wheel_speed(4, 10, 10)
        elif self.cnt < 100:
            self.set_wheel_speed(0, -10, -10)
            self.set_wheel_speed(1, -10, -10)
            self.set_wheel_speed(2, -10, -10)
            self.set_wheel_speed(3, -10, -10)
            self.set_wheel_speed(4, -10, -10)
        else:
            self.cnt = 0
        return self.wheel_speeds

    def set_wheel_speed(self, id, right, left):
        self.wheel_speeds[id].right = right
        self.wheel_speeds[id].left = left
