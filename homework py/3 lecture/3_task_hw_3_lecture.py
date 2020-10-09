def guessed_or_not(secret, guess):
    count = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            count += 1
    print(f'{count}A{len(secret)-count}B')


secret, guess = input(), input()

guessed_or_not(secret, guess)
