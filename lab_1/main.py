import random #1
from task1 import maxElement #1
from task2 import lastPlusElement,sumElements #2
# Вариант 5
# Вычислить:
# •Максимальный элемент массива.
# •Сумму	элементов массива, расположенных до последнего положительного элемента.
def main():
    arrSize = int(input("Введите размерность одномерного массива: \n")) #2
    arr = [] #1
    for i in range(arrSize): # 1 + n+ n = 1 +2n
        element = random.randint(0, 10) #n + n
        if (random.randint(0, 10) % 2 == 1): #n или 0
            element = element * -1 #0 или n + 1
        arr.append(element) #n

    print("Массив:") #1
    print(arr) #1
    maxElement(arr) #1
    if not lastPlusElement(arr) : #1 или 0
        print("Положительных элементов нет")#1
    else: # 1
        print("Последний положительный элемент ", lastPlusElement(arr)) #2
        sumElements(arr, lastPlusElement(arr)) #1


main()#1
#main
#в лучшем 6+2n+n+n+0+0+n+3+1+1+1 = 12+4n
#в худшем 6+2n+n+n+n+n+1+n+3+1+2+1+1 13+7n
# Первое задание:
# F1(n) = task1 + main = 16 + 11n - в худшем случае
# F2(n) = task1 + main = 15 + 7n - в лучшем случае
# Ответ : O(n)
# Второе задание:
# F1 (n) = task2 + main = 24 + 19n - в худшем случае
# F2 (n) = task2 + main= 22 + 14n - в лучшем случае
# Ответ : O(n)
# Вся программа:
# в худшем 16 +11n +24+19n-13-7n = 27 + 23n
# в лучшем 22 + 14n + 15 + 7n -12+4n = 25 + 17n