text = "1234 344 12"
def simbol(text):
    list = []
    for i in text:
        if i not in list:
            list.append(i)
    return len(list)

print(simbol(text))
