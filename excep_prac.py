a = 10
b = 5

# try.... except.... finally

try:
    print('file is opened')
    print(a/b)
except ZeroDivisionError as python:
    print('Hey, dividing a number by zero is not possible!', python)
except TypeError:
    print('Hey, dividing a number by char is not possible!')
except Exception as python:
    print('Some Problem!!!',python)
finally:
    print('file is closed')

print('Hey')

# 1. Syntactic 2. Semantic