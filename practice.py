def isPrime(n):
    if n in [2,3,5,7]:
        return True
    if n % 2 == 0:
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True

def isPrime1(n: int) -> bool:
    if n in [2,3,5,7]:
        return True
    if n % 2 == 0:
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True

# print(isPrime(100))
# print(isPrime1(101))


def some_name(n):
    r = 0
    while r * r < n:
        return 


def some_name2(n): #armstrong number
    s = 0
    p = len(str(n))
    for ch in str(n):
        s += int(ch)**p
    return s == n


# Higher Order Functions:


def divBad(n,a):
    return n//a,n%a

def square(n):
    return n * n

def cube(n):
    return n * n * n

def triangular(n):
    return (n * (n + 1))//2

def power2(n):
    return 2 ** n

def inv(f,n):
    r = 0
    while f(r) < n:
        r += 1
    return f(r) == n

es = list(range(1,10))

def isPerfSquare(n):
    return inv(square,n)

for i in es:
    if isPerfSquare(i):
        print(i)

def fb(n):
    list_a =[]
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 != 0:
            list_a.append('Fizz')
        elif i % 5 == 0 and i % 3 != 0:
            list_a.append('Buzz')
        elif i % 15 == 0:
            list_a.append('FizzBuzz')
        else:
            list_a.append(i)
    return list_a

#print(fb(50))



#Python Way of solving the  FizzBzz:

def pick(n):
    return int(n % 3 == 0) + 2 * int(n % 5 == 0)
def fb(n):
    return [str(n), "FIZZ", "BUZZ", "FIZZBUZZ"][pick(n)]
def fizzbuzz(N):
    return [fb(n) for n in range(1, N+1)]

# print(fizzbuzz(50))

# Even more interesting way:

def fb2(n):
    return int(n % 3 == 0) * "FIZZ" + int(n % 5 == 0) * "BUZZ" or str(n)

for i in range(50+1):
    print(fb2(i))
