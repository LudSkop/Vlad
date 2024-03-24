# чи являється 3-х значне число поліндромом.
namber = int(input('integen:  '))
nam_1 = namber // 100
nam_2 = namber % 10

if nam_1 == nam_2:
    print('yes')
else:
    print('now')