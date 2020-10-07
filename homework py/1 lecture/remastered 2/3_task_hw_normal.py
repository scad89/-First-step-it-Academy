def find_double_ints(ls):

    for i in range(len(ls)):
        for j in range(i+1, len(ls)):
            if ls[i] == ls[j]:
                print(f'Double int {ls[i]}')


ls = []
for i in range(int(input('How many items does the list contain: '))):
    num = int(input())
    ls.append(num)

find_double_ints(ls)
