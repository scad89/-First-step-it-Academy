def delete_double_elements_in_list(list):
    list = dict([(item, None) for item in list]).keys()
    return list


list_of_values = [int(input()) for _ in range(
    int(input('How many elements are in the array? ')))]
print(*(delete_double_elements_in_list(list_of_values)))
