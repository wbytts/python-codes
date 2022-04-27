# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:32:06 2017

@author: Administrator
"""
import numpy as np
#%%
def crd(M):
    m,n = M.shape
    DM = np.ones((m,m))
    for i in range(m):
        for j in range(m):
            vec1 = M[i,:]
            vec2 = M[j,:]
            DM[i,j] =  np.linalg.norm(vec1 - vec2)
    SM = 1-DM
    sup = np.sum(SM,axis=1)
    crd = sup/np.sum(sup)
    return crd
#%%
def muti_row(m,k):
    print(k)
    row_num = len(k)
    p,q = m.shape
    l = np.ones((p,q))
    for i in range(row_num):
        l[i,:]=m[i,:]*k[i]
    return l
#%%
def discount(m,pr,crd):
    re1 = muti_row(m,pr)
    re2 = muti_row(re1,crd)
    re = np.sum(re2,axis=0)
    re_normal = re/np.sum(re)
    return re_normal
#%%
pr1 = 0.53
pr2 = 0.53
pr3 = 0.85
pr4 = 0.85

m1 = [0.25, 0.15, 0.20, 0.40]
m2 = [0.20, 0.35, 0.20, 0.25]
m3 = [0.60, 0.15, 0.10, 0.15]
m4 = [0.65, 0.10, 0.15, 0.10]
pro=np.array([0.4759,0.1715,0.1526,0.2000])
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
#prp=np.array([0.133,0.5251,0.1407,0.2012])
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
#
#pro =np.array([0.1894,0.1261,0.3376,0.3469])
#%%
# 证据矩阵
M1 = np.array([m1,m2])
M2 = np.array([m3,m4])
# 优先级矩阵
pr1 = np.array([pr1,pr2])
pr2 = np.array([pr3,pr4])
# 可信度向量
crd1 = crd(M1)
crd2 = crd(M2)
#
result1 = discount(M1,pr1,crd1)
#%%
result2 = discount(M2,pr2,crd2)

#%% 枚举所有的组合情况
A=set('A')
B=set('B')
C=set('C')
D=set('ABC')
a = []
b = []
c = []
d = []
m = [A,B,C,D]
for num1,i in enumerate(m):
    for num2, j in enumerate(m):
        if i&j=={'A'}:
            print(num1,num2)
            a.append([num1,num2])
        if i&j=={'B'}:
            print(num1,num2)
            b.append([num1,num2])
        if i&j=={'C'}:
            print(num1,num2)
            c.append([num1,num2])
        if i&j=={'A', 'B', 'C'}:
            print(num1,num2)
            d.append([num1,num2])

a = np.array(a)
b = np.array(b)
c = np.array(c)
d = np.array(d)

#%%
def BPA2(meiju):
    SUM = 0
    for i in meiju:
        SUM += m1[i[0]]*m2[i[1]]
    return SUM

#%%
m1 = result1
m2 = result2
ds_m1 = BPA2(a)
ds_m2 = BPA2(b)
ds_m3 = BPA2(c)
ds_m4 = BPA2(d)
bpa = [ds_m1,ds_m2,ds_m3,ds_m4]
k= 1- sum(bpa)
#%%
# IR/MMW fusion result
final = bpa + k*pro
print(final)