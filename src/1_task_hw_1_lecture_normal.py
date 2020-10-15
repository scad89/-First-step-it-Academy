def find_max_XOR(ls):
    max_XOR = 0
    for i in range(len(ls)):
        for j in range(i+1, len(ls)):
            a = ls[i] ^ ls[j]
            if a > max_XOR:
                max_XOR = a
    return max_XOR


ls = []
for i in range(int(input('How many items does the list contain: '))):
    num = int(input())
    ls.append(num)

result = find_max_XOR(ls)
print(f'Maximum XOR value in the list {result}')
