def output_all_numbers(n: int, count: int) -> int:
    if n < count:
        return 0
    else:
        print(count, end=' ')
    return output_all_numbers(n, count + 1)


n = int(input())
count = 1
output_all_numbers(n, count)
