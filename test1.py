def list():
    try:
        a = int(input('Сколько элементов содержит список? '))
        list1 = []
    except ValueError:
        return
    for _ in range(a):
        a1 = int(input())
        list1.append(a1)
    return list1


def target():

    b = list()
    tar = int(input("Target: "))
    for i in b:
        for j in b[1:]:
            if i+j == tar:
                right_index = len(b) - b[::-1].index(i) - 1
                print(b.index(i), right_index)
                return


target()


# my_list = [2, 2]
# right_index = len(my_list) - my_list[::-1].index(n) - 1
