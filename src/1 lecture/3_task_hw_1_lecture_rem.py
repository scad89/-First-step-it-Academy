def find_double_ints(ls):

    ls.sort()
    for i in range(len(ls)):
        if ls[i] ^ ls[i+1] == 0:
            print(f'Double int {ls[i]}')
            break


ls = []
for i in range(int(input('How many items does the list contain: '))):
    num = int(input())
    ls.append(num)

find_double_ints(ls)
