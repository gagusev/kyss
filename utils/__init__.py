def is_latin_string(s):
    return all(char.isalpha() or char.isspace() for char in s)