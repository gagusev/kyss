from models.exceptions import StackError

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
        try:
            new_node = StackNode(data)
            new_node.next = self.top
            self.top = new_node
        except Exception as e:
            raise StackError(e)
        
    def pop(self):
        try:
            if self.is_empty():
                raise IndexError('pop from empty stack')
            popped_node = self.top
            self.top = self.top.next
            return popped_node.data
        except Exception as e:
            raise StackError(e)

    def peek(self):
        try:
            if self.is_empty():
                raise KeyError('peek from empty stack')
            return self.top.data
        except Exception as e:
            raise StackError(e)

    def __str__(self):
        values = []
        current = self.top
        while current:
            values.append(str(current.data))
            current = current.next
        return f'Stack <{id(self)}>: [{'] -> ['.join(values)}];'