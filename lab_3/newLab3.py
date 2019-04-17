from ctypes import *
#pointer = взять по адресу


for i in ("dakota"):
    a = c_wchar(i)
    print(a.value)
    b = pointer(a)
    print(b,"adress")

