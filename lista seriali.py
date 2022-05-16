# -*- coding: utf-8 -*-
lista_seriali=["dexter","twin peaks","house of cards"]
slownik={"dexter":7, "twin peaks":6,"house of cards":8}
print("lista seriali")
print(lista_seriali)
wybor=input("jaki serial chcesz obejrzeć? ")
print("ocena serialu to", slownik[wybor])
taknie=input("czy chcesz dodać kolejny serial? T/N ")
if taknie == "T":
    nowyserial=input("podaj nazwę serialu: ")
    ocenaserialu=input("podaj ocenę serialu: ")
    lista_seriali.append(nowyserial)
    slownik[nowyserial]=[ocenaserialu]
    print("teraz lista wygląda tak: ", lista_seriali)
else:
    print("okej, cześć")
