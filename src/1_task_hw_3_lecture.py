def prime_numbers(list):
    double_list = []
    for i in list[:: 2]:
        if i % 3 != 0 and i % 5 != 0:
            double_list.append(i)
    double_list.insert(1, 2)
    print(double_list)


list = [i for i in range(1, 100000)]

prime_numbers(list)
