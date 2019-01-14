input_arr = list(range(-10,10))
target_sum = 5
checked_num = []
result_arr = []

for i in input_arr:
    if target_sum-i in input_arr and target_sum-i != i and i not in checked_num:
        checked_num.extend((i,target_sum-i))
        result_arr.append((i,target_sum-i))

print(result_arr)