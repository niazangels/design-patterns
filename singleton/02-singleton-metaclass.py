class Singleton:
    """
    class Singleton:` does not work because 
    >>> '__call__' in dir(object)
    False
    >>> '__call__' in dir(type)
    True
    """

    instances = {}

    def __call__(cls, *a, **kw):
    """Even though `__call__` is a classmethod, it doesn't need a decorator"""
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*a, **kw)
        return cls.instances[cls]


class Database(metaclass=Singleton):
    def __init__(self, hostname):
        self.hostname = hostname

    def __repr__(self):
        return f"<Database: {self.hostname}>"


if __name__ == "__main__":
    db1 = Database("aws.com")
    db2 = Database("azure.com")

    print(db1)
    print(db2)
