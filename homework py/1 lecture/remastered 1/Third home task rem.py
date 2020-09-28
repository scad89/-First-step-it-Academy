# 1-ый способ:

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
for i in range(len(b)):
    for j in range(i+1, len(b)):
        if b[i] == b[j]:
            print("Повторяется элемент", b[i])


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
b.sort()
num = 0
for i in b:
    if i != num:
        num = i
    else:
        print("Повторяется элемент", num)
        break


# 3-ий способ

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
for i in set(b):
    if b.count(i) > 1:
        print("Повторяется элемент", i)
        break


# 4-ый способ

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
for i in b:
    if b.count(i) >= 2:
        print("Повторяется элемент", i)
        break
