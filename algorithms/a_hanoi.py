def hanoi(n, source, helper, target):
    if n > 0:
        hanoi(n - 1, source, target, helper)
        if source:
            target.append(source.pop())
        hanoi(n - 1, helper, source, target)



print(hanoi(3, 3, 0, 0))
