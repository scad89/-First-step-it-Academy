# 1-ый способ(перебор)
list = [1, 3, 4, 2, 2]
for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] == list[j]:
            print(list[i])

list = [3, 1, 3, 4, 2]    # 33 операций
for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] == list[j]:
            print(list[i])


# 2-ой способ(перебор через один цикл и сортировку)

list = [1, 3, 4, 2, 2]
list.sort()
num = 0
for i in list:
    if i != num:
        num = i
    else:
        print(num)
        break

list = [3, 1, 3, 4, 2]    # 16 операций
list.sort()
num = 0
for i in list:
    if i != num:
        num = i
    else:
        print(num)
        break

# 3-ий способ(через множества)

list = [1, 3, 4, 2, 2]
for i in set(list):
    if list.count(i) > 1:
        print(i)
        break

list = [3, 1, 3, 4, 2]    # 9 операций
for i in set(list):
    if list.count(i) > 1:
        print(i)
        break

# 4-ый способ(проверкой количества раз вхождения элемента в список):

list = [1, 3, 4, 2, 2]
list.sort()    # таким образом сокращу количество операций
for i in list:
    if list.count(i) >= 2:
        print(i)
        break

list = [3, 1, 3, 4, 2]    # 5 операций
for i in list:
    if list.count(i) >= 2:
        print(i)
        break
