# -*- coding: utf-8 -*-
wzrost=float(input('jaki masz wzrost? '))
waga=float(input('ile wazysz? '))
bmi=(waga/(wzrost**2))
print('twoje bmi wynosi:',bmi)
if bmi<18.5:
    print("masz niedowagę")
elif bmi>=18.5<24:
    print("masz normalną wagę")
elif bmi>=24<26.5:
    print("masz lekką nadwagę")
elif bmi>=26.5<30:
    print("masz nadwagę")
elif bmi>=30<35:
    print("masz otyłość 1 stopnia")
elif bmi>=35<40:
    print("masz otyłość 2 stopnia")
else:
    print("masz otyłość 3 stopnia")