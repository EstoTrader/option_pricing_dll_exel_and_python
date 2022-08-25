# import dll from python (option pricing dll by @estotrader)
import os
import ctypes
from ctypes import *

#load dll & define return function type
c_lib = ctypes.CDLL(os.path.join(os.path.realpath(    os.path.join(os.getcwd(), os.path.dirname(__file__))), 'Esto.dll'))
c_lib.precio_call.restype = ctypes.c_double
c_lib.precio_put.restype = ctypes.c_double

#wrapper pricing funtions (Black-Scholes Analitical Pricing Formula)
#TODO: add more wrappers for several extra pricing models
def precio_call(a,s,r,v,d,m):
    return c_lib.precio_call(byref (c_double(a)),byref(c_double(s)),byref(c_double(r)),byref(c_double(v)),byref(c_double(d)),byref(c_double(m)))
def precio_put(a,s,r,v,d,m):
    return c_lib.precio_put(byref (c_double(a)),byref(c_double(s)),byref(c_double(r)),byref(c_double(v)),byref(c_double(d)),byref(c_double(m)))

# option arguments
a=100 #underlying price // precio de la acción (subyacente)
s=100 #option strike // strike de la opción
r=2     #risk free // los tipos de interes o el bono
v=20   # volatility // volatilidad
d=45  # days till expiration // dias hasta expiración
m=1   #multiplier for mods // multiplicador normalmente 1 (sirve de ajuste por si los precios reales estan muy desviados)

print('Underlying price:    ' + str(a) )
print('Strike:                   ' + str(s))
print('Volatility:               ' + str(v) )
print('Days till expiration: ' + str(d) + "\n")

print ('Call option price:  ' + str(precio_call(a,s,r,v,d,m)))
print ('Put option price:  ' + str(precio_put(a,s,r,v,d,m)) + "\n")

#price mods
m=0.75 # cheap // barata
print ('Call option price modded (cheap)=' +str(precio_call(a,s,r,v,d,m)))
m=2.5 # expensive // cara
print ('Put option price modded (expensive)=' + str(precio_put(a,s,r,v,d,m)) + "\n")

print("Press enter to exit")
nombre = input()




