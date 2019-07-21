num_list = range(11)
# print(num_list)
# for x in num_list:
#     print(x)
# num_list_sqrs = [x*x for x in num_list if x*x < 50]
#
# print(num_list_sqrs)

num_list_sqrs_gen = (x**2 for x in num_list)

print(num_list_sqrs_gen)

for nums in num_list_sqrs_gen:
    print(nums)

num_list_sqrs_gen = (x**2 for x in num_list)

print(num_list_sqrs_gen)

for nums in num_list_sqrs_gen:
    print(nums,'gau')
#
# num_list_sqrs_set = {x*x for x in num_list}
#
# print(num_list_sqrs_set)
#
# num_list_sqrs_dict = {x:x*x for x in num_list_sqrs_set}
#
# # print(num_list_sqrs_dict)
#
# anum = int(input(f'enter a number from {num_list_sqrs_set} to find its sqare'))
# print(num_list_sqrs_dict[anum])
#
# num_list_nested = [[1,2,3],[4,5,6],[7,8,9]]
# num_list_nested_com = [[y**2 for y in x] for x in num_list_nested]
#
# print(num_list_nested_com)
#
# # print(num_list_sqrs_dict)