c = 'helllo'

l = [i for i in c]
print(l)

numbs = [n * n for n in range(0, 11)]
print(numbs)


numbs = [n * n for n in range(0, 11) if n % 2 != 0]
print(numbs)

rating = [2845, 2564, 2485, 2600]
titles = ['GM' if x >= 2500 else 'MM' for x in rating]
print(titles)