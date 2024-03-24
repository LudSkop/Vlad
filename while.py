
from  colorama import Fore
import pyttsx3



count = 0
engine = pyttsx3.init()
engine.setProperty('volume', 100)



while True:

    
    user_input = input(Fore.LIGHTMAGENTA_EX +'Як тебе звати?   >>  ' )
    # engine.say('как тебя зовут?')
    # engine.runAndWait()
    user_input = user_input.lower().strip()
    if user_input =='exit' :
        engine.say('Досвидания. всего хорошего. красота  моя!!!!')
        engine.runAndWait()
        break
    
    elif user_input == 'oleg':
        print(Fore.LIGHTRED_EX + f'Вітаю Олеже як себе почуваєш?   ' )
        engine.say('Олежка  добрый день , как ты  думаешь когда война закончится? сил уже нет никаких.   ')
        engine.runAndWait()
    elif user_input == 'vlad':
         print(Fore.LIGHTRED_EX + f'Вітаю, Владе як у тебе справи? як твої учні, достають тебе?  ')
         engine.say('Здравствуй Владислав  как ты думаешь от чего кружится голова  .vlad наверное от пайтона? ')
         engine.runAndWait()
    elif user_input == 'liuda':
        print(Fore.LIGHTRED_EX + f'Вітаю, ти добре вивчаєш пайтон?  ')
        engine.say('Добрый день Людмила как ты себя чувствуешь и как твои успехи в питоне? ты хорошо контролируешь своих пацанов? ')
        engine.runAndWait()
    elif user_input == 'ok':
        print(Fore.BLACK + f' ')
        engine.say('я хочу сказать вам всем уважаемые  мои люди что война закончится скоро и у нас всё будет хорошо. и это будет так. поверьте мне')     
        engine.runAndWait()
    else:
        print(Fore.LIGHTYELLOW_EX + f'Введіть текст : {user_input}')