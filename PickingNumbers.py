import itertools

def pickingNumbers(a):
    return {i for i in itertools.combinations(a,2) if abs(i[0] - i[1]) <= 1}

arr = [1,2,2,3,1,2]

print(pickingNumbers(arr))
