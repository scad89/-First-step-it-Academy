def fibonacci_sequence(n):
    a, b = 1, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    return


n = int(input())
fibonacci_sequence(n)
