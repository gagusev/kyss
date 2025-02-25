class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'Node <{id(self)}>: [{self.data}];'


node = StackNode(42)
print(node)
