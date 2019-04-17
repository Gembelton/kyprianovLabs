# Максимальный элемент
def maxElement(a):
    firstElement = a[0]  # 1
    for i in range(len(a)):  # 1+n+n = 1+2n
        if a[i] > firstElement:  # n
            firstElement = a[i]  # 0 или n
    print("Максимальный элемент ", firstElement)
