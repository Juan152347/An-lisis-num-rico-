# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 11:00:59 2021

@author: PC
"""
import scipy.interpolate as sc
import matplotlib.pyplot as plt 
from pylab import *

x = [4830000,5250000];
y = [1329190,1501474];
p = sc.lagrange(x,y);
print(p);
z = p(x);
plt.plot(z);
plt.show();
print(p(5000000));
x = [4410000,4830000,5250000];
y = [1165978,1329190,1501474];
p = sc.lagrange(x,y);
print(p);
z = p(x)
plt.plot(z);
plt.show();
print(p(5000000));
x = [4410000,4830000,5250000,5670000];
y = [1165978,1329190,1501474,1682830];
p = sc.lagrange(x,y);
print(p);
z = p(x);
plt.plot(z);
plt.show();
print(p(5000000));
print("diferencia entre cuota aproximada con polinomio de grado 1 y polinomio de grado 2")
print(1398924.0000000007-1397831.142857121);
print("diferencia entre cuota aproximada con polinomio de grado 1 y polinomio de grado 3")
print(1398924.0000000007-1397831.142856656);
