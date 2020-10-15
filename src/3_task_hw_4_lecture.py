def moving_the_chips(start, n):
    if n <= 0:
        return
    if start <= n:
        print(start, end=' ')
        if start > 1 and start != n:
            print(-(start-1), end=' ')
        moving_the_chips(start+1, n)
    else:
        return moving_the_chips(1, n - 2)


n = int(input())
start = 1
moving_the_chips(start, n)
