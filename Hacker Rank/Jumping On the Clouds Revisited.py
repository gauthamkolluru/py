def jumpingOnClouds(c, k, e = 100):
    check = True
    i = 0
    while check:
        prev = i
        i = (i + k) % len(c)
        if c[i] == 0:
            e -= 1
        else:
            e -= 3
        check = False if i <= prev else True
    return e

print(jumpingOnClouds([1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,1,1,1],19))