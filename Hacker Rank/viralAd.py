def dayLikes(n):
    if n == 1:
        return 2
    else:
        return (3 * dayLikes(n-1)) // 2
def viralAdvertising(n):
    return sum(map(dayLikes,range(1,n+1)))

print(viralAdvertising(5))