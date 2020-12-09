def delete_double_elements(list):
    new_set = set()
    for i in list:
        new_set.add(i)
    return new_set


list_of_values = [int(input()) for _ in range(
    int(input('How many elements are in the array? ')))]
print(delete_double_elements(list_of_values))
