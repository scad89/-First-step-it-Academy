def find_max_XOR(ls):
    max_XOR = 0
    ls.sort()
    ls.reverse()
    max_value = ls[0]
    for i in range(1, len(ls)):
        xor = max_value ^ ls[i]
        if xor > max_XOR:
            max_XOR = xor
    return max_XOR


ls = []
for i in range(int(input('How many items does the list contain: '))):
    num = int(input())
    ls.append(num)

result = find_max_XOR(ls)
print(f'Maximum XOR value in the list {result}')
