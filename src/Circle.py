import math

from src.Figure import Figure
class Circle(Figure):
    def __init__(self, r):
        super().__init__(r)

    @property
    def area_circle(self):
        return math.pi * self.r * self.r

    @property
    def perimeter_circle(self):
        return math.pi*2 * self.r

circle = Circle (r=5)
print(circle.perimeter_circle)

print(circle.area_circle)