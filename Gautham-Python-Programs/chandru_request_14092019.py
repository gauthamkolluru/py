# a = []
# list(map(lambda x : list(map(lambda y : a.append(y[0]+y[1]), x)), list(filter(lambda x : x if x else None, list(map(lambda x : list(filter(lambda y : y if y[0] % 2 == 0 and y[-1] % 2 == 1 else None, x)),list(map(lambda i : list(map(lambda j : (i,j), range(5))),list(range(5))))))))))
# print(a)

# list(map(lambda x : list(filter(lambda y : y if y[0] % 2 == 0 and y[-1] % 2 == 1 else None, x)),))

# print(list(map(lambda i : list(map(lambda j : (i,j), ))),list(range(5)))))

# list(filter(lambda x : 'x' if x == 0 or x % 2 == 0 else None, range(5)))

# list(filter(lambda x : 'x' if x % 2 == 1 else None, range(5)))

# print(list(map(lambda x : list(filter(lambda y : y if y[0] % 2 == 0 and y[-1] % 2 == 1 else None, x)),)))

list(map(lambda i : map(lambda j : (i,j), filter(lambda x : x % 2 == 1, range(5))),filter(lambda x : x % 2 == 0, range(5))))

# print(list(filter(lambda x : 'x' if x % 2 == 0 else None, range(5))))

# a = lambda x : 'x' if x % 2 == 0 else None

# seq = [0, 1, 2, 3, 5, 8, 13]
# result = filter(lambda x: x % 2 == 0, seq) 
# print(list(result)) 

# list(filter(lambda x : x % 2 == 0, range(5)))