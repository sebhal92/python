# -*- coding: utf-8 -*-
imiona={"adam":"meskie","dawid":"meskie","ewa":"zenskie","zuzanna":"zenskie"}
imie=input("podaj imie: ")
if imie.endswith("a") == True:
    print("użytkownik jest kobietą")
else:
    print("użytkownik jest mężczyzną")
if imie in imiona:
    print("czesc ", imie)
else:
    print("nie znamy tego imienia, dodaj je")
    imieplec=input("czy imie jest męskie? T/N")
    if imieplec=="T":
        imiona[imie] = "meskie"
    else:
        imiona[imie] = "zenskie"
    print(imiona.keys()))