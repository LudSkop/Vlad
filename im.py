#перевірити чи в 3-х значному всі числа різні. І чи є тільки 2 однакових числа.
 
result = input('Enter 3 digit namber:  ')
if len(result) != 3:
    print('Please provide a valid integen:  ')
else:
    res_1 = int(result[0])
    res_2 = int(result[1])
    res_3 = int(result[2])

    if res_1 != res_3 and res_2 != res_3 and res_2!= res_1:
        print('Nambers are diffrent ')
    elif (res_1 == res_3 or res_2 == res_3 or res_1 == res_2) and not ( res_1 == res_2 or res_1 == res_3):
        print('2 same  namber')
    
         











