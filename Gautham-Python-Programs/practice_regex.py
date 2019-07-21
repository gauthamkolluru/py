# l = [1,2,4,5,6]

# # complete the list

# if l[-1] != len(l):


# d = {'a':1, 'b':1, 'c':1, 'd':2, 'e':10}

# def chan_dict(a):
#     a = [(i,j) for i,j in a.items()]
#     for i in a:
#         for j in a[a.index(i)+1:]:
#             if i[1] == j[1]:
#                 a.remove(j)
#     return {i[0]:i[1] for i in a}

# l = [1,2,3,4,2,2,3,4,3,5]

# l1 = set(l)

# ml = []

# for i in l1:
#     if l.count(i) > 1:
#         ml.append(i)

# print([i for i in l1 if l.count(i) > 1])

# class A:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

# class B(A):
#     def __init__(self,a,b,c):
#         A(a,b)
#         self.c = c

# b1 = B(10,20,30)

# print(b1.a, b1.b, b1.c)


s = "aksdjhbbfkjasdhhffjosdf fasdjfhasldkfh sdijfh saddiljfh asdljhf hsjad bfjasdjfhb 127.0.0.1 akjjhbfbgkjansf fsd 423985"

s1 = "sai gautham kolluru"

import re

ip = re.findall('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', s)

name = re.findall('[g]\w{6}', s1)

print(ip)
print(name)