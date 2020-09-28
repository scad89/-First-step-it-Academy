# 1-ый способ(перебор)

def list():
    try:
        a = int(input('Сколько элементов содержит список? '))
        list1 = []
    except ValueError:
        return
    for _ in range(a):
        a1 = int(input())
        list1.append(a1)
    return list1


b = list()
max_XOR = 0
for i in range(len(b)):
    for j in range(i+1, len(b)):
        a = b[i] ^ b[j]
        if a > max_XOR:
            max_XOR = a
print("Максимальный XOR элементов списка =", max_XOR)


# 2-ой способ

def list():
    try:
        a = int(input('Сколько элементов содержит список? '))
        list1 = []
    except ValueError:
        return
    for _ in range(a):
        a1 = int(input())
        list1.append(a1)
    return list1


b = list()
max_XOR = 0
b.sort()
b.reverse()
a = b[0]
for i in range(1, len(b)):
    xor = a ^ b[i]
    if xor > max_XOR:
        max_XOR = xor
print("Максимальный XOR элементов списка =", max_XOR)
