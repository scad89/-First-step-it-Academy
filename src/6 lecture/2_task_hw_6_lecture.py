def delete_double_elements_in_list(list):
    return set(list)


list_of_values = [int(input()) for _ in range(
    int(input('How many elements are in the array? ')))]
print(delete_double_elements_in_list(list_of_values))
