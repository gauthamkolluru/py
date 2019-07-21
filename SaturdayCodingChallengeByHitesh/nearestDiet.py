def nearestDiet(arr, nm):
    difference_arr = [abs(new_mem - i) for i in arr]
    return arr[difference_arr.index(min(difference_arr))]


arr = [100,50,150,250,20,30,130]

new_mem = 140

print(nearestDiet(arr, new_mem))
