print('Hello, what is your name?')
name = input()
print(name +', what is your year of birth?')
yob = input()
age = 2023 - int(yob)
if age < 0:
    print('Stop the jokes '+name)
elif age < 18:
     print('go home, no entry')
else:
    print('uko sawa')
print('Thank you')