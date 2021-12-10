# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:00:07 2020

@author: Jurgen
"""
from math import*;
from sympy import*;
#from IPython import get_ipython;
import numpy as np;
import matplotlib.pyplot as plt;
import sys, time, os;

x = Symbol('x');


def ApliDeriv():
    
    
    
    print("\n\n\n\n\n\nAPLICACIONES DE DERIVADAS.");
    print("\nIngrese lo que se le pide conforme al tiempo que se desea.\n\n\n");
    
    try:
    
        t=1;
        
        s1=str(input("\nIngrese la primera ecuacion de la posicion del objeto en base al tiempo:\n\ns1(t)= "));
        
        InducirError=eval(s1);
        
        print("\nEl objeto sera representado en la grafica por el color Rojo.");
        
        s2=str(input("Ingrese la segunda ecuacion de la posicion del objeto en base al tiempo:\n\ns2(t)= "));
        
        InducirError=eval(s2);
        
        print("\nEl objeto sera representado en la grafica por el color Azul.");
            
        tiempo=Abs(float(input("Ingrese los segundos que desea visualizar:")));
        
        while tiempo==0:
    
            print("\nEl tiempo no puede ser 0.");
            tiempo=Abs(float(input("Ingrese los segundos que desea visualizar:")));
        
        t = Symbol('t');
        Parsets1='';
        Parsets2='';
        
        try:
            
            s1 = float(s1);
            
        except:
            
            Parsets1 = lambdify(t,parse_expr(s1),'numpy');
        
        
        
        try:
            
            s2 = float(s2);
            
        except:
            
            Parsets2 = lambdify(t,parse_expr(s2),'numpy');
        
        
        
        
        def graphs1(x):
            
            if(type(s1) is float) == True:
                                
                return np.full(x.shape,s1);
            
            else:
                
                return Parsets1(x);
            
            
        
        def graphs2(x):
            
            if(type(s2) is float) == True:
                                
                return np.full(x.shape,s2);
            
            else:
                
                return Parsets2(x);
        
        
        
        Ranget=np.linspace(0,int(tiempo),num=500);

        plt.grid(True);
        plt.axhline(0, color="black");
        plt.axvline(0, color="black");
        plt.plot(Ranget,graphs1(Ranget),'r');
        plt.plot(Ranget,graphs2(Ranget),'b');
        plt.axis('auto');
        plt.ylabel('Distancia (fts)');
        plt.xlabel('Tiempo (s)');
        plt.show();
        
     
        """Gp=plot((s1,(t,0,tiempo)),(s2,(t,0,tiempo)),show=False,xlabel='Tiempo (s)',ylabel='Distancia (fts)');
        
        #Gp.annotations=[{'s':'La altura maxima del primer objeto es de: '+"%.2f "%float(s1.subs(t,PMat[0]))+' fts\n El segundo objeto tiene un punto minimo en: '+str(s2.subs(t,PMit[0]))+' fts','xy':(2,-50),'size':'10','color':'black','ha':'center', 'va':'center'}];
        
        Gp[0].line_color='r';
        
        Gp.show();"""
        
    except:
        
        print("\nHa ocurrido un error. Regresando...");
        time.sleep(2);
        
    else:
        
        t = Symbol('t');
        bolGrafiv1=False;
        bolGrafiv2=False;
        
        
        print("\nLa posicion del primer objeto esta dada por: " + str(s1));
        
    
        v1=diff(s1,t);
        v1a=Abs(diff(s1,t));
            
        print("\nLa velocidad del primer objeto esta dada por: " + str(v1));
        print("La rapidez del primer objeto esta dada por: " + str(v1a));
        
        t=0;
        
        try:
            
            PuntoOs1=float(eval(str(s1)));
            
        except:
            
            PuntoOs1=None;
           
        
        t=int(tiempo);
        
        try:
            
            PuntoFs1=float(eval(str(s1)));

        except:
                
            PuntoFs1=None;
                
            
        if PuntoOs1==None and PuntoFs1==None:
            
            PuntoExtres1=None;
            
        elif PuntoOs1==None and PuntoFs1!=None:
                
            PuntoExtres1=PuntoFs1;
            
        elif PuntoOs1!=None and PuntoFs1==None:
                
            PuntoExtres1=PuntoOs1;
            
        else:
            
            if(PuntoOs1<=PuntoFs1):
                        
                PuntoExtres1=PuntoFs1;
                        
            else:
                        
                PuntoExtres1=PuntoOs1;
            
        
        t = Symbol('t');
        
        if diff(s1,t)!=0:
            
            bolGrafiv1=True;
            
            if diff(v1,t)!=0:
                
                try:
                    
                   PCri1=solve(v1,t);
                
                except:
                    
                   print("Es imposible obtener los puntos estacionarios del objeto.");
                
                else:
                    
                    if len(PCri1)>=1:
                        
                        print("Los puntos estacionarios del primer objeto estan en: " + str(PCri1) + " segundos.");
                    
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
                                            
                                            try:
                                                
                                                Posicion=float(eval(s1));
                                            
                                            except:
                                                
                                                Posicion=None;
                                            
                                            if Posicion!=None:
                                                                       
                                                if bolInicio==True:
                                                
                                                    bolInicio=False;
                                                    
                                                    AlturaMax1=Posicion;
                                                    
                                                elif AlturaMax1<Posicion:
                                                    
                                                    AlturaMax1=Posicion;

        try:
                
            if AlturaMax1<PuntoExtres1:
                
                AlturaMax1=PuntoExtres1;
                
        except:
            
              AlturaMax1=PuntoExtres1;          
            
        try:
                            
            print("La altura maxima del primer objeto es: " + "%.2f "%(AlturaMax1)+" fts.");
                        
        except:
                            
            print("El objeto no tiene una altura maxima a traves del tiempo.");
                        
        
        time.sleep(5);
            
        t = Symbol('t');
            
        print("\nLa posicion del segundo objeto esta dada por: " + str(s2));
        
        v2=diff(s2,t);
        v2a=Abs(diff(s2,t));
            
        print("\nLa velocidad del segundo objeto esta dada por: " + str(v2));
        print("La rapidez del segundo objeto esta dada por: " + str(v2a));
        
        t=0;
        
        try:
            
            PuntoOs2=float(eval(str(s2)));
            
        except:
            
            PuntoOs2=None;
        
        t=int(tiempo);
        
        try:
            
            PuntoFs2=float(eval(str(s2)));
        
        except:
            
            PuntoFs2=None;
        
        if PuntoOs2==None and PuntoFs2==None:
            
            PuntoExtres2=None;
            
        elif PuntoOs2==None and PuntoFs2!=None:
                
            PuntoExtres2=PuntoFs2;
            
        elif PuntoOs2!=None and PuntoFs2==None:
                
            PuntoExtres2=PuntoOs2;
            
        else:
            
            if(PuntoOs2<=PuntoFs2):
                        
                PuntoExtres2=PuntoFs2;
                        
            else:
                        
                PuntoExtres2=PuntoOs2;
        
        
        t = Symbol('t');
        
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
                                           
                                            try: 
                                           
                                                Posicion=float(eval(s2));
                                            
                                            except:
                                                
                                                Posicion=None;
                                                
                                            if Posicion==None:
                                                                       
                                                if bolInicio==True:
                                                
                                                    bolInicio=False;
                                                    
                                                    AlturaMax2=Posicion;
                                                    
                                                elif AlturaMax2<Posicion:
                                                    
                                                    AlturaMax2=Posicion;
                                                
        try:
                
            if AlturaMax2<PuntoExtres2:
                
                AlturaMax2=PuntoExtres2;
                
        except:
            
              AlturaMax2=PuntoExtres2;        
                                        

                        
        try:
                            
            print("La altura maxima del segundo objeto es: " + "%.2f "%(AlturaMax2)+" fts.");
                        
        except:
                            
            print("El objeto no tiene una altura maxima a traves del tiempo.");
                        
                          
        input("Pulsa Enter para continuar.");
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
           
        
        
            try:
                
                """Gv=plot((v1,(t,0,tiempo)),(v2,(t,0,tiempo)),show=False,xlabel='Tiempo (s)',ylabel='Velocidad (fts/s)');
                                 
                #Gv.annotations=[{'s':'Tienen la misma velocidad en: '+str(float(Mv[0]))+' s','xy':(1.5,-25),'size':'10','color':'black','ha':'center', 'va':'center'}];
                        
                Gv[0].line_color='r';
                        
                Gv.show();"""
                
                t = Symbol('t');
                Parsetv1='';
                Parsetv2='';
                
                v1=str(v1);
                v2=str(v2);
                
                try:
                    
                    v1 = float(v1);
                    
                except:
                    
                    Parsetv1 = lambdify(t,parse_expr(v1),'numpy');
                
                
                
                try:
                    
                    v2 = float(v2);
                    
                except:
                    
                    Parsetv2 = lambdify(t,parse_expr(v2),'numpy');
                
                
                
                
                def graphv1(x):
                    
                    if(type(v1) is float) == True:
                                        
                        return np.full(x.shape,v1);
                    
                    else:
                        
                        return Parsetv1(x);
                    
                    
                
                def graphv2(x):
                    
                    if(type(v2) is float) == True:
                                        
                        return np.full(x.shape,v2);
                    
                    else:
                        
                        return Parsetv2(x);
                
                
                
                Ranget=np.linspace(0,int(tiempo),num=500);
        
                plt.grid(True);
                plt.axhline(0, color="black");
                plt.axvline(0, color="black");
                plt.plot(Ranget,graphv1(Ranget),'r');
                plt.plot(Ranget,graphv2(Ranget),'b');
                plt.axis('auto');
                plt.ylabel('Velocidad (fts/s)');
                plt.xlabel('Tiempo (s)');
                plt.show();
                
            except:
                
                print("\nEs imposible obtener una grafica de las velocidades.");
        
            try:
                
                """Gva=plot((v1a,(t,0,tiempo)),(v2a,(t,0,tiempo)),show=False,xlabel='Tiempo (s)',ylabel='Rapidez (fts/s)');
                        
                
                #Gva.annotations=[{'s':'Tienen la misma rapidez en: '+str(float(Mr2[0]))+' s y '+str(float(Mr1[0]))+' s','xy':(1.75,25),'size':'10','color':'black','ha':'center', 'va':'center'}];
                        
                Gva[0].line_color='r';
                        
                Gva.show();"""
                
                t = Symbol('t');
                Parsetv1a='';
                Parsetv2a='';
                
                v1a=str(v1a);
                v2a=str(v2a);
                
                try:
                    
                    v1a = float(v1a);
                    
                except:
                    
                    Parsetv1a = lambdify(t,parse_expr(v1a),'numpy');
                
                
                
                try:
                    
                    v2a = float(v2a);
                    
                except:
                    
                    Parsetv2a = lambdify(t,parse_expr(v2a),'numpy');
                
                
                
                
                def graphv1a(x):
                    
                    if(type(v1a) is float) == True:
                                        
                        return np.full(x.shape,v1a);
                    
                    else:
                        
                        return Parsetv1a(x);
                    
                    
                
                def graphv2a(x):
                    
                    if(type(v2a) is float) == True:
                                        
                        return np.full(x.shape,v2a);
                    
                    else:
                        
                        return Parsetv2a(x);
                
                
                
                Ranget=np.linspace(0,int(tiempo),num=500);
        
                plt.grid(True);
                plt.axhline(0, color="black");
                plt.axvline(0, color="black");
                plt.plot(Ranget,graphv1a(Ranget),'r');
                plt.plot(Ranget,graphv2a(Ranget),'b');
                plt.axis('auto');
                plt.ylabel('Rapidez (fts/s)');
                plt.xlabel('Tiempo (s)');
                plt.show();
                

            except:
                
                print("\nEs imposible obtener una grafica de las rapideces.");
            
            
        input("Pulsa Enter para continuar.");
    






def Rotar():
    
    try:
        x1 = float(input("Introduzca el valor del primer punto en x: "));
        y1 = float(input("Introduzca el valor del primer punto en y: "));
        
        x2 = float(input("Introduzca el valor del segundo punto en x: "));
        y2 = float(input("Introduzca el valor del segundo punto en y: "));
        
        x3 = float(input("Introduzca el valor del tercer punto en x: "));
        y3 = float(input("Introduzca el valor del tercer punto en y: "));
        
        MatrizA=[[x1,y1],[x2,y2],[x3,y3]];    
        
        print("\nSu matriz original es:\n");
        
        for i in range(3):
            for j in range(2):
                print(MatrizA[i][j],end=" ");
                
            print();
        
        
        AnguloDe=float(input("Introduzca el angulo de rotacion en grados: "));
        
    except:
        
        print("\nError al introducir datos. Regresando...\n");
        time.sleep(2);
        
    else:
        
        Angulo=float((AnguloDe*pi)/180); #45 grados
        Rot=[[cos(Angulo),-1*sin(Angulo)],[sin(Angulo),cos(Angulo)]];
        
        MatrizARota=[
                    [(MatrizA[0][0]*Rot[0][0]+MatrizA[0][1]*Rot[1][0]),(MatrizA[0][0]*Rot[0][1]+MatrizA[0][1]*Rot[1][1])],
                    [(MatrizA[1][0]*Rot[0][0]+MatrizA[1][1]*Rot[1][0]),(MatrizA[1][0]*Rot[0][1]+MatrizA[1][1]*Rot[1][1])],
                    [(MatrizA[2][0]*Rot[0][0]+MatrizA[2][1]*Rot[1][0]),(MatrizA[2][0]*Rot[0][1]+MatrizA[2][1]*Rot[1][1])]
                    ];
        
        print("\nSu matriz rotada es:\n");
        
        for i in range(3):
            for j in range(2):
                print("%.2f "%(MatrizARota[i][j]),end=" ");
            
            print();
        
        input('Presione Enter para continuar ');


def Trasladar():
    
    try:
        x1 = float(input("Introduzca el valor del primer punto en x: "));
        y1 = float(input("Introduzca el valor del primer punto en y: "));
        
        x2 = float(input("Introduzca el valor del segundo punto en x: "));
        y2 = float(input("Introduzca el valor del segundo punto en y: "));
        
        x3 = float(input("Introduzca el valor del tercer punto en x: "));
        y3 = float(input("Introduzca el valor del tercer punto en y: "));
        
        MatrizA=[[x1,y1],[x2,y2],[x3,y3]];
        MatrizAA=[[x1,y1,1],[x2,y2,1],[x3,y3,1]];
        
        print("\nSu matriz original es:\n");
        
        for i in range(3):
            for j in range(2):
                print(MatrizA[i][j],end=' ');
            
            print();
        
        h = float(input("Introduzca la unidades de traslacion en x: "));
        k = float(input("Introduzca la unidades de traslacion en y: "));
    
    except:
    
        print("\nError al introducir datos. Regresando...\n");
        time.sleep(2);
    
    else:
        
        MatrizTras=[[1,0,0],[0,1,0],[h,k,1]];
        
        MatrizATras=[
                     [MatrizAA[0][0]*MatrizTras[0][0]+MatrizAA[0][1]*MatrizTras[1][0]+MatrizAA[0][2]*MatrizTras[2][0],
                      MatrizAA[0][0]*MatrizTras[0][1]+MatrizAA[0][1]*MatrizTras[1][1]+MatrizAA[0][2]*MatrizTras[2][1],
                      MatrizAA[0][0]*MatrizTras[0][2]+MatrizAA[0][1]*MatrizTras[1][2]+MatrizAA[0][2]*MatrizTras[2][2]],
                     
                     [MatrizAA[1][0]*MatrizTras[0][0]+MatrizAA[1][1]*MatrizTras[1][0]+MatrizAA[1][2]*MatrizTras[2][0],
                      MatrizAA[1][0]*MatrizTras[0][1]+MatrizAA[1][1]*MatrizTras[1][1]+MatrizAA[1][2]*MatrizTras[2][1],
                      MatrizAA[1][0]*MatrizTras[0][2]+MatrizAA[1][1]*MatrizTras[1][2]+MatrizAA[1][2]*MatrizTras[2][2]],
                    
                     [MatrizAA[2][0]*MatrizTras[0][0]+MatrizAA[2][1]*MatrizTras[1][0]+MatrizAA[2][2]*MatrizTras[2][0],
                      MatrizAA[2][0]*MatrizTras[0][1]+MatrizAA[2][1]*MatrizTras[1][1]+MatrizAA[2][2]*MatrizTras[2][1],
                      MatrizAA[2][0]*MatrizTras[0][2]+MatrizAA[2][1]*MatrizTras[1][2]+MatrizAA[2][2]*MatrizTras[2][2]],
                    ];
        
        RMatrizATras=[
                        [MatrizATras[0][0],MatrizATras[0][1]],
                        [MatrizATras[1][0],MatrizATras[1][1]],
                        [MatrizATras[2][0],MatrizATras[2][1]],
                      
                      ];
        
        print("\nSu matriz trasladada es:\n");
        
        for i in range(3):
            for j in range(2):
                print("%.2f "%(RMatrizATras[i][j]),end=' ');
            
            print();
            
        input('Presione Enter para continuar ');

def Escalacion():
    
    try:
        x1 = float(input("Introduzca el valor del primer punto en x: "));
        y1 = float(input("Introduzca el valor del primer punto en y: "));
        
        x2 = float(input("Introduzca el valor del segundo punto en x: "));
        y2 = float(input("Introduzca el valor del segundo punto en y: "));
        
        x3 = float(input("Introduzca el valor del tercer punto en x: "));
        y3 = float(input("Introduzca el valor del tercer punto en y: "));
        
        MatrizA=[[x1,y1],[x2,y2],[x3,y3]];
        MatrizAA=[[x1,y1,1],[x2,y2,1],[x3,y3,1]];
        
        print("\nSu matriz original es:\n");
        
        for i in range(3):
            for j in range(2):
                print(MatrizA[i][j],end=' ');
            
            print();
        
        Es = float(input("Introduzca la unidades de escalacion de la matriz: "));

    except:
        
        print("\nError al introducir datos. Regresando...\n");
        time.sleep(2);

    else:

        MatrizEsca=[[Es,0,0],[0,Es,0],[0,0,1]];
        
        MatrizAEsca=[
                     [MatrizAA[0][0]*MatrizEsca[0][0]+MatrizAA[0][1]*MatrizEsca[1][0]+MatrizAA[0][2]*MatrizEsca[2][0],
                      MatrizAA[0][0]*MatrizEsca[0][1]+MatrizAA[0][1]*MatrizEsca[1][1]+MatrizAA[0][2]*MatrizEsca[2][1],
                      MatrizAA[0][0]*MatrizEsca[0][2]+MatrizAA[0][1]*MatrizEsca[1][2]+MatrizAA[0][2]*MatrizEsca[2][2]],
                     
                     [MatrizAA[1][0]*MatrizEsca[0][0]+MatrizAA[1][1]*MatrizEsca[1][0]+MatrizAA[1][2]*MatrizEsca[2][0],
                      MatrizAA[1][0]*MatrizEsca[0][1]+MatrizAA[1][1]*MatrizEsca[1][1]+MatrizAA[1][2]*MatrizEsca[2][1],
                      MatrizAA[1][0]*MatrizEsca[0][2]+MatrizAA[1][1]*MatrizEsca[1][2]+MatrizAA[1][2]*MatrizEsca[2][2]],
                    
                     [MatrizAA[2][0]*MatrizEsca[0][0]+MatrizAA[2][1]*MatrizEsca[1][0]+MatrizAA[2][2]*MatrizEsca[2][0],
                      MatrizAA[2][0]*MatrizEsca[0][1]+MatrizAA[2][1]*MatrizEsca[1][1]+MatrizAA[2][2]*MatrizEsca[2][1],
                      MatrizAA[2][0]*MatrizEsca[0][2]+MatrizAA[2][1]*MatrizEsca[1][2]+MatrizAA[2][2]*MatrizEsca[2][2]],
                    ];
        
        RMatrizAEsca=[
                        [MatrizAEsca[0][0],MatrizAEsca[0][1]],
                        [MatrizAEsca[1][0],MatrizAEsca[1][1]],
                        [MatrizAEsca[2][0],MatrizAEsca[2][1]],
                      
                      ];
        
        
        print("\nSu matriz escalada es:\n");
        
        for i in range(3):
            for j in range(2):
                print("%.2f "%(RMatrizAEsca[i][j]),end=' ');
            
            print();
            
            
        input('Presione Enter para continuar ');


#get_ipython().magic('reset -f');

def Matrices():
    
    Seleccion=0;
    BolMaSalir=False;
    
    while BolMaSalir==False:
        
        #!cls;
        #get_ipython().magic('clear');
        #import os 
        #os.system('cls')
        print('\n\nMATRICES');
        print('\n1.Rotar una Matriz');
        print('\n2.Trasladar una Matriz');
        print('\n3.Escalar una Matriz');
        print('\n4.Salir');
        
        try:
            
           Seleccion=int(input('Ingrese una opcion: '));
            
        except:
            
            Seleccion=0;
            
        
        if Seleccion<1 or Seleccion>4:
                
            print("Opcion no valida, intentelo de nuevo.");
            time.sleep(2);
            
        elif Seleccion==4:
                
            print("Regresando...");
            BolMaSalir=True;
            time.sleep(2);
            
        elif Seleccion==3:
            
            Escalacion();
            
        elif Seleccion==2:
                
            Trasladar();
                
            
        elif Seleccion==1:
                
            Rotar();
            

def Presentacion():
    
    print('\n\n        Universiad Nacional de Ingenieria');
    print('\n      Facultad de Electronica y Computacion');
    print('\n         Matematicas I Para Computacion');
    print('Repaso General de curso usando Matlab, Octave o Python');
    print('                      1M1-CO');
    print('  Jurgen Francisco Bermudez Picado    2020-0290U');
    print('  María Gabriela Robleto Gutiérrez    2020-0429U');
    print('  Shania Joshua Levy Omier 		      2020-0494U');
    
    input('Presione Enter para continuar ');


def graph_function():
    
    global x
    limit_left = -10
    limit_right = 10
    
    bolSalir=False
    
    while bolSalir==False:
    
        try:
            
            #os.system('cls')
            print("\n\n\n\n\n\n\n\n\n\n\n\nIngrese la función a graficar en base a x:\n")
            equation = str(input('ƒ(x) = '))
            ParseEquation = ''
    
            try:
                
                equation = int(equation)
                
            except:
                
                ParseEquation = lambdify(x,parse_expr(equation),'numpy')
    
            def graph(x):
                
                #Si equation se cambio a entero, retorna esto
                if(type(equation) is int) == True:
                    
                    print("Es entero")
                    return np.full(x.shape,equation)
                
                else:
                    
                    return ParseEquation(x)
    
            """
            ParseEquation = parse_expr(equation)
            Numpyequation = lambdify(x,ParseEquation,'numpy')
    
            def graph(x):
                return Numpyequation(x)
            """
            
            xRange = np.linspace(limit_left,limit_right,num=500)
    
            plt.grid(True)
            plt.axhline(0, color="black")
            plt.axvline(0, color="black")
            
            try:
            
                plt.plot(xRange,graph(xRange),'g')
                plt.axis('auto')
                plt.title(f'ƒ(x) = {(equation)}')
                plt.ylabel('ƒ (x)')
                plt.show()
            
            except:
                
                print("\nEcuación incorrecta!")
                plt.show()
            
        except:
            
            print("\nEcuación incorrecta!")
        
        Leer='r'
            
        while Leer!='s'and Leer!='n':
        
            print('\nDesea Ingresar otra funcion?')
            Leer=input('(s/n) :')
            
            if Leer=='s':
                
                bolSalir=False
                
            elif Leer=='n':
                
                bolSalir=True
                
            
            
            
    

def limits():
    
    global x
    os.system('cls')
    x = Symbol('x')
    bolSalir=False
    
    while bolSalir==False:

        try:
            
            parseEquation = ''
            print("\n\n\n\n\n\n\n\n\n\n\n\n= = => Ingrese la función para calcular el límite <= = =\n")
            equation = str(input('ƒ(x) = '))
            parseEquation = parse_expr(equation)
            
            x=1
            
            InducirError=eval(str(parseEquation))
            
            x = Symbol('x')
            
            xValue = int(input("\nIngrese el valor de x: "))
    
            #parse_xValue = parse_expr(xValue)
            #Numpyequation = lambdify(parse_xValue,parseEquation,'numpy')
    
            lim = limit(parseEquation,x,xValue)
            print("\n=> El límite es: ",lim)
            
        except:
            
            print("\nError al introducir datos.\n")
            
        Leer='r'
            
        while Leer!='s'and Leer!='n':
        
            print('\nDesea Ingresar otra funcion?')
            Leer=input('(s/n) :')
            
            if Leer=='s':
                
                bolSalir=False
                
            elif Leer=='n':
                
                bolSalir=True



def limit_lat():
    
    global x
    os.system('cls')
    x = Symbol('x')
    bolSalir=False
    
    while bolSalir==False:
    
        try:
            
            print("\n\n\n\n\n\n\n\n\n\n\n\n= = => Ingrese la función para calcular el límite <= = =\n")
            equation = str(input('ƒ(x) = '))
            parseEquation = parse_expr(equation)
            
            x=1
            
            InducirError=eval(str(parseEquation))
            
            x = Symbol('x')
            
            
            xValue = int(input("\nIngrese el valor de x : "))
            #parse_xValue = parse_expr(xValue)
            sideValue = str(input("\nEscriba ( + ) si se aproxima por la derecha o ( - ) si se aproxima por la izquierda: "))
    
            #Numequation = lambdify(parse_xValue,parseEquation,'numpy')
            #parse_sideValue = parse_expr(sideValue)
    
            if sideValue == '+' or sideValue == '-':
                
                lim = limit(parseEquation,x,xValue,sideValue)
                print("\n=> El límite es: ",lim)
                
                
            else:
                
                print("\nError al introducir datos.\n")

        except:
            
            print("\nError al introducir datos.\n")

            
        Leer='r'
            
        while Leer!='s'and Leer!='n':
        
            print('\nDesea Ingresar otra funcion?')
            Leer=input('(s/n) :')
            
            if Leer=='s':
                
                bolSalir=False
                
            elif Leer=='n':
                
                bolSalir=True




def limits_menu():
    
    os.system('cls')
    bolLimites=False
    
    while bolLimites==False:
    
        print("\n\nLIMITES\n\n1.Calcular el límite de una función\n\n2.Calcular el límite de una función lateral\n\n3.Atrás\n\n")
        option = str(input("Indique la opcion: "))
    
        if option == '1':
            
            limits()
                    
        elif option == '2':
            
            limit_lat()
        
        elif option == '3':
            
            bolLimites=True
            print("Regresando...")
            time.sleep(2)
            
        else:
            
            os.system('cls')
            print("\nOpción invalida")
            time.sleep(2)




def Sintaxis():
    
    print('\nSINTAXIS DE ECUACIONES (Recuerde el uso correcto de parentesis)\n');
    print("Suma:           +");
    print("Resta:          -");
    print("Multiplicacion: *");
    print("Division:       /");
    print("Potencia:       **");
    print("Raiz:           sqrt(Argumento)");
    print("Logaritmo:      log(Argumento), ln(Argumento), lognum(Argumento)");
    print("Trigonometria:  sin(Argumento), cos(Argumento), tan(Argumento)");
    input('Presione Enter para continuar ');

    print('\nEJEMPLOS (Recuerde el uso correcto de parentesis)\n');
    print("Suma:           2+2=4");
    print("Resta:          2-2=0");
    print("Multiplicacion: 2*2=4");
    print("Division:       2/2=1");
    print("Potencia:       2**2=4");
    print("Raiz:           sqrt(4)=2");
    print("Logaritmo:      log(e)=1, ln(e)=1, log10(10)=1");
    print("Trigonometria:  sin(0)=0, cos(0)=1, tan(0)=0");
    input('Presione Enter para continuar ');
    


def Derivate():
    
    global x 
    x = Symbol('x')
    # x esta declarada como variable global al inicio del codigo solamente 
    # se le llama para ser utulizado
    
    os.system('cls')
    
    bolSalir=False
    
    while bolSalir==False:
    
        try:
            
            print("\n\n\n\n\n\n\n\n\n\n\n\n= = => Ingrese la función para calcular la derivada <= = =\n")
            y = str(input('ƒ(x) = '))
            
            parsey = parse_expr(y)
            
            x=1

            InducirError=eval(str(parsey))
            
            x = Symbol('x')
            
            derivada = diff(parsey,x)
            
            # Se convierte a variable del tipo ecuacion
            # a traves de la funcion parse_expr
            
            print("\n\nƒ'(x) = ", derivada)
            
            
        except:
            
            print("\nError al introducir datos.\n")

            
        Leer='r'
            
        while Leer!='s'and Leer!='n':
        
            print('\nDesea Ingresar otra funcion?')
            Leer=input('(s/n) :')
            
            if Leer=='s':
                
                bolSalir=False
                
            elif Leer=='n':
                
                bolSalir=True
    










bolMenuPrin=True;
Seleccion=0;

while bolMenuPrin==True:
    
    
    
    print('\nMENU PRINCIPAL\n');
    print('1.Matrices');
    print('2.Funciones');
    print('3.Limites');
    print('4.Derivadas');
    print('5.Aplicaciones de Derivadas');
    print('6.Presentacion');
    print('7.Ayuda-Sintaxis');
    print('8.Salir');
    
    try:
            
        Seleccion=int(input('Ingrese la opcion que desea: '));
            
    except:
            
        Seleccion=0;
            
        
    if Seleccion<1 or Seleccion>8:
                
        print("Opcion no valida, intentelo de nuevo.");
        time.sleep(2);
            
    elif Seleccion==1:
                
        Matrices();
            
    elif Seleccion==2:
            
        graph_function();
            
    elif Seleccion==3:
                
        limits_menu();
                
    elif Seleccion==4:
                
        Derivate();
        
    elif Seleccion==5:
                
        ApliDeriv();
    
    elif Seleccion==6: 
                
        Presentacion();
        
    elif Seleccion==7:
                
        Sintaxis()
        
    elif Seleccion==8:
                
        print("Saliendo...");
        bolMenuPrin=False;
        time.sleep(2);
    
    
    

