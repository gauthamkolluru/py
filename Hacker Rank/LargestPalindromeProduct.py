n = 923576
# sixDigitPal = [i for i in range(n,101100,-1) if str(i)[0:3] == str(i)[3:6][::-1]]
# print(len(sixDigitPal))
# # for i in range(100,1000):
# #     for j in
# maxVal = n
# for i in sixDigitPal:
#     if i < n:
#         maxVal = i
#         break

# print(maxVal)

# reqVal = 0
# for i in getPalindrome(800000):
#     while reqVal == 0:
#         for j in range(100,1000):
#             q,r = divmod(i,j)
#             if r == 0 and len(str(q)) == 3:
#                 print(i)
#                 reqVal = i
#                 break

def getProPalindrome(m):
    for i in range(100,1000):
        q,r = divmod(m,i)
        if r == 0 and len(str(q)) == 3:
            return m
    return


def getPalindrome(n):
    for i in range(n,101100,-1):
        if str(i)[0:3] == str(i)[3:6][::-1]:
            yield getProPalindrome(i)



for i in getPalindrome(800000):
    if i:
        print(i)
        break
