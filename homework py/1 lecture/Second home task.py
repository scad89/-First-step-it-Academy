# 1-ый способ

def func():

    list = [2, 7, 11, 15]
    for i in list:
        for j in list:
            if i+j == 9:
                print(list.index(i), list.index(j))
                return


func()


def func():

    list = [3, 2, 4]
    for i in list:
        for j in list:
            if i+j == 6 and i != j:
                print(list.index(i), list.index(j))
                return


func()

list = [3, 3]
if list[0] + list[1] == 6 and list[0] == list[1]:
    list[1] = 4
print(list.index(3), list.index(4))

# тут получилось аж 3-и способа:)
