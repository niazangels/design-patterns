class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def __iter__(self):
        return traverse_in_order(self)


def traverse_in_order(root):
    def traverse(current):
        if current.left:
            for left in traverse(current.left):
                yield left
        yield current
        if current.right:
            for right in traverse(current.right):
                yield right

    for node in traverse(root):
        yield node


for i in Node(2, Node(1), Node(3)):
    print(i.value)
