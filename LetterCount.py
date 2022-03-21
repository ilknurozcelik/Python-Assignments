sentence = (input("Please enter a sentence : ")).lower()
letter_count = {}

for i in sentence:
  if i not in letter_count:
    letter_count[i] = 1
  else:
    letter_count[i] += 1

print(letter_count)
