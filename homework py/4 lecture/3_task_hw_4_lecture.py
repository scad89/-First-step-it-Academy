def moving_the_chips(n: int) -> int:
    result = [1]
    if n > 1:
        for i in range(2, (n-1)*2+1):
            if i % 2 == 0:
                result.append(i//2 + 1)
            else:
                result.append(-1*(i-1)//2)
        if n-2 > 1:
            return result + moving_the_chips(n-2)
        elif n-2 == 1:
            return result + [1]

    return result


n = int(input())
print(*moving_the_chips(n))
