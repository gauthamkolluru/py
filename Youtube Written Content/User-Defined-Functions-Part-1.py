def hello(name, qual = 'Bachelors'):
    return 'Hello ' + name + ' ' + qual

name = 'Gautham'

print(hello(name, qual = 'Masters'))


















# def hello(*args, **kwargs):
#     str_val = ''
#     if args:
#         str_val += ' '.join(args)
#     if kwargs:
#         str_val += ' '. join(kwargs.values())
#     return str_val

# print(hello('Python'))