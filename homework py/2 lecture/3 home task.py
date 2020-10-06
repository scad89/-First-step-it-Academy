def delete_characters(*dict):
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


def transformation_str_to_int(friendsAndCash):
    for k, v in friendsAndCash.items():    # переводим str в int
        friendsAndCash[k] = int(v)
    return friendsAndCash


# меняем местами ключи и значения для вывода имени друга с max суммой денег
def change_key_to_value(friendsAndCash):
    new_dict = {value: key for key, value in friendsAndCash.items()}
    return new_dict


def max_cash_and_total_cash(new_dict):
    max_cash = 0
    total_cash = 0
    for value in friendsAndCash.values():    # находим максимальное число денег и общее количество
        total_cash += value
        if value > max_cash:
            max_cash = value
    return max_cash, total_cash


friendsAndCash = {'John': '20$', 'Dan': '35$', 'Lois': '14$', 'Doug': '144$'}
new_dict1 = {value: key for key, value in friendsAndCash.items()}
result = delete_characters()
result1 = transformation_str_to_int(result)
result2 = change_key_to_value(result1)
m_cash, t_cash = max_cash_and_total_cash(result2)
new_dict = result2

print('Общая сумма на руках', t_cash)
print('Самый зажиточный крестьянин', new_dict[m_cash])
print(new_dict1)
