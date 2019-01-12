def primeNumbersWithin(m,n):
    primeNum = []
    for i in range(m,n+1):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            primeNum.append(i)
    return primeNum

n = 2264

if n < 1230 :
    print(primeNumbersWithin(1,10000)[n])
elif 1230 <= n < 2263 :
    print(primeNumbersWithin(10001,20000)[n-1230])
elif 2263 <= n < 3246 :
    print(primeNumbersWithin(20001, 30000)[n - 2263])
elif 3246 <= n < 4203 :
    print(primeNumbersWithin(30001, 40000)[n - 3246])
elif 4203 <= n < 5133 :
    print(primeNumbersWithin(40001, 50000)[n - 4203])
elif 5133 <= n < 6057:
    print(primeNumbersWithin(50001, 60000)[n - 5133])
elif 6057 <= n < 6935:
    print(primeNumbersWithin(60001, 70000)[n - 6057])
elif 6935 <= n < 7837:
    print(primeNumbersWithin(70001, 80000)[n - 6935])
elif 7837 <= n < 8713:
    print(primeNumbersWithin(80001, 90000)[n - 7937])
elif 8713 <= n < 9592:
    print(primeNumbersWithin(90001, 100000)[n - 8173])
elif 9592 <= n:
    print(primeNumbersWithin(90001, 100000)[n - 9592])