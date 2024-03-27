import math

class AreaCalculator:
    """БИБЛИОТКА РАССЧЕТА ПЛОЩАДИ КРУГА И ТРЕУГОЛЬНИКА, А ТАКЖЕ ЯВЛЯЕТСЯ ЛИ ТРЕУГОЛЬНИК ПРЯМОУГОЛЬНЫМ::
    Пример площади круга:   circle_area(радиус)
    Пример площади треугольника: triangle_area(сторона1, сторона2, сторона3)
    Проверка "прямоугольности" треугольника: is_right_triangle(сторона1, сторона2, сторона3)
    """
    def circle_area(self, radius):
        "Радиус => площадь"
        return math.pi * radius**2

    def triangle_area(self, side1, side2, side3):
        "Три стороны => площадь"
        s = (side1 + side2 + side3) / 2
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    def is_right_triangle(self, side1, side2, side3):
        "Три стороны => проверка угла на присутствие угла 90 градусов (True,False) "
        sides = [side1, side2, side3]
        max_side = max(sides)
        sides.remove(max_side)
        return max_side**2 == sides[0]**2 + sides[1]**2

