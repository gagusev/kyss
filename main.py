class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'Node <{id(self)}>: [{self.data}];'

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print('pop from empty stack')
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def peek(self):
        if self.is_empty():
            print('peek from empty stack')
            return None
        return self.top.data

    def __str__(self):
        values = []
        current = self.top
        while current:
            values.append(str(current.data))
            current = current.next
        return f'Stack <{id(self)}>: [{'] -> ['.join(values)}];'

stack = Stack()
print(stack)
stack.push(42)
stack.push('42')
stack.push(4.2)
print(stack)
print(f'Value we pop out: {stack.pop()};')
print(stack)
print(f'Value we peek: {stack.peek()};')
print(stack)
