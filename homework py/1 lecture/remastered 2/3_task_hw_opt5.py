def find_double_ints(ls):

    ls.sort()
    num = 0
    for i in ls:
        if i ^ num == 0:
            print(f'Double int {i}')
        else:
            num = i


ls = []
for i in range(int(input('How many items does the list contain: '))):
    num = int(input())
    ls.append(num)

find_double_ints(ls)
