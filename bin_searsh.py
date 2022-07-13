from random import randint

lst = [randint(1,75) for i in range(12)] # заполняем список 12-ю рандомными числами от 1 до 75
lst.sort() # сортируем список
print('Числа, которые находятся в списке через запятую:',end = ' ')
for element in lst:
    print(element, end = ', ')
digit = int(input('Введите число, индекс которого вы хотите узнать: '))
mid = len(lst) // 2
low = 0 
high = len(lst) - 1
while lst[mid] != digit and low <= high:
    if digit > lst[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("Такого числа в списке нет.")
else:
    print("Индекс искомого числа в списке:", mid)
