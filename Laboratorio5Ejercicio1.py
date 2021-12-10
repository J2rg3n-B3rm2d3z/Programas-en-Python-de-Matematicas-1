# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:05:32 2020

@author: Jurgen
"""

from sympy import*;
from math import*;

t = Symbol('t');

s1=4*t-3*t**2;
s2=t**2-2*t;

v1=diff(s1,t);
v2=diff(s2,t);

v1a=Abs(diff(s1,t));
v2a=Abs(diff(s2,t));

print("\n\nEjercicio 1. Dos objetos se mueven a lo largo de un eje coordenado. Al final de t segundos su distancia dirigida desde el origen, en pies, están dadas por s1=4t-3t^2 y  s2=t^2-2t, respectivamente.  (a) Escriba un programa en Python que simule el movimiento de los dos objetos. (b) Determine en la gráfica cuando tienen la misma velocidad. (c) Determine en la gráfica cuando tienen la misma rapidez (d) Determine la altura máxima.");

print("Respuestas en los graficos.");

print("s1 es representado a traves del color rojo.");
print("s2 es representado a traves del color azul.");

"""

print(s1);
print(s2);

print(v1);
print(v2);

print(v1a);
print(v2a);

"""


Gp=plot((s1,(t,0,5)),(s2,(t,0,5)),show=False,xlabel='Tiempo (s)',ylabel='Distancia (fts)',label='Funciones');

PMat=solve(v1,t);
PMit=solve(v2,t);

Gp.annotations=[{'s':'La altura maxima del primer objeto es de: '+"%.2f "%float(s1.subs(t,PMat[0]))+' fts\n El segundo objeto tiene un punto minimo en: '+str(s2.subs(t,PMit[0]))+' fts','xy':(2,-50),'size':'10','color':'black','ha':'center', 'va':'center'}];

Gp[0].line_color='r';

Gp.show();




Gv=plot((v1,(t,0,5)),(v2,(t,0,5)),show=False,xlabel='Tiempo (s)',ylabel='Velocidad (fts/s)');

Mv=solve(v1-v2,t);

Gv.annotations=[{'s':'Tienen la misma velocidad en: '+str(float(Mv[0]))+' s','xy':(1.5,-25),'size':'10','color':'black','ha':'center', 'va':'center'}];

Gv[0].line_color='r';

Gv.show();




Gva=plot((v1a,(t,0,5)),(v2a,(t,0,5)),show=False,xlabel='Tiempo (s)',ylabel='Rapidez (fts/s)');

Mr1=solve(v1-v2,t);
Mr2=solve(v1+v2,t);

Gva.annotations=[{'s':'Tienen la misma rapidez en: '+str(float(Mr2[0]))+' s y '+str(float(Mr1[0]))+' s','xy':(1.75,25),'size':'10','color':'black','ha':'center', 'va':'center'}];

Gva[0].line_color='r';

Gva.show();


"""
x = symbols('x')

#Defined the function to be differentiated
f = "exp(x) * sin(2*x)"
#plot1 = f
p1 = f
#plot2 = f'
p2 = diff(f, x)
#P is the plot of f and f'
p = plot(p1, p2, (x, 0, 10), show=false)
#change the color of p2
p[1].line_color = 'r'

p.show()"""