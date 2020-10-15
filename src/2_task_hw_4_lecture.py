def reverse_number(n: int) -> int:
    if n == 0:
        return 0
    else:
        print(n % 10, end='')
    return reverse_number(n//10)


n = int(input())
reverse_number(n)
