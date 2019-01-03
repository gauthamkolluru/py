def func_true(*args):
    countTrue = 0
    args = list(args)
    while args:
        if args[-1]:
            countTrue += 1
        args.pop()
    return True if countTrue == 2 else False


print(func_true(True,False,False))

print(func_true(True,False,True))

print(func_true(True,True,True))

