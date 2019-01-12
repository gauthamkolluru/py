import itertools
def biggerIsGreater(w):
    x = sorted(itertools.permutations(w,len(w)))
    print(x[-1])
    return ''.join(x[x.index(tuple(w))+1]) if x[x.index(tuple(w))+1] else 'no answer'


print(biggerIsGreater('abcd'))