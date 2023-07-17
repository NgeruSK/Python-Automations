while True:
    print('Type a preferred password. At least 8 characters')
    pass_len = len(input())
    if pass_len > 8:
        break
    else:
        print('Make it longer')
print('Great, At least you follow instructions')