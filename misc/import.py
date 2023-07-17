import random
i = 0
num = random.randint(1,50)
while True:
    print('Guess the number')
    i += 1
    if (int(input()) != num) & (i<=4):
        continue
    if i>4:
        print('code is '+str(num))
        print('Bye Bye')
        break
    else:
        break
print('Good stuff')