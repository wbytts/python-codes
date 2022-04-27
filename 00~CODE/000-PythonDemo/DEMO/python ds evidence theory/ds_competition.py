import numpy as np

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
    d2 = (d1-min(d1))/(max(d1)-min(d1))
    d3 = d2/sum(d2)
    return d3

#%%
pr1 = 1
pr2 = 1
pr3 = 1
pr4 = 1
pr5 = 1
#%%
#m1 = [1,0,0]
#m2 = [0,1,0]
#m3 = [0.8,0.1,0.1]
#m4 = [0.8,0.1,0.1]
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
m1= [0.7,0.1,0.1 ,0.0 ,0.1 ]
m2= [0.0,0.5,0.2 ,0.1 ,0.2 ]
m3= [0.6,0.1,0.15,0.0 ,0.15]
m4=[0.55,0.1,0.1 ,0.15,0.1 ]
m5= [0.6,0.1,0.2 ,0.0 ,0.1 ]

#%%
# 证据矩阵
m = np.array([m1,m2,m3,m4,m5])
# 优先级矩阵
pr = np.array([pr1,pr2,pr3,pr4,pr5])
# 可信度向量
crd = crd(m)
#
discount_evidence = discount(m,pr,crd)




