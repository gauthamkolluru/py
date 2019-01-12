import itertools

def pickingNumbers(a):
    # b = list(set(a))
    # if len(b) <= 2:
    #     return a
    # for i in range(len(a)):
    #     for j in range(i+1,len(a)):
    #         if abs(a[i]-a[j]) <= 1:
    b = itertools.combinations(a,2)

    # print(list(b))
    return {i[0] for i in b if abs(i[0]-i[1]) <= 1}

a = [4,6,5,3,3,1]

c = [1,2,2,3,1,2]

print(pickingNumbers(a))

print(pickingNumbers(c))