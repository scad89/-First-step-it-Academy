def output_all_numbers(n: int, count: int) -> int:
    count += 1
    if n < count:
        return 0
    else:
        print(count, end=' ')
    return output_all_numbers(n, count)


n = int(input())
count = 0
output_all_numbers(n, count)
