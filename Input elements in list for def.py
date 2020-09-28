def list():
    try:
        a = int(input('Сколько элементов будет содержать список? '))
        list1 = []
    except ValueError:
        return
    for _ in range(a):
        a1 = int(input())
        list1.append(a1)
    return list1


print(list())
