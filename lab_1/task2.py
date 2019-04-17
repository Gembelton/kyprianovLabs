
# Последний положительный
def lastPlusElement(a):
    plusElement = 0  # 1
    for i in range(len(a)):  # 1+n+n = 1+2n
        if a[len(a)-i-1] > 0:  # 1 или n
            plusElement = a[len(a)-i-1]  # 1 или 0
            break #1 или 0
        elif plusElement <= 0: # n или 0
            plusElement = False #0 или n
    return plusElement #1


# Сумма элементов до последнего (+) элемента
def sumElements(a, plusEl):
    stop = 0  # 1
    sumEl = 0  # 1
    for i in range(len(a)):  # 1 + n+ n = 1 +2n
        if plusEl == a[i]:  # n
            stop = i  # 0 или n
    for i in range(stop):  # 1 +n + n = 1+ 2n
        sumEl += a[i]  # n
    print(sumEl)  # 1
    return sumEl #1

