try:
    ege = input('how old are you?>>>  ')
    ege = int(ege)
    if ege >= 18:
        print('Access alloved')
    else:
        print('Access denied')

except ValueError:
    print('please of number>>>  ')
