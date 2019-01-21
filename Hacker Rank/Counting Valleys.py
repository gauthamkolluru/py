def countingValleys(n, s):
    valley_count = 0
    mountain_count = 0
    down_count = 0
    up_count = 0
    for i in range(n):
        if down_count == up_count and down_count != 0 and up_count != 0:
            down_count = 0
            up_count = 0
            if s[i] == 'D':
                down_count += 1
                valley_count += 1
            elif s[i] == 'U':
                up_count += 1
                mountain_count += 1
        elif down_count == 0 and up_count == 0:
            if s[i] == 'D':
                down_count += 1
                valley_count += 1
            elif s[i] == 'U':
                up_count += 1
                mountain_count += 1
        elif down_count != up_count:
            if s[i] == 'D':
                down_count += 1
            elif s[i] == 'U':
                up_count += 1
        # print('Value of i = ', i)
        # print('Valley Count = ', valley_count)
        # print('Down Count = ', down_count)
        # print('Up Count = ', up_count)
        # print('Mountain Count = ', mountain_count)
    return valley_count

print(countingValleys(4,'DUDU'))
