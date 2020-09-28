# этот способ решает [2, 7, 11, 15] target = 9 и [3, 2, 4] target = 6:

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
        for j in b:
            if i+j == tar:
                print(b.index(i), b.index(j))
                return


target()


# а этот [3, 3] target = 6

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
