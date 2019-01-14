# n -> No. of Prisoners
# m -> No. of Candys
# s -> Staring Chair

def saveThePrisoner(n, m, s):
    if n == m:
        return n if s == 1 else n-1
    elif m < n:
        if s == 1:
            return m
        elif s == n:
            return n-1
        else:
            return m - len(range(s,n+1))
    elif m > n:
        if s == 1:
            return m - n * (m//n)
        else:
            return (m - n * (m // n)) - 1 - (n - s)
    else:
        return 0

print(saveThePrisoner(46934,543563655,46743))