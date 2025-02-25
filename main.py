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
    
def is_latin_string(s):
    return all(char.isalpha() or char.isspace() for char in s)

def caesar_cipher_set(input_set, shift=3):
    encrypted_set = Set()
    current = input_set.stack.top
    while current:
        element = current.data
        if not isinstance(element, str):
            print(f'set element \'{element}\' is not a string')
        if not is_latin_string(element):
            print(f'set element \'{element}\' contains non-Latin characters')
        encrypted_element = ''.join(
            chr(((ord(char) - 97 + shift) % 26) + 97) if char.islower() else
            chr(((ord(char) - 65 + shift) % 26) + 65) if char.isupper() else
            char
            for char in element
        )
        encrypted_set.add(encrypted_element)
        current = current.next
    return encrypted_set

def atbash_cipher_set(input_set):
    atbash_set = Set()
    current = input_set.stack.top
    while current:
        element = current.data
        if not isinstance(element, str):
            raise print(f'set element \'{element}\' is not a string')
        if not is_latin_string(element):
            raise print(f'set element \'{element}\' contains non-Latin characters')
        atbash_element = ''.join(
            chr(155 - ord(char)) if char.isupper() else
            chr(219 - ord(char)) if char.islower() else
            char
            for char in element
        )
        atbash_set.add(atbash_element)
        current = current.next
    return atbash_set

test_set = Set()
test_set.add('long live the king')
test_set.add('The king is dead')
print(test_set)
print('Ah what a set!')
print('Let\'s run it through a Caesar cipher:')
print(caesar_cipher_set(test_set))
print('And what about an Atbash one?')
print(atbash_cipher_set(test_set))
print('So who\'s gonna stop as from layering both ciphers now??')
print('\033[30;103mScience isn\'t about WHY, it\'s about WHY NOT!\033[0m')
print(atbash_cipher_set(caesar_cipher_set(test_set)))
