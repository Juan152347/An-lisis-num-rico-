# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 08:05:34 2021

@author: PC
"""

import numpy as np
import sympy as sp
from sympy.plotting import plot

x=np.array([1,1,2,2])
y=np.array([0,0,0.69,0.69])

dr=np.array([1,0.5])
dr2=np.array([0,-8])


mtr = np.array([[1,0,0,0,0],[1,0,0,0,0],[2,0.69,0,0,0],[2,0.69,0,0,0]])
it=0
it2=0

for i in range(2,5):#c
    it=it+1
    for j in range(0,4):#F
        if(j+it<4):
            if(mtr[j][0]==mtr[j+it][0]):
                mtr[j][i]=1/mtr[j][0]
            else:
                mtr[j][i]=(mtr[j+1][i-1]-mtr[j][i-1])/(mtr[j+it][0]-mtr[j][0])
                print(mtr[j+1][i-1],"-",mtr[j][i-1],"/",mtr[j+it][0],"-",mtr[j][0])
                print(j,"-",i)
    
            
print(mtr)



            
x = sp.Symbol("x")              
c = sp.Symbol("c")

fx = sp.log(x)

pli = 0+1*(x-1)-0.31*(x-1)**2+0.12*((x-1)**2)*(x-2)

err = int(sp.log(2)-pli.subs(x,2))
#print("{:.35f}".format(err))

p = plot(fx,(x,0,5),show=False,line_color="red")           
p1 =  plot(pli,(x,0,5),show=False)
p.append(p1[0])
p.show()
     
        
        
