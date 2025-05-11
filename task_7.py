text = 'nastya dfgh fgh fg'
def min_word(text):
    word = text.split()
    return min(len(min_w) for min_w in word)

print(min_word(text))
