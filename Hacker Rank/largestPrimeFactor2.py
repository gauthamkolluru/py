import math

def primeFactors(n):
    minPrime = [1,2,3,5,7,11,13,17,23]
    if n in minPrime:
        return n
    loop = True
    i = 1
    m = n
    while loop:
        q,r = divmod(m,minPrime[i])
        if r == 0 and q != 1:
            for j in range(2, q):
                if (q % j) == 0:
                    break
            else:
                return q
            m = q
        else:
            i += 1
        if i >= len(minPrime):
            loop = False


    return m,n//m



# print(primeFactors(2347572983729388757))

print(primeFactors(999984))