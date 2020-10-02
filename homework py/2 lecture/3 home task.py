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


def chang(friendsAndCash):    # меняем местами ключи и значения для вывода имени друга
    new_dict = {value: key for key, value in friendsAndCash.items()}
    return new_dict


def mak(new_dict):
    max_d = 0
    for value in friendsAndCash.values():    # находим максимальное число денег
        if value > max_d:
            max_d = value
    return max_d


def ttal(new_dict):
    total = 0
    for value in friendsAndCash.values():    # общее количество денег
        total += value
    return total


friendsAndCash = {'John': '20$', 'Dan': '35$', 'Lois': '14$', 'Doug': '144$'}
new_dict1 = {value: key for key, value in friendsAndCash.items()}
result = minysSYM()
result1 = sToint(result)
result2 = chang(result1)
result3 = mak(result2)
result4 = ttal(result2)
new_dict = result2

print('Общая сумма на руках', result4)
print('Самый зажиточный крестьянин', new_dict[result3])
print(new_dict1)
