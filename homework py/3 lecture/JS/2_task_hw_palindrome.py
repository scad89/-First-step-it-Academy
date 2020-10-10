def palindrome(a):
    b = a[::-1]
    k = int(len(a)/2)
    print("YES" if a[0:k] == b[0:k] else "NO")


a = input()
palindrome(a)
