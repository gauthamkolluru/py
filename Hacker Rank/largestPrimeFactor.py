n = 1000000000
# maxVal = n
primeFactors = []
for i in range(n,0,-1):
    print(i)
    k = []
    # for j in range(1,i+1):
    #     if i % j == 0 and n % i == 0:
    #         if j != 1 and j != i:
    #             k.append(j)
    #         if len(k) > 0:
    #             print(k)
    #             break
    j = 2
    while j < i+1:
        if i % j == 0 and n % i == 0:
            if j != i:
                k.append(j)
            if len(k) > 0:
                print(k)
                break
        j += 1
    if len(k) == 0:
        primeFactors.append(i)
    if len(primeFactors) == 1:
        print(primeFactors[-1])
        break

print(max(primeFactors))

