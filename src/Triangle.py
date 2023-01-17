from src.Figure import Figure

class Triangle(Figure):
    def __init__(self, a, b,c):
        super().__init__(a, b,c)


    @property
    def area_triangle(self, b, a):

        return 0.5*self.b*self.a

    @property
    def perimeter_triangle(self):
        return self.a + self.b + self.c


triangle = Triangle(b=5, a=4)
print(triangle.area_triangle)

triangle = Triangle(a=5, b=4, c=1)
print(triangle.perimeter_triangle)
