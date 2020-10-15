def find_index_for_target(ls):

    for i in range(len(ls)-1):
        for j in range(i+1, len(ls)):
            if ls[i]+ls[j] == target:
                print([i, j])
    return


ls = []
for i in range(int(input('How many items does the list contain: '))):
    num = int(input())
    ls.append(num)
target = int(input('Target: '))

find_index_for_target(ls)
