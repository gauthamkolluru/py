def collatz(x):
    if x > 0:
        res = [x]
        if x == 1:
            return [1,4,2,1]
        elif x == 2:
            return [2,1,4,2,1]
        elif x == 4:
            return [4,2,1]
        else:
            while x != 4:
                if x % 2 == 0:
                    x = x//2
                    res.append(x)
                else:
                    x = (3*x)+1
                    res.append(x)
            res.extend([2,1])
        return res

c = collatz(1000)

print(c)
