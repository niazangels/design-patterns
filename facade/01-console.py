class Buffer:
    def __init__(self, width=30, height=20):
        self.width = width
        self.height = height
        self.buffer = ["*"] * (width * height)

    def write(self, text):
        self.buffer += text

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)


class Viewport:
    def __init__(self, buffer=None):
        if buffer is None:
            buffer = Buffer()
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[index + self.offset]

    def append(self, text):
        self.buffer.write(text)


class Console:
    def __init__(self):
        buffer = Buffer()
        self.current_viewport = Viewport(buffer)
        self.buffer = [buffer]
        self.viewports = [self.current_viewport]

    def write(self, text):
        self.current_viewport.buffer.write(text)

    def get_char_at(self, index):
        return self.current_viewport.get_char_at(index)


if __name__ == "__main__":
    c = Console()
    c.write("Hello there!")
    char = c.get_char_at(0)
    print(char)
