def ch(a, b):
    a, b = b, a
    return a, b


a, b = int(input('a: ')), int(input('b: '))
print(ch(a, b))
