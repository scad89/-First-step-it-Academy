def bubble_sort(list_of_values):
    n = len(list_of_values)

    for i in range(n - 1):
        flag = False
        for j in range(n - i - 1):
            if list_of_values[j] > list_of_values[j + 1]:
                list_of_values[j], list_of_values[j +
                                                  1] = list_of_values[j + 1], list_of_values[j]
                flag = True
        if flag == False:
            break
    return list_of_values


def merge_sort(list):
    n = len(list)
    if n < 2:
        return list

    left = merge_sort(list[:n//2])
    right = merge_sort(list[n//2:n])

    i = j = 0
    new_list = []
    while i < len(left) or j < len(right):
        if not i < len(left):
            new_list.append(right[j])
            j += 1
        elif not j < len(right):
            new_list.append(left[i])
            i += 1
        elif left[i] < right[j]:
            new_list.append(left[i])
            i += 1
        else:
            new_list.append(right[j])
            j += 1
    return new_list


list_of_values = [int(input()) for _ in range(
    int(input('How many elements are in the array? ')))]
print(f'Bubble sort: {bubble_sort(list_of_values)}')
print(f'Merge sort: {merge_sort(list_of_values)}')
