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
    
class Set:
    def __init__(self):
        self.stack = Stack()

    def add(self, element):
        current = self.stack.top
        while current:
            if current.data == element:
                return
            current = current.next
        self.stack.push(element)

    def remove(self, element):
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
        print(f'element {element} not found in the set')

    def contains(self, element):
        current = self.stack.top
        while current:
            if current.data == element:
                return True
            current = current.next
        return False

    def __str__(self):
        values = []
        current = self.stack.top
        while current:
            values.append(str(current.data))
            current = current.next
        return f'Set <{id(self)}>: ({', '.join(values)});'

test_set = Set()
print(test_set)
test_set.add(42)
test_set.add('42')
test_set.add(4.2)
print(test_set)
print('Now we remove 4.2!')
test_set.remove(4.2)
print('I wonder if it\'s still there...')
print('Let\'s ask our data structure right away!')
print(f'> {test_set.contains(4.2)}.')
print('Quod erat demonstrandum.')
print(test_set)
