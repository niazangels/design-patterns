import abc


class Shape(abc.ABC):
    @abc.abstractclassmethod
    def __repr__(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, scale):
        self.radius *= scale

    def __repr__(self):
        return f"A Circle of radius {self.radius}"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __repr__(self):
        return f"A Square of side {self.side}"


class ColoredShape(Shape):
    def __init__(self, shape, color):
        if isinstance(shape, ColoredShape):
            raise TypeError("Cannot apply color decorator twice")
        self.shape = shape
        self.color = color

    def __repr__(self):
        return f"{self.shape} has color {self.color}"


class TransparentShape(Shape):
    def __init__(self, shape, transparency: float):
        self.shape = shape
        self.transparency = transparency

    def __repr__(self):
        return f"{self.shape} has {self.transparency *100}% transparency"


if __name__ == "__main__":
    circle = Circle(1)
    print(circle)

    circle.resize(2)
    print(circle)

    red_circle = ColoredShape(Circle(2), color="red")
    print(red_circle)

    # Cannot call methods of Circle:
    try:
        red_circle.resize(2)
    except Exception as e:
        print(f"ERROR: {e}")

    red_half_transparent_circle = TransparentShape(red_circle, transparency=0.5)
    print(red_half_transparent_circle)

    # Nothing prevents us from applying the class twice unless we actually check for it
    try:
        mixed_color_circle = ColoredShape(red_circle, color="blue")
        print(mixed_color_circle)
    except TypeError as e:
        print(f"ERROR: {e}")

    # But even that does not prevent us from doing this:
    mixed_color_circle = ColoredShape(
        TransparentShape(ColoredShape(circle, "red"), 1), "blue"
    )
    print(mixed_color_circle)
