def listMultiplication(n):
    listProduct = 1
    for i in n:
        listProduct *= int(i)
    return listProduct

def largestProductSeries(n,k):
    maxProduct = 0
    for i in range(len(n)-k+1):
        product = listMultiplication(n[i:i+k])
        if product > maxProduct:
            maxProduct = product
    return maxProduct

print(largestProductSeries('89723465987263786455987273658793655873265876489656873466879365872675897368755236487568734265874365876587368756487622873568734657863498768756234383746587346',65))