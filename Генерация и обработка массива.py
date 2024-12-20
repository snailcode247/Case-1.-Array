import random

def array_gen(): #создаём функцию генерации массива
    A = random.randint(5,15) #от 5 до 15 элементов
    #return [random.randint(-100,100) for _ in range(A)] #с диапазоном элементов от -100 до 100
    return random.sample(range(-100,101),A) #генерация чисел от -100 до 100 без повторений

def sum_negatives(arr): #основная функция ищущая максимальный и минимальный элементы
                        #и складывающая отрицательные числа между ними
    check = 0
    if not arr:
        print("Массив пуст.")
        return 0 #возврат нуля, если массив пуст

    min_val = min(arr)  # максимальный и минимальный элементы в виде отдельных переменных
    max_val = max(arr)
    min_index = arr.index(min_val) #индексы максимального и минимального элементов
    max_index = arr.index(max_val)
    print(f"Минимальный элемент: {min_val} c индексом {min_index} \nМаксимальный элемент: {max_val} с индексом {max_index}")
                        #выводим мин и макс элементы с их индексами


    starti = min(max_index, min_index) +1 #начало диапазона, выбирается следующий элемент после меньшего индекса
    endi = max(max_index, min_index) #конец диапазона, выбирается больший из двух индексов
    subarray = arr[starti:endi] #создаём массив элементов между меньшим и большим

    if not subarray:
        print("Между максимальным и минимальным нет других элементов")
        return 0,0,0,0
    print(f"Массив между минимальным и максимальным элементами: \n {subarray}")
    negative_sum = sum(x for x in subarray if x<0)  #суммируем отрицательные элементы
    if negative_sum == 0:
        check = 1
    return negative_sum, max_index, min_index, check

while True:

    flag = 0
    b = array_gen()
    print(f"Сгенерированный случайный массив (всего элементов:", len(b), "):", b)
    input(f"\nНажмите продолжить, чтобы продолжить...\n")
    nsum, max_index, min_index, check = sum_negatives(b)

    if check !=0:
        print(f"Между минимальным и максимальным нет отрицательных элементов, попробуем снова\n")
    elif nsum == 0:
        print(f"Пробуем снова\n")
    elif max_index > min_index:
        print(f"Сумма отрицательных элементов массива между минимальным и максимальным элементами: {nsum}")
        flag = 1
    else:
        print(f"Сумма отрицательных элементов массива между максимальным и минимальным элементми: {nsum}")
        flag = 1

    if flag == 1:
        break

input("\nЕщё раз нажмите продолжить, чтобы продолжить...\n")

