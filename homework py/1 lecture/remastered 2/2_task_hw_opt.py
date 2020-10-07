def find_index_for_target(ls):

    double_list = []
    target = int(input('Target: '))
    for index, value in enumerate(ls):
        if (target - value) in double_list:
            print(double_list.index(target - value), index)
        double_list.append(value)
    return


ls = []
for i in range(int(input('How many items does the list contain: '))):
    num = int(input())
    ls.append(num)

find_index_for_target(ls)
