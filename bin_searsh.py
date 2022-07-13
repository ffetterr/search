from random import randint

lst = [randint(1,75) for i in range(12)] # заполняем список 12-ю рандомными числами от 1 до 75
lst.sort() # сортируем список
print('Числа, которые находятся в списке через запятую:',end = ' ')
for element in lst:
    print(element, end = ', ')
