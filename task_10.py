text = 'tre tre re ert ret ter rew'

def new_words(text):
    words = text.split()
    first_word = words[0]
    result = []

    for word in words[1:]:
        if word == first_word:
            continue
        has_duplicates = False
        for i in range(len(word)):
            for j in range(i + 1, len(word)):
                if word[i] == word[j]:
                    has_duplicates = True
                    break
            if has_duplicates:
                break

        if not has_duplicates:
            result.append(word)

    print(*result if result else "Таких слов нет")

print(new_words(text))
