text = "1234 344 12"
def simbol(text):
    count = 0
    simbole = []
    for i in text:
        if i not in simbole:
            simbole.append(i)
    return len(simbole)

print(simbol(text))
