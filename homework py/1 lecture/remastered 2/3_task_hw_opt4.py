def find_double_ints(ls):

    double_list = []
    for i in ls:
        if i in double_list:
            print(f'Double int {i}')
        double_list.append(i)


ls = []
for i in range(int(input('How many items does the list contain: '))):
    num = int(input())
    ls.append(num)

find_double_ints(ls)
