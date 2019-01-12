import itertools

s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]


def formingMagicSquare(s):
    num_list = [1,2,3,4,5,6,7,8,9]
    sx = itertools.permutations(num_list,3)
    sx = [list(i) for i in sx if sum(i) == 15]


formingMagicSquare(s)