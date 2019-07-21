T = int(input())

n = [] #list of Ns

for i in range(T):
    n.append(input())

def check_N(n):
    c = []
    for i in n:
        if '4' in i:
            A = int(i)//2
            B = int(i) - A
            while '4' in str(A) or '4' in str(B):
                A -= 1
                B += 1
            c.append((A,B))
        else:
            c.append(int(i))
    return c

print(check_N(n))

