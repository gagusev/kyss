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