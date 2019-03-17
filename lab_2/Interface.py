import re, os


class Interface():
    def __init__(self):
        print("------------------------------------------------------------\n"
              "1.Добавить рейс в файл\n"
              "2.Удалить рейс из файла\n"
              "3.Просмотр содержимого файла\n"
              "4.сортировать рейсы в порядке возрастания их номеров.\n"
              "5.Вывести на экран пункты назначения и номера рейсов,\n"
              " Обслуживаемых самолетом, тип которого введен с клавиатуры\n"
              "0.Выход\n"
              "------------------------------------------------------------\n")

    # добавление
    def addPlane(self):
        fileAero = open('aeroport.txt', 'a')
        punkt = input("Введите пункт: ")
        raceNum = input("Введите номер рейса: ")
        plane = input("Введите ваш самолет: ")
        fileAero.write(punkt + ', ' +
                       raceNum + ', ' +
                       plane + '\n')

    # удаление
    def deletePlane(self):
        choose = int(input("1.Удалить все содержимое\n"
                           "2.Удалить конкретный рейс\n"))

        if choose == 2:
            accept = True
            fileTime = open('timefile.txt', 'w')
            fileAero = open('aeroport.txt', 'r')
            numOfDeletedPlane = input("Введите самолет/номер или место посадки: ")

            for text in fileAero.readlines():
                if not re.search(numOfDeletedPlane, text):
                    fileTime.write(text)
                else:
                    print("Рейс: ", text, end="Удален из файла \n")
                    accept = False

            fileTime = open('timefile.txt', 'r')
            if accept:
                if not re.search(numOfDeletedPlane, fileAero.read()):
                    print("Таких рейсов нет")
            fileAero = open('aeroport.txt', 'w')

            for text in fileTime.readlines():
                fileAero.write(text)

        elif choose == 1:
            fileAero = open('aeroport.txt', 'w')
            fileAero.write("")

    # просмотр содержимого файла
    def fileReader(self):
        choose = int(input("Выберите файл: \n"
                           "1.aeroport.txt\n"
                           "2.aeroport2.txt - сортированый по возрастанию первый файл\n"))

        if choose == 1:
            fileAero = open('aeroport.txt', 'r')
            file = 'aeroport.txt'
        elif choose == 2:
            fileAero = open('timefile.txt', 'r')
            file = 'timefile.txt'
        for text in fileAero.readlines():
            print(text, end='')
        if os.stat(file).st_size == 0:
            print("Файл пустой")
        fileAero.close()

    # сортировка , в порядке возрастания номеров
    def sortFile(self):
        arr = []
        fileAero = open('aeroport.txt', 'r')
        fileTime = open('timefile.txt', 'w')
        for text in fileAero.readlines():
            text = text[text.find(',') + 2:]
            text = text[:text.find(',')]
            arr.append(int(text))

        arr = sorted(arr)
        kol = 0
        print(arr)
        #
        fileTime = open('timefile.txt', 'w')
        for kol in range(len(arr)):

            fileAero = open('aeroport.txt', 'r')
            for line in fileAero.readlines():
                if re.match(str(arr[kol]), line[line.find(',') + 2:]):
                    fileTime.write(line)
                    break

    # вывод на экран рейсов,которые совпадают с типом самолета
    def outputInfo(self):
        accept = True
        userPlane = input("Введите тип самолета: \n")
        fileAero = open('aeroport.txt', 'r')
        for line in fileAero.readlines():
            lineDop = line[line.find(',') + 2:]
            if re.search(userPlane, lineDop):
                newLine = line[:line.rfind(',')]
                print(newLine)
                accept = False
        if not re.search(userPlane, fileAero.read()):
            if accept == True:
                print("Таких типов самолетов нет\n")
