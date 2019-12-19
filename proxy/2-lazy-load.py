class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f"Loading image from {self.filename}")

    def draw(self):
        print("Drawing the image")


def draw(image):
    print(f"About to draw {image.filename}")
    image.draw()
    print(f"Done drawing {image.filename}")
    print("-" * 80)


def fake_draw(image):
    print(f"About to fake draw {image.filename}")
    print(f"Done faking drawing {image.filename}")
    print("-" * 80)


class LazyBitmap:
    def __init__(self, filename: str):
        self.filename: str = filename
        self.initialized: bool = False

    def lazy_init(self):
        if self.initialized:
            return
        self.image = Bitmap(self.filename)
        self.initialized = True

    def draw(self):
        self.lazy_init()
        self.image.draw()


if __name__ == "__main__":
    # This will load the image even if we don't ever draw it
    bmp = Bitmap("jagathi.jpg")
    fake_draw(bmp)
    draw(bmp)

    # This will not load anything until we really need it
    bmp = LazyBitmap("jayan.jpg")
    fake_draw(bmp)
    draw(bmp)
