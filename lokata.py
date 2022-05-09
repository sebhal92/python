# -*- coding: utf-8 -*-
stan_start=float(input('podaj stan konta: '))
stopa=float(input('podaj stope oprocentowania '))
lata=int(input('podaj liczbe lat na lokacie: '))
stan_end=stan_start*(1+stopa*lata)
print("Po {} latach bedziesz mial {:5.5f} zlotych".format(lata, stan_end))