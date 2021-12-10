# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:05:32 2020

@author: Jurgen
"""

from sympy import*;
from math import*;

print("\n\nEjercicio 2.	Dos atletas se disponen a correr los 100 metros planos. Las distancias s1 (t) y s2 (t) que cada uno de ellos recorre a los t segundos esta dada por   s1 (t)=(1/5)t^2+8t y s2 (t)=1100t/(t+100) para t mayor o igual a 0. (a) Escriba un programa en Python que simule el movimiento de los dos corredores. (b)Determine cual de los dos corredores es el rapido en la salida. (c) El que gana la carrera. (c) El mas rapido en cruzar la meta.");

t = Symbol('t');

s1=((1/5)*t**2)+(8*t);
s2=(1100*t)/(t+100);

v1=diff(s1,t);
v2=diff(s2,t);

 
print("\nAmbos corredores tienen una velocidad de 0 al momento de estar en la Salida por ende ambos son iguales de rapidos.");

if v1.subs(t,1)<v2.subs(t,1):
    
    print("Al pasar 1 segundo despues de iniciar la Salida el segundo corredor es mas rapido con "+"%.2f"%float(v2.subs(t,1))+" m/s.");
    
elif v1.subs(t,1)>v2.subs(t,1):
    
    print("Al pasar 1 segundo despues de iniciar la Salida el primer corredor es mas rapido con "+"%.2f"%float(v1.subs(t,1))+" m/s.");

else:
    
    print("Al pasar 1 segundo despues de iniciar la Salida ambos tienen la misma rapidez con "+"%.2f"%float(v1.subs(t,1))+"m/s.");

t1=solve(s1-100,t);
t2=solve(s2-100,t);

if t1[1]>t2[0]:
    
    print("\nEl segundo corredor gana la carrera con un tiempo de "+ "%.2f"%float(t2[0])+ " s.");

elif t1[1]<t2[0]:
    
    print("\nEl primer corredor gana la carrera con un tiempo de "+ "%.2f"%float(t1[1])+" s.");
    
else :

    print("\nNinguno gana la carrera, empataron con un tiempo de "+ "%.2f"%float(t1[1])+" s.");


if v1.subs(t,t1[1])<v2.subs(t,t2[0]):
    
    print("\nEl segundo corredor es mas rapido al momento de cruzar la linea de meta con una velocidad de "+ "%.2f"%float(v2.subs(t,t2[0]))+ " m/s.");

elif v1.subs(t,t1[1])>v2.subs(t,t2[0]):
    
    print("\nEl primer corredor es mas rapido al momento de cruzar la linea de meta con una velocidad de "+ "%.2f"%float(v1.subs(t,t1[1]))+ " m/s.");
    
else :

    print("\nAmbos tienen la misma velocidad de "+ "%.2f"%float(v2.subs(t,t2[0]))+" m/s.");

