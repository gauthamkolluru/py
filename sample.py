import email, sys

# print(dir(email))
for i  in sys.argv:
    print(i,type(i))

for i in help(email):
    print(i)

