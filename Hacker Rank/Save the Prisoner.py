# n -> No. of Prisoners
# m -> No. of Candys
# s -> Staring Chair

def saveThePrisoner(n, m, s):
    if n == m:
        if s == 1:
            return n
        if s > 1:
            return n-1
    if m != n:
        if s == 1:
            return m - n * (m//n)
        else:
            return s + (m - n * (m // n)) - 1

print(saveThePrisoner(352926151,380324688,94730870))