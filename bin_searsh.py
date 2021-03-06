from random import randint

lst = [randint(1,75) for i in range(12)] # заполняем список 12-ю рандомными числами от 1 до 75
lst.sort() # сортируем список
print('Числа, которые находятся в списке через запятую:',end = ' ')
for element in lst:
    print(element, end = ', ')
print()
digit = int(input('Введите число, индекс которого вы хотите узнать: '))
mid = len(lst) // 2 # получаем индекс срединного элемента в списке
low = 0 # индекс первого
high = len(lst) - 1 # индекс последнего. -1, т.к. индексы от 0.
while lst[mid] != digit and low <= high:
    if digit > lst[mid]:
        low = mid + 1 # нижнюю границу смещаем к бывшей середине + 1
    else:
        high = mid - 1 # иначе верхнюю границу смещаем к бывшей середине - 1
    mid = (low + high) // 2 # обновляем значение индекса середины

if low > high: # для этого +1 и -1 при переприсваивании low и high, а т.ж. условие low<=high
    print("Такого числа в списке нет.")
else:
    print("Индекс искомого числа в списке:", mid)
