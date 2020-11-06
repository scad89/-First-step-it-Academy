from collections import OrderedDict

list_of_values = [int(input()) for _ in range(
    int(input('How many elements are in the array? ')))]
print(list(OrderedDict.fromkeys(list_of_values)))
