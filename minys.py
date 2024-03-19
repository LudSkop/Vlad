from pprint import pprint 


from colorama import Fore 
from tabulate import tabulate


    
age = 'Oleg 190, vlad 12000, liudmyla 35000, Alissa 12, Pusha 89, we 60000'
inaf = age.strip().split(',')
dict_1 = {}
for anabely in inaf:
    grant = anabely.strip().split(" ")
    dict_1[grant[0]] = grant[1]




table_data = []
for name, salary in dict_1.items():
    name_and_selary = []
    name_and_selary.append(name)
    name_and_selary.append(salary)
    table_data.append(name_and_selary)



print(Fore.LIGHTBLUE_EX + tabulate(table_data, headers=['name','value'], tablefmt='grid'))
with open('Liuda.json', 'w') as file:
    file.write(dict_1)

    
    











