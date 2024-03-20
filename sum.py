#from colorama import For


#скласти програму яка виводить з клавіатури на єкран 3 значне число 
# і виводить на єкран суму останньої і передостанньої цифр
# і виводить суму першої і останньої цифри
# x = int(input("Введіть  трьохзначне число : "))

# x3 = x % 10
# x2 = x // 10 % 10
# x1 = x // 100 % 10
# print(f'x3 : {x3} x2 : {x2} x1 : {x1}')
# resulte = x3 + x2
# resulte_1 = x1 + x3
# print(f"сума останньої і передостанньої цифри : {resulte} \nсума першої і останньої цифри : {resulte_1}")

payment = 30.6
payment_1 = 58.9
payment_2 = 30
payment_3 = 23.7
payment_4 = 61.85

sume = payment + payment_1 + payment_2 + payment_2 + payment_4
dollar = int(sume)
cent = int((sume - int(sume))* 100 )
#cent = float(sume - dollar)
print(sume)
print(dollar)
print(cent)

  






