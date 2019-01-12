def sumOfSquares(n):
    return  n*(n+1)*(2*n+1)//6

def squareOfSums(n):
    return (n*(n+1)//2)**2


def absoluteDiff(n):
    return abs(squareOfSums(n) - sumOfSquares(n))


print(absoluteDiff(10000000000000000000000000000000000))