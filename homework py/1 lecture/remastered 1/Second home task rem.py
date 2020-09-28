# 1-ый способ

import itertools


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
    for i in range(len(b)-1):
        for j in range(i+1, len(b)):
            if b[i]+b[j] == tar:
                print(i, j)
                return


target()


# 2-ой способ(оптимизация)


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
    comb = itertools.combinations(range(len(b)), 2)
    for i, j in comb:
        if b[i] + b[j] == tar:
            print(i, j)
            return
