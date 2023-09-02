class Area:
    def calculate(self, radius):
        return radius * 10

    def calculate(self, height, width):
        return height * width


class Main:
    p1 = Area()
    p1.calculate(height=10, width=20)
