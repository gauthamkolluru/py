def getSumOfMultiples(n,m):
    while True:
        if n % m == 0:
            return m*((n//m)*((n//m)+1))//2
        else:
            n -= 1

x = getSumOfMultiples(999,3)
y = getSumOfMultiples(999,5)
z = getSumOfMultiples(999,15)
print(x+y-z)