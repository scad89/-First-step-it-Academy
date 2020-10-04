def minysSYM(*dict):
    num = ''
    for k, v in friendsAndCash.items():    # отделяем $
        for char in friendsAndCash[k]:
            if char.isdigit():
                num = num + char
            else:
                if num != '':
                    friendsAndCash[k] = num
                    num = ''
    return friendsAndCash


def sToint(friendsAndCash):
    for k, v in friendsAndCash.items():    # переводим str в int
        friendsAndCash[k] = int(v)
    return friendsAndCash


def chang(friendsAndCash):    # меняем местами ключи и значения для вывода имени друга с max суммой денег
    new_dict = {value: key for key, value in friendsAndCash.items()}
    return new_dict


def mak(new_dict):
    max_d = 0
    total = 0
    for value in friendsAndCash.values():    # находим максимальное число денег и общее количество
        total += value
        if value > max_d:
            max_d = value
    return max_d, total


friendsAndCash = {'John': '20$', 'Dan': '35$', 'Lois': '14$', 'Doug': '144$'}
new_dict1 = {value: key for key, value in friendsAndCash.items()}
result = minysSYM()
result1 = sToint(result)
result2 = chang(result1)
m, t = mak(result2)
new_dict = result2

print('Общая сумма на руках', t)
print('Самый зажиточный крестьянин', new_dict[m])
print(new_dict1)
