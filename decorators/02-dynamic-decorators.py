class FileWithLogging:
    def __init__(self, file):
        self.file = file

    def writelines(self, strings):
        self.file.writelines(strings)
        print(f"wrote {len(strings)} lines")

    # If we were to implement all the methods of file, it would get messy

    # def write(self, item):
    #   ...
    # def close(self):
    #   ...

    # Instead we'll implement methods to delegate concrete implementation for self.file
    def __iter__(self):
        return self.file.__iter__()

    def __next__(self):
        return self.file.__next__()

    def __getattr__(self, key):
        if key == "file":
            return self.file
        else:
            return getattr(self.__dict__["file"], key)

    def __setattr___(self, key, value):
        if key == "file":
            self.__dict__[key] = value
        else:
            setattr(self.__dict__["file"], key, value)

    def __delattr__(self, key):
        delattr(self.__dict__["file"], key)


if __name__ == "__main__":
    file = FileWithLogging(open("hello.tmp", "w"))
    # The following is executed by FileWithLoading.writelines
    file.writelines(["hello", "there!"])
    # However, this one will be delegated
    file.write("hello")
    file.close()
