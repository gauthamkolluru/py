def pageCount(n, p):
    if p == 1:
        return 0
    if p == n:
        return 0
    if n%2 != 0 and p == n-1:
        return 0
    if p <= n//2:
        for i in range(2,n//2+1,2):
            if p == i or p == i+1:
                return i//2
    if p > n//2:
        p = p=n//2
        for i in range(2,n//2+1,2):
            if p == i or p == i+1:
                return i//2
