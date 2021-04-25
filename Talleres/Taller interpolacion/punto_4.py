# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 21:39:10 2021

@author: PC
"""

import numpy as np
import sympy as sp
from math import factorial

from sympy.plotting import plot

def dif(a):
    if(a==1):
        return 1/3
    if(a==2):
        return 7
    
def difii(b):
    if(b==2):
        return 8

x=np.array([1,1,2,2])
y=np.array([0,0,0.69,0.69])

dr=np.array([1,0.5])
dr2=np.array([0,-8])


mtr = np.array([[1,2.7,0,0,0,0],[1,2.7,0,0,0,0],[2,6,0,0,0,0],[2,6,0,0,0,0],[2,6,0,0,0,0]])
it=0
it2=0

for i in range(2,6):#c
    it=it+1
    for j in range(0,5):#F
        if(j+it<5):
            if(mtr[j][0]==mtr[j+it][0]):
                if(it==1):
                    mtr[j][i]=dif(mtr[j][0])#todo bien

                else:
                    mtr[j][i]=difii(mtr[j][0])/factorial(mtr[j][0])
            else:
                mtr[j][i]=(mtr[j+1][i-1]-mtr[j][i-1])/(mtr[j+it][0]-mtr[j][0])
                print(mtr[j+1][i-1],"-",mtr[j][i-1],"/",mtr[j+it][0],"-",mtr[j][0])
                print(j,"-",i)
    
            
print(mtr)
            
x = sp.Symbol("x")              
c = sp.Symbol("c")



pli = 2.7+0.33333333*(x-1)+2.96666667*((x-1)**2)+0.73333333*((x-1)**2)*(x-2)-0.43333333*((x-1)**2)*((x-2)**2)



        
p1 =  plot(pli,(x,0,5))
