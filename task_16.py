def check_brackets(text):
    stack = []
    for i, char in enumerate(text):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if not stack:
                print(f"Ошибка: закрывающая скобка без пары на позиции {i}")
                return False
            stack.pop()
    
    if stack:
        for pos in stack:
            print(f"Ошибка: открывающая скобка без пары на позиции {pos}")
        return False
    
    return True

text = input("Введите текст для проверки скобок: ")
if check_brackets(text):
    print("Скобки расставлены правильно")
else:
    print("Обнаружены ошибки в расстановке скобок")
