import string
import random

s = string.ascii_lowercase
c = 0

# while c < 5:
#     random.choice(string.ascii_letters)
#     c += 1

t = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
print(t)