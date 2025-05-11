text = 'tre tre re ert ret ter rew'

def find_duplicate_words(text):
    words = text.split()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i] == words[j]:
                return words[i]
    return None  

print(find_duplicate_words(text))
