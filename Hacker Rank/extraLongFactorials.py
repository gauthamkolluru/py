def extraLongFactorials(n):
    if n == 0:
        return 1
    else:
        return n * extraLongFactorials(n-1)

print(extraLongFactorials(25))