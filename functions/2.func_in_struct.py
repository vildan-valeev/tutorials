def yell(text: str) -> str:
    return text.upper() + '!'


bark = yell

del yell

#########
funcs = [bark, str.lower, str.capitalize]
print(funcs)

for f in funcs:
    print(f, f('всем ку'))

print(funcs[0]('Еще Ку'))


#######
def greet(func):
    greeting = func('Hello! I\'m func')
    print(greeting)


greet(bark)

l = list(map(bark, ['one', 'two', 'ok']))
print(l)
