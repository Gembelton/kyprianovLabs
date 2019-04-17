# в котором Фамилия и имя
from ctypes import c_wchar, pointer


# класс Node для определения элемента списка
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    # инициализация списка
    def __init__(self):
        self.first = None
        self.last = None
        self.adress = 0
        self.charPointer = 0
        self.length = 0

    # распечатать список
    def __str__(self):
        if self.first != None:
            current = self.first
            self.adress = c_wchar(current.value)
            self.charPointer = pointer(self.adress)
            out = 'Односвязный список [ \n' + str(current.value) + " " + str(self.charPointer) + '\n'
            while current.next != None:
                current = current.next
                self.adress = c_wchar(current.value)
                self.charPointer = pointer(self.adress)
                out += str(current.value) + " " + str(self.charPointer) + '\n'
            return out + ']'
        return 'Односвязный список []'

    # добавить элемент в конец
    def add(self, x):
        self.length += 1
        if self.first == None:
            # self.first и self.last будут указывать на одну область памяти
            self.last = self.first = Node(x, None)
        else:
            # здесь, уже на разные, т.к. произошло присваивание
            self.last.next = self.last = Node(x, None)


if __name__ == '__main__':
    L = LinkedList()
    for i in (input("Введите Фио:\n")):
        L.add(i)
    print(L)
