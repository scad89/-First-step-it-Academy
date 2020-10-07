def find_double_ints(ls):

    for i in set(ls):
        if ls.count(i) > 1:
            print(f'Double int {i}')
            break


ls = []
for i in range(int(input('How many items does the list contain: '))):
    num = int(input())
    ls.append(num)

find_double_ints(ls)
