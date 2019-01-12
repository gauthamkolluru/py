# take a num of 4 digits
# gen the smallest num from those 4 digits
# gen the largest num from those 4 digits
# do largest - smallest
# goto line 2 above and continue until at least the last 2 outcomes are same

def largest(num):
    return int(''.join(sorted(str(num),reverse=True)))

def smallest(num):
    return int(''.join(sorted(str(num))))

def nextNum(num):
    return largest(num)-smallest(num)

def kaprekarSeq(num):
    prev = 0
    while prev != nextNum(num):
        yield num
        prev = num
        num = nextNum(num)
    else:
        yield num

for i in kaprekarSeq(6238):
    print(i)