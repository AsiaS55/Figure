from src.Figure import Figure

class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__(a, b)

    @property
    def area_rectangle(self):
        return self.a*self.b

    @property
    def perimeter_rectangle(self):
        return 2 * (self.a + self.b)

rectangle = Rectangle (a=5, b=2)
print(rectangle.perimeter_rectangle)

print(rectangle.area_rectangle)




