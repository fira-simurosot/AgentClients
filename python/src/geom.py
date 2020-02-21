from sympy import Point2D
import math


class Vector2D(Point2D):
    def __init__(self, x=0, y=0):
        super(Point2D, Point2D).__init__(x, y)

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
