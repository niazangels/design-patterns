def singleton(klass):
    instances = {}

    def get_instance(*a, **kw):
        if klass not in instances:
            instances[klass] = klass(*a, *kw)
        return instances[klass]

    return get_instance


@singleton
class Database:
    def __init__(self, hostname):
        self.hostname = hostname

    def __repr__(self):
        return f"<Database: {self.hostname}>"


if __name__ == "__main__":
    db1 = Database("aws.com")
    db2 = Database("azure.com")

    print(db1)
    print(db2)
