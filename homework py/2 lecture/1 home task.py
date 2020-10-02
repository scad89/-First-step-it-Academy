def change(tuples):
    n_list = list(tuples)
    for i in range(len(tuples)):
        if i % 2 == 0:
            n_list[i] = n_list[i]*2
        elif i % 2 != 0:
            n_list[i] = n_list[i]-2
    tuples_ch = tuple(n_list)
    return tuples_ch


tuples = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print(change(tuples))
