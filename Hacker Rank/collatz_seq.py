value = 7

def eve(n):
    return n//2

def od(n):
    return (3 * n)+1

aList = []
while value != 1:
    aList.append(value)
    if value % 2 == 0:
        value = eve(value)
    else:
        value = od(value)

aList.append(1)

while len(aList) < 3:
    aList.extend([4,2,1])

print(aList)