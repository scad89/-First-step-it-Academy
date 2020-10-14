def reverse_number(n: int, last_digit: int) -> int:
    last_digit = n % 10
    if n == 0:
        return 0
    else:
        print(last_digit, end='')
        n = n//10
    return reverse_number(n, last_digit)


n = int(input())
last_digit = 0

reverse_number(n, last_digit)
