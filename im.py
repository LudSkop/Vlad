

while True:

    try:
        age = input('how old are you?>>>  ')
        age = int(age)
        if age >= 18:
            print('Access alloved')
            break
        else:
            print('Access denied')
            break

    except ValueError:
        print('please of number>>>  ')
