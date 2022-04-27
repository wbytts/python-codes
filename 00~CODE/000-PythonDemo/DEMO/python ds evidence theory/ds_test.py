# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:32:06 2017

@author: Administrator
"""
import numpy as np


dm = np.ones((4,4))
a = np.array([[1,0,0],[0,1,0],[0.8,0.1,0.1],[0.8,0.1,0.1]])
#a = np.array([[0.5,0.2,0.3],[0.5,0.2,0.3],[0,0.9,0.1],[0.5,0.2,0.3]])
#a = np.array([[0.9,0.1,0],[0,0.1,0.9],[0.1,0.15,0.75],[0.1,0.15,0.75]])
for i in range(4):
    for j in range(4):
        dm[i,j]=np.linalg.norm(a[i]-a[j])
sm = (dm)/np.sqrt(2)/2+0.5
e  = 4*sm*(1-sm)
b = np.sum(e,axis=1)-1
c = sum(b)
d = b/c

aa = a.T
dd = np.sum(aa*d,axis=1)

ddd = (dd-min(dd))/(max(dd)-min(dd))
dddd = ddd/sum(ddd)
#%%
def crd(M):
    m,n = M.shape
    DM = np.ones((m,m))
    for i in range(m):
        for j in range(m):
            vec1 = M[i,:]
            vec2 = M[j,:]
            DM[i,j] =  np.linalg.norm(vec1 - vec2)
#    SM = ((np.sqrt(2) -DM)/np.sqrt(2))**2
    sm = (DM)/np.sqrt(2)/2+0.5
    e  = 4*sm*(1-sm)
    b = np.sum(e,axis=1)-1
    c = sum(b)
    crd = b/c
    return crd
#%%
def muti_row(m,k):
    row_num = len(k)
    p,q = m.shape
    l = np.ones((p,q))
    for i in range(row_num):
        l[i,:]=m[i,:]*k[i]
    return l
#%%
def discount(m,pr,crd):
    m_trans = m.T
    d1 = np.sum(m_trans*pr*crd,axis=1)
    d2 = (dd-min(dd))/(max(dd)-min(dd))
    d3 = ddd/sum(ddd)
    return d3

##%%
#pr1 = 0.53
#pr2 = 0.53
#pr3 = 0.85
#pr4 = 0.85
#
#m1 = [0.25, 0.15, 0.20, 0.40]
#m2 = [0.20, 0.35, 0.20, 0.25]
#m3 = [0.60, 0.15, 0.10, 0.15]
#m4 = [0.65, 0.10, 0.15, 0.10]
#%%
#pr1 = 0.86
#pr2 = 0.86
#pr3 = 0.45
#pr4 = 0.45
#
#m1 = [0.1,0.6,0.1,0.2]
#m2 = [0.1,0.7,0.1,0.1]
#m3 = [0.2,0.3,0.1,0.4]
#m4 = [0.2,0.25,0.35,0.2]
#%%
#pr1 = 0.40
#pr2 = 0.35
#pr3 = 0.60
#pr4 = 0.65
#
#m1 = [0.12,0.21,0.32,0.35]
#m2 = [0.35,0.06,0.29,0.30]
#m3 = [0.29,0.03,0.28,0.40]
#m4 = [0.05,0.20,0.43,0.32]
#%%
pr1 = 1
pr2 = 1
pr3 = 1
pr4 = 1
#%%
m1 = [1,0,0]
m2 = [0,1,0]
m3 = [0.8,0.1,0.1]
m4 = [0.8,0.1,0.1]
#%%
#m1=[0.5,0.2,0.3]
#m2=[0.5,0.2,0.3]
#m3=[0,0.9,0.1]
#m4=[0.5,0.2,0.3]
#%%
#m1=[0.9,0.1,0]
#m2=[0,0.1,0.9]
#m3=[0.1,0.15,0.75]
#m4=[0.1,0.15,0.75]
#%%
#m1= [0.7,0.1,0.1 ,0.0 ,0.1 ]
#m2= [0.0,0.5,0.2 ,0.1 ,0.2 ]
#m3= [0.6,0.1,0.15,0.0 ,0.15]
#m4=[0.55,0.1,0.1 ,0.15,0.1 ]
#m5= [0.6,0.1,0.2 ,0.0 ,0.1 ]
#%%
# 证据矩阵
m = np.array([m1,m2,m3,m4])
# 优先级矩阵
pr = np.array([pr1,pr2,pr3,pr4])
# 可信度向量
crd = crd(m)
#
discount_evidence = discount(m,pr)

#def BPA(m):
#    p,q = m.shape
#    b = np.ones(q)
#    for i in range(p):
#        b = b*m[i,:]
#    return b
#bpa = BPA(m)
#k = 1-np.sum(bpa)
##%%
#final = bpa+k*result
##%%
#A=set('A')
#B=set('B')
#C=set('C')
#D=set('ABC')
#a = []
#b = []
#c = []
#d = []
#
#m = [A,B,C,D]
#for num1,i in enumerate(m):
#    for num2, j in enumerate(m):
#        for num3, k in enumerate(m):
#            for num4, l in enumerate(m):
#                if i&j&k&l=={'A'}:
#                    print(num1,num2,num3,num4)
#                    a.append([num1,num2,num3,num4])
#                if i&j&k&l=={'B'}:
#                    print(num1,num2,num3,num4)
#                    b.append([num1,num2,num3,num4])
#                if i&j&k&l=={'C'}:
#                    print(num1,num2,num3,num4)
#                    c.append([num1,num2,num3,num4])
#                if i&j&k&l=={'A', 'B', 'C'}:
#                    print(num1,num2,num3,num4)
#                    d.append([num1,num2,num3,num4])
#
#a = np.array(a)
#b = np.array(b)
#c = np.array(c)
#d = np.array(d)
##%%
#def BPA2(meiju):
#    SUM = 0
#    for i in meiju:
#        SUM += m1[i[0]]*m2[i[1]]*m3[i[2]]*m4[i[3]]
#    return SUM
#
##%%
#ds_m1 = BPA2(a)
#ds_m2 = BPA2(b)
#ds_m3 = BPA2(c)
#ds_m4 = BPA2(d)
#bpa = [ds_m1,ds_m2,ds_m3,ds_m4]
#k= 1- sum(bpa)
##%%
#
#final = bpa + k*result

#%%
import numpy as np
dm = np.ones((4,4))
a = np.array([[1,0,0],[0,1,0],[0.8,0.1,0.1],[0.8,0.1,0.1]])
#a = np.array([[0.5,0.2,0.3],[0.5,0.2,0.3],[0,0.9,0.1],[0.5,0.2,0.3]])
#a = np.array([[0.9,0.1,0],[0,0.1,0.9],[0.1,0.15,0.75],[0.1,0.15,0.75]])
for i in range(4):
    for j in range(4):
        dm[i,j]=np.linalg.norm(a[i]-a[j])
sm = (1- dm)
b = np.sum(sm,axis=1)
c = sum(b)
d = b/c

aa = a.T
dd = np.sum(aa*d,axis=1)
ddd = (dd-min(dd))/(max(dd)-min(dd))
dddd = ddd/sum(ddd)

#%%
import numpy as np
dm = np.ones((5,5))
a = np.array(([0.7,0.1,0.1,0,0.1],[0,0.5,0.2,0.1,0.2],[0.6,0.1,0.15,0,0.15],[0.55,0.1,0.1,0.15,0.1],[0.6,0.1,0.2,0,0.1]))
for i in range(5):
    for j in range(5):
        dm[i,j]=np.linalg.norm(a[i]-a[j])
sm = (1- dm)
b = np.sum(sm,axis=1)
c = sum(b)
d = b/c

aa = a.T
dd = np.sum(aa*d,axis=1)
ddd = (dd-min(dd))/(max(dd)-min(dd))
dddd = ddd/sum(ddd)
#%%
p = np.linspace(10e-10,1,100)
h = -(p*np.log2(p)+(1-p)*np.log2(1-p))
gini  = 4*p*(1-p)
import matplotlib.pyplot as plt
plt.plot(p,h)
plt.plot(p,gini)
#%%
import numpy as np
dm = np.ones((4,4))
a = np.array([[1,0,0],[0,1,0],[0.8,0.1,0.1],[0.8,0.1,0.1]])
#a = np.array([[0.5,0.2,0.3],[0.5,0.2,0.3],[0,0.9,0.1],[0.5,0.2,0.3]])
#a = np.array([[0.9,0.1,0],[0,0.1,0.9],[0.1,0.15,0.75],[0.1,0.15,0.75]])
for i in range(4):
    for j in range(4):
        dm[i,j]=np.linalg.norm(a[i]-a[j])
sm = (dm)/np.sqrt(2)/2+0.5
e  = 4*sm*(1-sm)
b = np.sum(e,axis=1)-1
c = sum(b)
d = b/c

aa = a.T
dd = np.sum(aa*d,axis=1)

ddd = (dd-min(dd))/(max(dd)-min(dd))
dddd = ddd/sum(ddd)
#%%
import numpy as np
dm = np.ones((5,5))
a = np.array(([0.7,0.1,0.1,0,0.1],[0,0.5,0.2,0.1,0.2],[0.6,0.1,0.15,0,0.15],[0.55,0.1,0.1,0.15,0.1],[0.6,0.1,0.2,0,0.1]))
for i in range(4):
    for j in range(4):
        dm[i,j]=np.linalg.norm(a[i]-a[j])
sm = (dm)/np.sqrt(2)/2+0.5
e  = 4*sm*(1-sm)
b = np.sum(e,axis=1)-1
c = sum(b)
d = b/c

aa = a.T
dd = np.sum(aa*d,axis=1)
ddd = (dd-min(dd))/(max(dd)-min(dd))
dddd = ddd/sum(ddd)

