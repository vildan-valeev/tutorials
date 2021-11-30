def yell(text: str) -> str:
    return text.upper() + '!'


print(yell('привет'))
bark = yell

print(bark('woo'))

del yell

# print(yell('yell name deleted, not func object'))

print(bark('bark not delete'))

print(bark.__name__)