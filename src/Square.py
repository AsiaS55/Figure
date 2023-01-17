from src.Figure import Figure
class Square(Figure):
    def __init__(self, a):
        super().__init__(a)
    @property
    def area_square(self):
        return self.a*self.a

    @property
    def perimeter_square(self):
        return 4 * self.a


square = Square (a=5)
print(square.perimeter_square)

print(square.area_square)