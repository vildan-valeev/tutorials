from collections import Counter

lst = [1, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 7, 5, 4, 56, 56, 7, 7, 43, 23, 4, 55, 66, 7, ]
print(Counter(lst))


sentence = 'Hello, how are you doing? hello, I\'m fine'
c = Counter(sentence.split(' '))

print(c)
print(list(c))
print(set(c))
print(dict(c))
