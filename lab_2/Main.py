"""Описать структуру с именем AEROFLOT, содержащую следующие поля:
название пункта назначения рейса;
номер рейса;
Написать программу, выполняющую следующие действия:
открытие файла aeroflot.txt и запись 7 строк в файл.
Каждая строка файла содержит запись об одном рейсе. Формат записи:
название пункта назначения (20 поз., название должно начинаться с первой позиции),
номер рейса (5 поз.), тип самолета (6 поз.). Не забудьте проверить, был ли создан файл и его содержимое;
сортировку рейсов в порядке возрастания их номеров. Результат должен быть записан в файл aeroflot1.txt;
вывод на экран пунктов назначения и номеров рейсов, обслуживаемых самолетом, тип которого введен с клавиатуры;
если таких рейсов нет, выдать на дисплей соответствующее сообщение."""
from Aeroflot import *
from Interface import *


def main():
    arrAero = [Aeroflot("Сибирь", "1", "боинг"),
               Aeroflot("Краснояново", "128", "плэйн"),
               Aeroflot("Малайзия", "3", "боинг"),
               Aeroflot("Краснореченск", "9", "ил"),
               Aeroflot("Витовк", "23", "боинг"),
               Aeroflot("Палеченск", "4", "ил"),
               Aeroflot("Ладыговка", "744", "плэйн"), ]

    fileAero = open('timefile.txt', 'w')
    fileAero.write("")

    # запись структур в файл для начального шаблона
    def fileWriter():
        fileAero = open('aeroport.txt', 'w')
        for i in range(len(arrAero)):
            fileAero.write(arrAero[i].namePunkt + ', ' +
                           arrAero[i].raceNumber + ', ' +
                           arrAero[i].aeroType + '\n')

    # начало программы
    def begin():
        while True:
            interface = Interface()
            choose = int(input("Выберите действие: \n"))
            if choose == 1:
                interface.addPlane()
            elif choose == 2:
                interface.deletePlane()
            elif choose == 3:
                interface.fileReader()
            elif choose == 4:
                interface.sortFile()
            elif choose == 5:
                interface.outputInfo()
            elif choose == 0:
                break

    fileWriter()
    begin()
    a = input("")


main()
