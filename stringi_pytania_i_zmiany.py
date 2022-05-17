# -*- coding: utf-8 -*-
imie=input("jak masz na imię? ")
nazwisko=input("jak masz na nazwisko? ")
telefon=input("jaki masz numer telefonu? ")
print("czy imie ma same litery?", imie.isalpha())
print("czy nazwisko ma same litery", nazwisko.isalpha())
print("czy telefon ma same liczby", telefon.isdigit())
print(imie, nazwisko, telefon)
imie.capitalize()
nazwisko.capitalize()
telefon=telefon.replace(" ","").replace("-","")
print(imie, nazwisko, telefon)
if imie.endswith("a") == True:
    print("użytkonik jest kobietą")
else:
    print("użytkownik jest mężczyzną")
personal=imie+" "+nazwisko+" "+telefon
print(personal)
len(personal)
litery=len(personal)-personal.count(" ")-9