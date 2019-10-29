def addition(name1, **python):
    add_res = 0
    add_name = name1 + ' '
    if python:
        for i in python:
            add_name += i
            add_res += python[i]
    return add_name, add_res

my_sum = addition('Gautham',v1 = 1, v2 = 2, v3 = 234, v4 = 2345, v5 = 2345, v6 = 2345)

print(my_sum)


# args - not a keyword
# kwargs - not a keyword
# named - var_name = values