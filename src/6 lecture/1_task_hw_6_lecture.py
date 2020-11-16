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


def split_list(list):
    if len(list) == 1:
        return list

    d = len(list) // 2
    left = split_list(list[:d])
    right = split_list(list[d:])

    return merge(left, right)


def merge(left, right):
    i, j, new_list = 0, 0, []
    while True:
        if left[i] < right[j]:
            new_list.append(left[i])
            i += 1
            if i == len(left):
                new_list.extend(right[j:])
                break

        else:
            new_list.append(right[j])
            j += 1
            if j == len(right):
                new_list.extend(left[i:])
                break

    return new_list


list_of_values = [int(input()) for _ in range(
    int(input('How many elements are in the array? ')))]
print(f'Bubble sort: {bubble_sort(list_of_values)}')
print(f'Merge sort: {split_list(list_of_values)}')
