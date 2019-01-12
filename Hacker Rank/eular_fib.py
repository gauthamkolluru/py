n = 100
a, b = 0, 1
fib_list = []
while a <= n:
    fib_list.append(a)
    a, b = b, a+b
print(sum([i for i in fib_list if i % 2 ==0]))