def angryProfessor(k, a):
    print(len([i for i in a if i>=0]))
    return 'NO' if len([i for i in a if i>=0]) >= k else 'YES'

a = '26 94 -95 34 67 -97 17 52 1 86'
a = [int(i) for i in a.split()]
print(angryProfessor(7,a))