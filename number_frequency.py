from collections import Counter
x = [1, 3, 7, 4, 3, 0, 3, 6, 3] 
n = Counter(x)
print(n)
# print(n.most_common(1))
result = n.most_common(1)
print(result)
print("The most frequent number is {} , and it was {} times repeatead.".format(result[0][0] , result[0][1]))

