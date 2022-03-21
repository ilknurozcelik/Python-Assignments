# OBCEVTIVE :To improve your knowledge of collection types (set),
# boolean logic and raise your awareness of ten fingers keyboard.

# left_hand_letters = set("q", "a", "z", "w", "s", "x", "e", "d", "c", "r","f", "v", "t", "g", "b")
# right_hand_letters = set("y", "h", "n", "u", "j", "m", "ı", "k", "ö", "o", "l", "ç", "p", "ş")

left_hand_letters = set("qazwsxedcrfvtgb")
right_hand_letters = set("yhnujmıköolçpş")
word = set(input("Please enter a word :"))
print(word)
print(word.intersection(left_hand_letters))
print(word.intersection(right_hand_letters))
left_hand_result = len(word.intersection(left_hand_letters))
right_hand_result = len(word.intersection(right_hand_letters))
print("Is the given word comfortable word? : {}".format(bool(left_hand_result and right_hand_result)))
