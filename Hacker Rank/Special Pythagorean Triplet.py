def listMultiplication(n):
    listProduct = 1
    for i in n:
        listProduct *= int(i)
    return listProduct

def specialPythagoreanTriplet(n):
    specialTriplet = []
    for a in range(2,n//2):
        b = int(((2*a*n)-(n*n))//(2*(a-n)))
        c = n - (a+b)
        if a*a + b*b == c*c:
            specialTriplet.append((a,b,c))
    return (max(map(listMultiplication,specialTriplet)) if specialTriplet else -1),specialTriplet,list(map(listMultiplication,specialTriplet))

print(specialPythagoreanTriplet(12))