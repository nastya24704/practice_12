text = "1234 344 12"
def simbol(text):
    for ch in text:
        if text.count(ch)==3:
            return ch

print(simbol(text))
