n = int(input())
d = {}
nl = []
for i  in range(n):
    a,b = input().split()
    d.update({a:b})
for i in range(len(d)):
    nl.append(input())

for i in nl:
    if i in d.keys():
        print('{} = {}'.format(i,d[i]))
    else:
        print('Not Found')

