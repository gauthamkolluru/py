num_range = range(1,10001)
amicable_list = []
for i in num_range:
    factor_sum = 0
    factor_sum2 = 0
    for j in range(1, (i//2)+1):
        if i%j == 0:
            factor_sum += j
    for j in range(1,(factor_sum//2)+1):
        if factor_sum % j == 0:
            factor_sum2 += j
    if factor_sum2 == i and factor_sum != i:
        amicable_list.append(i)

print(amicable_list)
print(sum(amicable_list))