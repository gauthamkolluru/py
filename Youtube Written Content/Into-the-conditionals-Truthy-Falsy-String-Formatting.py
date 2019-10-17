# A person John Doe goes for a jog every morning only if it is not raining.

# WAP to check if it is raining. If it turns out to be 'yes' then print, 'Hurray! no Jogging today' else print 'Alas! you must go!'

# Case 1: rain = boolean value

# Case 2: rain = boolean value but

# Any values that refers to nothingness is said to be a Falsy value: 0, None, False, ''

# Any Value other that is not a falsy value is a Truthy valu

# Case 3: rain is referenced to Flasy values

# Ternary way of writing if

rain = bool(input('Enter True / False: '))

# print('Hurray! no Jogging today') if rain.lower() == 'Yes'.lower() else print('Alas! you must go for jog')

jog = 'No' if rain  else 'yes'

print("Value of jog = ", jog)