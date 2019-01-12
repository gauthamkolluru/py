
def str_palin(n):
    n = str(n).lower()
    mid_val = len(n)//2
    if len(n) % 2 == 0:
        return n[:mid_val] ==n[mid_val:][::-1]
    else:
        return n[:mid_val] == n[mid_val+1:][::-1]

print(str_palin('MAlayalam'))
print(str_palin('ACCA'))
print(str_palin('Gautham'))
print(str_palin(1234321))
print(str_palin(123321))