# from typing import
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


def draw_point(p: Point):
    print(".", end=" ")


# ^^ This is given


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end


class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x + width, y + height), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x, y)))


class LineToPointAdapter(list):
    count = 0


def draw_rectangles(rectangle):
    for rectangle in rectangles:
        for line in rectangle:
            draw_line()


if __name__ == "__main__":
    rs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6),
    ]




class Square:
    def __init__(self, side=0):
        self.side = side

def calculate_area(rc):
    return rc.width * rc.height

class SquareToRectangleAdapter:
    def __init__(self, square):
        