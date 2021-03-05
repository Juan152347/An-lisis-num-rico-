# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 07:10:19 2021

@author: PC
"""

import sympy as sp

cont = 0
ac=0
errab=0.1 
print("Ingrese un n: ")
n = int(input())


for i in range(1,n+1):
    ac=ac+pow(i, 2)
    cont=cont+2
    
err = (errab/ac)*100



sum = (n*(n+1)*(2*n+1))/6

print(sum)
print("resultado: ",ac)
print("numero de operaciones: ",cont)
print("Error relativo porcentual: ",err)