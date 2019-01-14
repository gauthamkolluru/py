def sequenceEquation(p):
    p = list(p)
    p.insert(0,0)
    result = []
    for i in range(1,len(p)):
        if p.index(p.index(i)):
            result.append(str(p.index(p.index(i))))
    return result

print(sequenceEquation([2,5,11,10,1,14,7,3,16,9,8,6,18,12,15,17,13,4]))