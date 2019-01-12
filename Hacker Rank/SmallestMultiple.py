def primeNumbersWithin(n):
    primeNum = []
    for i in range(1,n+1):
        k = [j for j in range(1, i + 1) if i % j == 0]
        if len(k) == 2:
            primeNum.append(i)
    return primeNum

def smallestMultiple(n):
    numList = primeNumbersWithin(n)
    smallestNum = 1
    for i in numList:
        j = 1
        while i**j <= n:
            j += 1
        else:
            smallestNum *= (i**(j-1))
    return smallestNum

print(smallestMultiple(11))
