import keyword

def is_valid_python_identifier(name):
    if not name:
        return False
    if keyword.iskeyword(name):
        return False
    first_char = name[0]
    if not (first_char.isalpha() or first_char == '_'):
        return False
    for char in name[1:]:
        if not (char.isalnum() or char == '_'):
            return False
    
    return True

test_names = ["nastya_name", "2types", "_privet", "class", "import", "MyType"]
for name in test_names:
    print(f"'{name}': {'Да' if is_valid_python_identifier(name) else 'Нет'}")
