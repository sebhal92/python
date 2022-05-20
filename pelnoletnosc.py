# -*- coding: utf-8 -*-
dorosly=18
age = int(input("Ile masz lat?"))
if  age >= 18 and age > 100:
    print("Użytkownik pełnoletni")
    print("200 lat")
else:
    age=dorosly-age
    print("Użytkownik niepełnoletni, do pełnoletności zostało ",age," lat")