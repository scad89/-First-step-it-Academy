# 1-ый способ(перебор)

list = [3, 10, 5, 25, 2, 8]
max_XOR = 0
for i in range(len(list)):
    for j in range(i+1, len(list)):
        a = list[i] ^ list[j]
        if a > max_XOR:
            max_XOR = a
print(max_XOR)


# 2-ой способ

list = [3, 10, 5, 25, 2, 8]
max_XOR = 0
list.sort()
list.reverse()
a = list[0]
for i in range(1, len(list)):
    xor = a ^ list[i]
    if xor > max_XOR:
        max_XOR = xor
print(max_XOR)

# Тут удалось сократить количество операций почти в три раза, по сравнению с 1-ым способом.
# Вероятно, есть некий другой способ оптимизации кода...
