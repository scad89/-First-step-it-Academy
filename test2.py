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
