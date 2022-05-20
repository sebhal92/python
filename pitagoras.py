# -*- coding: utf-8 -*-
a=float(input("podaj bok a: "))
b=float(input("podaj bok b: "))
c=float(input("podaj bok c: "))

print(a,b,c)

if c<a:
    d=c
    c=a
    a=d
if c<b:
    d=c
    c=b
    b=d
if b<a:
    d=b
    a=b
    b=d
print(a,b,c)

trójkąt=False

if a+b>c:
    print("da się zrobić trójkąt")
    trojkat=True
else:
    print("nie da się zrobić trójkąta")

if a**2+b**2==c**2 and trojkat:
    print("trójkąt jest pitagorejski")
    if a/3==b/4==c/5:
        print("trójkąt jest egipski")
else:
    print("trójkąt zwykły a nie pitagorejski")
            
         