text = '''1234 344 12
45678 763 654
879 67 98'''
def simbol(text):
    a, b, c = text.split('\n')
    list = []
    for ch in text:
        count = 0
        if ch in a:
            count +=1
        if ch in b:
            count += 1
        if ch in c:
            count += 1
        if count == 1:
            list.append(ch)
    all_chars = []
    for i in list:
        if i not in all_chars:
            all_chars.append(i)

    return all_chars
print(simbol(text))
