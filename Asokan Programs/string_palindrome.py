
def str_palin(n):
    n = str(n).lower()
    mid_val = len(n)//2
    return n[:mid_val] ==n[mid_val:][::-1] if len(n) % 2 == 0 else n[:mid_val] == n[mid_val+1:][::-1]

print(str_palin('Malayalam'))
print(str_palin('ACCA'))
print(str_palin('Gautham'))
print(str_palin(1234321))
print(str_palin(123321))