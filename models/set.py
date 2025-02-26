from models.stack import Stack
from models.exceptions import SetError

class Set:
    def __init__(self):
        self.stack = Stack()

    def add(self, element):
        try:
            current = self.stack.top
            while current:
                if current.data == element:
                    return
                current = current.next
            self.stack.push(element)
        except Exception as e:
            raise SetError(e, 'add', element)

    def remove(self, element):
        try:
            current = self.stack.top
            prev = None
            while current:
                if current.data == element:
                    if prev:
                        prev.next = current.next
                    else:
                        self.stack.top = current.next
                    return
                prev = current
                current = current.next
            raise KeyError(f'element {element} not found in the set')
        except Exception as e:
            raise SetError(e, 'remove', element)

    def contains(self, element):
        try:
            current = self.stack.top
            while current:
                if current.data == element:
                    return True
                current = current.next
            return False
        except Exception as e:
            raise SetError(e, 'contains', element)

    def __str__(self):
        values = []
        current = self.stack.top
        while current:
            values.append(str(current.data))
            current = current.next
        return f'Set <{id(self)}>: ({', '.join(values)});'
    