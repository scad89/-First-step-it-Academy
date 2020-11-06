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


def bottom_up_of_list(list):
    k = 1
    while k < len(list):
        for i in range(0, len(list)-k, 2*k):
            list[i:i+2*k] = merge(list[i:i+k], list[i+k:i+2*k])
        k *= 2

    return list


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
print(f'Merge sort: {bottom_up_of_list(list_of_values)}')
