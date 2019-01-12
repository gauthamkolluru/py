import itertools

def permutationEquation(p):
    if p:
        q = itertools.permutations(p, len(p))
        return [checkPermut(p,i) for i in q if len(checkPermut(p,i)) != 0]
    else:
        return 0

def checkPermut(p,v):
    n = list(range(1,len(v)+1))
    p.insert(0,0)
    m = [v[i] for i in range(len(v)) if p[p[i]] == n[i]]
    return m



print(permutationEquation([2,3,1]))