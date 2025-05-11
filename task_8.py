sentence = "настя привет пока нет да зачем почему"
def new_sentence(sentence):
  words = sentence.split()
  n = len(words)
  for i in range(n):
      for j in range(0, n - i - 1):
          if len(words[j]) > len(words[j + 1]):
              words[j], words[j + 1] = words[j + 1], words[j]
  return " ".join(words)
print(new_sentence(sentence))
