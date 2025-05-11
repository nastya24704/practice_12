text = 'nastya dfgh fgh fg'
def opposite_definition(text):
    word = text.split(' ')
    sentence = word[::-1]
    opposite_sentence = ''.join(sentence)
    return sentence
print(opposite_definition(text))
