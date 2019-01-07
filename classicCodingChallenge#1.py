COOKIE = '0'

def cookieChip(n):
    return [len(x) for x in n.split(COOKIE) if len(x)>0]

print(cookieChip('1101100000011111000100110'))