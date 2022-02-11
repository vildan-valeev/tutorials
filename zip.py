def whos_first(p1, p2):
    for i, k in zip(p1, p2):
        if i == k:
            continue
        if i != ' ':
            return 'p1'
        if k != ' ':
            return 'p2'
        print(i)
    return 'tie'

print(whos_first("  3", ' 3'))
print()
