def prime(n):
    c = 0
    for i in range(1, n+1):
        if n % i == 0:
            c += 1
    if c == 2:
        return True


# a = 600851475143

a = 13195

li = []

for i in range(1, a+1):
    if a % i == 0:
        if prime(i):
            li.append(i)

print(max(li))