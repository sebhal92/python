# -*- coding: utf-8 -*-
centymetr=float(input('podaj dlugosc w centymetrach '))
kilogram=float(input('podaj wage w kilogramach '))
print("dlugosc = {} centymetrow".format(centymetr))
print("waga = {} kilogramow".format(kilogram))
metr=centymetr/100
cal=centymetr/2.54
funt=kilogram*2.2046
print("dlugosc w calach wynosi {:6.4f}" .format(metr))
print("dlugosc w calach wynosi {:6.4f}" .format(cal))
print("waga w funtach wynosi {:6.4f}" .format(funt))