def delete_double_elements(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list


list_of_values = [int(input()) for _ in range(
    int(input('How many elements are in the array? ')))]
print(delete_double_elements(list_of_values))
