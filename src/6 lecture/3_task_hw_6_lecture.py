def permutations(strings, array, fixed_value=""):
    for i in strings:
        permutations(strings.replace(i, ""), array, fixed_value + i)
    if not strings:
        array.append(fixed_value)
    return array


string = input()
list = []
print(*permutations(string, list))
