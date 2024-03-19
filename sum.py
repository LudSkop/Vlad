from colorama import Fore

while True:
    try:
        x = input(Fore.LIGHTRED_EX + 'plese 4 значне  namber : ')
        if x == "5" :
            print(Fore.LIGHTYELLOW_EX + "good bye Alissa")
            break

        result = 0
        awarage = 0
        for asta in x:
            result += int(asta) 
        awarage = result / len(x)
        print(Fore.LIGHTGREEN_EX + str(awarage))
    except ValueError: 
        continue
    except  ZeroDivisionError:
        continue


  






