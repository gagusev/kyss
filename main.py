import sys

sys.tracebacklimit = 0

class StackError(Exception):
    def __init__(self, original_exception):
        super().__init__(f"Error occurred in Stack operation: {str(original_exception)}")
        self.original_exception = original_exception

class CipheringError(Exception):
    def __init__(self, original_exception, element):
        super().__init__(f"Error occurred while ciphering element '{element}': {str(original_exception)}")
        self.original_exception = original_exception
        self.element = element

class SetError(Exception):
    def __init__(self, original_exception, operation, element=None):
        if element:
            super().__init__(f"Error occurred in Set operation '{operation}' with element '{element}': {str(original_exception)}")
        else:
            super().__init__(f"Error occurred in Set operation '{operation}': {str(original_exception)}")
        self.original_exception = original_exception
        self.operation = operation
        self.element = element

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
    
def is_latin_string(s):
    return all(char.isalpha() or char.isspace() for char in s)

def apply_cipher(func):
    def wrapper(input_set, **kwargs):
        encrypted_set = Set()
        current = input_set.stack.top
        while current:
            element = current.data
            try:
                if not isinstance(element, str):
                    raise ValueError(f'set element \'{element}\' is not a string')
                if not is_latin_string(element):
                    raise ValueError(f'set element \'{element}\' contains non-Latin characters')
                encrypted_set.add(func(element, **kwargs))
            except Exception as e:
                raise CipheringError(e, element)
            current = current.next
        return encrypted_set
    return wrapper


@apply_cipher
def caesar_cipher_set(element, shift=3):
    return ''.join(
        chr(((ord(char) - 97 + shift) % 26) + 97) if char.islower() else
        chr(((ord(char) - 65 + shift) % 26) + 65) if char.isupper() else
        char
        for char in element
    )

@apply_cipher
def atbash_cipher_set(element):
    return''.join(
        chr(155 - ord(char)) if char.isupper() else
        chr(219 - ord(char)) if char.islower() else
        char
        for char in element
    )

test_set = Set()
test_set.add(42)
print(caesar_cipher_set(test_set))