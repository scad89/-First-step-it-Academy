def string_combinations(string):
    if len(string) == 1:
        return [string]
    new_list = []
    for i in string_combinations(string[1:]):
        for j in range(len(string)):
            new_list.append(i[:j] + string[0:1] + i[j:])
    return new_list


s = input('Enter string: ')
print(*string_combinations(s))
