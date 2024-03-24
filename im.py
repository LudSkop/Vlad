try:
    nume = int(input('Enter a namber>>>  '))
    is_even = True if nume % 2 == 0 else False
    print(is_even)
except ValueError:
    print('Invalid input>>>   ')




