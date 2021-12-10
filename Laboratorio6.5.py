# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 21:38:05 2020

@author: Jurgen
"""

from sympy import*;
from math import*;

try:
    
    t=1;
    
    s1=str(input("Ingrese la primera funcion en base a t:"));
    
    InducirError=eval(s1);
    
    print("\nEl objeto sera representado en la grafica por el color Rojo.");
    
    s2=str(input("Ingrese la segunda funcion en base a t:"));
    
    InducirError=eval(s2);
    
    print("\nEl objeto sera representado en la grafica por el color Azul.");
        
    tiempo=Abs(float(input("Ingrese el tiempo en segundos:")));
    
    while tiempo==0:

        print("\nEl tiempo no puede ser 0.");
        tiempo=Abs(float(input("Ingrese el tiempo en segundos:")));
    
    t = Symbol('t');
    
    Gp=plot((s1,(t,0,tiempo)),(s2,(t,0,tiempo)),show=False,xlabel='Tiempo (s)',ylabel='Distancia (fts)');
    
    #Gp.annotations=[{'s':'La altura maxima del primer objeto es de: '+"%.2f "%float(s1.subs(t,PMat[0]))+' fts\n El segundo objeto tiene un punto minimo en: '+str(s2.subs(t,PMit[0]))+' fts','xy':(2,-50),'size':'10','color':'black','ha':'center', 'va':'center'}];
    
    Gp[0].line_color='r';
    
    Gp.show();
    
except:
    
    print("\nHa ocurrido un error. Cerrando Programa...");
    
else:
    
    bolGrafiv1=False;
    bolGrafiv2=False;
    
    
    print("\nLa posicion del primer objeto esta dada por: " + str(s1));
    

    v1=diff(s1,t);
    v1a=Abs(diff(s1,t));
        
    print("\nLa velocidad del primer objeto esta dada por: " + str(v1));
    print("La rapidez del primer objeto esta dada por: " + str(v1a));
        
    if diff(s1,t)!=0:
        
        bolGrafiv1=True;
        
        if diff(v1,t)!=0:
            
            try:
                
               PCri1=solve(v1,t);
            
            except:
                
               print("Es imposible obtener los puntos criticos del objeto.");
            
            else:
                
                if len(PCri1)>=1:
                    
                    print("Los puntos criticos del primer objeto estan en: " +str(PCri1) + " segundos.");
                
                    bolInicio=True;
                    
                    for i in range(len(PCri1)):
                        
                        bolImaginario=False;
                        
                        try:
                            
                            float(PCri1[i]);
                        
                        except:
                            
                            bolImaginario=True;
                        
                        
                        if bolImaginario==False:
                        
                            if PCri1[i]>=0:
                                
                                t = Symbol('t');
                                
                                a=diff(v1,t);
                                
                                t=PCri1[i];
                                
                                if PCri1[i]!=0:
                                
                                    PuntoMaxMin1=eval(str(a));
                                    
                                    if PuntoMaxMin1<0:
                                        
                                        Posicion=eval(s1);
                                                                   
                                        if bolInicio==True:
                                        
                                            bolInicio=False;
                                            
                                            AlturaMax1=Posicion;
                                            
                                        elif AlturaMax1<Posicion:
                                            
                                            AlturaMax1=Posicion;
                                            
                                else:
                                    
                                    t=1;
                                    
                                    Mde1=eval(str(v1));
                                    
                                    if Mde1<0:
                                    
                                        t=0;    
                                    
                                        Posicion=eval(s1);
                            
                                        if bolInicio==True:
                                            
                                            bolInicio=False;
                                                
                                            AlturaMax1=Posicion;
                                                
                                        elif AlturaMax1<Posicion:
                                                
                                            AlturaMax1=Posicion;
                                
                    
                    try:
                        
                        print("La altura maxima del primer objeto es: " + "%.2f "%(AlturaMax1)+" fts.");
                    
                    except:
                        
                        print("El objeto no tiene una altura maxima a traves del tiempo.");
                    
                    
                    t = Symbol('t');
                    
                else:
                
                    print("El objeto no posee puntos criticos y por ende no tiene altura maxima.");
                
        else:
             
             print("El objeto no posee puntos criticos y por ende no tiene altura maxima.");
    
    else:
    
        print("El objeto no posee puntos criticos y por ende no tiene altura maxima.");
        
        
        
    t = Symbol('t');
        
    print("\nLa posicion del segundo objeto esta dada por: " + str(s2));
    
    v2=diff(s2,t);
    v2a=Abs(diff(s2,t));
        
    print("\nLa velocidad del segundo objeto esta dada por: " +str(v2));
    print("La rapidez del segundo objeto esta dada por: " +str(v2a));
        
    if diff(s2,t)!=0:
        
        bolGrafiv2=True;
        
        if diff(v2,t)!=0:
            
           try:
                
               PCri2=solve(v2,t);
            
           except:
                
               print("Es imposible obtener los puntos criticos del objeto.");
               
           else:
               
               if len(PCri2)>=1:
                    
                    print("Los puntos criticos del primer objeto estan en: " + str(PCri2) + " segundos.");
                
                    bolInicio=True;
                    
                    for i in range(len(PCri2)):
                        
                        bolImaginario=False;
                        
                        try:
                            
                            float(PCri2[i]);
                        
                        except:
                            
                            bolImaginario=True;
                        
                        
                        if bolImaginario==False:
                        
                            if PCri2[i]>=0:
                                
                                t = Symbol('t');
                                
                                a=diff(v2,t);
                                
                                t=PCri2[i];
                                
                                if PCri2[i]!=0:
                                
                                    PuntoMaxMin2=eval(str(a));
                                    
                                    if PuntoMaxMin2<0:
                                        
                                        Posicion=eval(s2);
                                                                   
                                        if bolInicio==True:
                                        
                                            bolInicio=False;
                                            
                                            AlturaMax2=Posicion;
                                            
                                        elif AlturaMax2<Posicion:
                                            
                                            AlturaMax2=Posicion;
                                            
                                else:
                                    
                                    t=1;
                                    
                                    Mde2=eval(str(v2));
                                    
                                    if Mde2<0:
                                    
                                        t=0;    
                                    
                                        Posicion=eval(s2);
                            
                                        if bolInicio==True:
                                            
                                            bolInicio=False;
                                                
                                            AlturaMax2=Posicion;
                                                
                                        elif AlturaMax2<Posicion:
                                                
                                            AlturaMax2=Posicion;
                                
                    
                    try:
                        
                        print("La altura maxima del segundo objeto es: " + "%.2f "%(AlturaMax2)+" fts.");
                    
                    except:
                        
                        print("El objeto no tiene una altura maxima a traves del tiempo.");
                    
                    
                    t = Symbol('t');
                    
               else:
                
                    print("El objeto no posee puntos criticos y por ende no tiene altura maxima.");
                
                
        else:
            
            print("El objeto no posee puntos criticos y por ende no tiene altura maxima.");
    else:
            
        print("El objeto no posee puntos criticos y por ende no tiene altura maxima.");
               
                
    
    t = Symbol('t');
    
    
    if bolGrafiv1==True or bolGrafiv2==True:
        
        
        try:
            
            Mv=solve(v1-v2,t);
                
            j=0;
                
            if len(Mv)>=1:
                
                    for i in range(len(Mv)):
                        
                        bolImaginario=False;
                        
                        try:
                                    
                            float(Mv[i]);
                                
                        except:
                                    
                            bolImaginario=True;
                            
                        if bolImaginario==False:
                            
                            if Mv[i]>=0:
                                
                                j+=1;
                                
            Mvm=[None]*j;
    
            j=0;
            
            if len(Mv)>=1:
                
                    for i in range(len(Mv)):
                        
                        bolImaginario=False;
                        
                        try:
                                    
                            float(Mv[i]);
                                
                        except:
                                    
                            bolImaginario=True;
                            
                        if bolImaginario==False:
                            
                            if Mv[i]>=0:
                                
                                Mvm[j]="%.2f"%float(Mv[i]);
                                j+=1;
                        
        
            
            if(len(Mvm)>=1):
                
                print("\nAmbos objetos tienen la misma velocidad en: " + str(Mvm) + " s.");
            
            else:
                
                print("\nLa velocidad de los dos objetos nunca son iguales, son iguales en un punto fuera del tiempo o siempre son iguales.");
            
            
        except:
            
            print("\nNo es posible encontrar una solucion respecto al tiempo en que la velocidad de los dos objetos son iguales.");
            
       
        try:
        
            Mr1=solve(v1-v2,t);
            Mr2=solve(v1+v2,t);
            
            #print(Mr1);
            #print(Mr2);
            
            j=0;
            
            if len(Mr1)>=1:
            
                for i in range(len(Mr1)):
                    
                    bolImaginario=False;
                    
                    try:
                                
                        float(Mr1[i]);
                            
                    except:
                                
                        bolImaginario=True;
                        
                    if bolImaginario==False:
                        
                        if Mr1[i]>=0:
                            
                            #Mrm[j]=Mr1[i];
                            j+=1;
            
            
            
            if len(Mr2)>=1:
            
                for i in range(len(Mr2)):
                    
                    bolImaginario=False;
                    
                    try:
                                
                        float(Mr2[i]);
                            
                    except:
                                
                        bolImaginario=True;
                        
                    if bolImaginario==False:
                        
                        if Mr2[i]>=0:
                            
                            #Mrm[j]=Mr2[i];
                            j+=1;
                    
            
            Mrm=[None]*j;
            
            j=0;
            
            if len(Mr1)>=1:
            
                for i in range(len(Mr1)):
                    
                    bolImaginario=False;
                    
                    try:
                                
                        float(Mr1[i]);
                            
                    except:
                                
                        bolImaginario=True;
                        
                    if bolImaginario==False:
                        
                        if Mr1[i]>=0:
                            
                            Mrm[j]="%.2f"%float(Mr1[i]);
                            j+=1;
            
            
            
            if len(Mr2)>=1:
            
                for i in range(len(Mr2)):
                    
                    bolImaginario=False;
                    
                    try:
                                
                        float(Mr2[i]);
                            
                    except:
                                
                        bolImaginario=True;
                        
                    if bolImaginario==False:
                        
                        if Mr2[i]>=0:
                            
                            Mrm[j]="%.2f"%float(Mr2[i]);
                            j+=1;
            
            
            if(len(Mrm)>=1):
                
                print("\nAmbos objetos tienen la misma rapidez en: " + str(Mrm)+" s.");
           
            else:
                
                print("\nLa rapidez de los dos objetos nunca son iguales, son iguales en un punto fuera del tiempo o siempre son iguales.");
            
        except:
        
            print("\nNo es posible encontrar una solucion respecto al tiempo en que la rapidez de los dos objetos son iguales.");
       
    
    
             
        Gv=plot((v1,(t,0,tiempo)),(v2,(t,0,tiempo)),show=False,xlabel='Tiempo (s)',ylabel='Velocidad (fts/s)');
                         
        #Gv.annotations=[{'s':'Tienen la misma velocidad en: '+str(float(Mv[0]))+' s','xy':(1.5,-25),'size':'10','color':'black','ha':'center', 'va':'center'}];
                
        Gv[0].line_color='r';
                
        Gv.show();
    
    
    
        Gva=plot((v1a,(t,0,tiempo)),(v2a,(t,0,tiempo)),show=False,xlabel='Tiempo (s)',ylabel='Rapidez (fts/s)');
                
        
        #Gva.annotations=[{'s':'Tienen la misma rapidez en: '+str(float(Mr2[0]))+' s y '+str(float(Mr1[0]))+' s','xy':(1.75,25),'size':'10','color':'black','ha':'center', 'va':'center'}];
                
        Gva[0].line_color='r';
                
        Gva.show();
        
