

while True:

    try:
        ege = input('how old are you?>>>  ')
        ege = int(ege)
        if ege >= 18:
            print('Access alloved')
            break
        else:
            print('Access denied')
            break

    except ValueError:
        print('please of number>>>  ')
