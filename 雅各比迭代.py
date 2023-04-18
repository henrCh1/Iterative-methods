# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 15:25:14 2023

@author: 86319
"""
#导入NumPy库

import numpy as np

#初始化变量

x = np.zeros(4) # 将长度为4的全零向量赋值给x
x_new = np.zeros(4) # 将长度为4的全零向量赋值给x_new
b = np.array([1, 2, 3, 4]) # 将长度为4的数组[1, 2, 3, 4]赋值给b
A = np.array([[10, 2, 1, 2], [1, 5, 1, 1], [2, 3, 10, 2], [1, 2, 2, 5]]) # 将4x4的矩阵赋值给A

#设置迭代次数
num_iter = 100

#定义变量

max_diff = 0.0001 # 当迭代结果之差的最大值小于0.0001时，停止迭代
diff = np.zeros(4) # 存储每次迭代结果之差的向量

#进行Jacobi迭代

for i in range(num_iter):
    for j in range(4):
    # 计算x_new中第j个元素的值
        x_new[j] = (b[j] - np.dot(A[j,:], x) + A[j,j]*x[j])/A[j,j]
    
    # 计算本次迭代与上次迭代之间的差
        diff = np.abs(x_new - x)
    
    # 如果迭代结果之差的最大值小于设定的阈值，停止迭代
    if np.max(diff) < max_diff:
        print(f"Converged after {i+1} iterations")
        break
    
    # 将x_new的值复制给x
    x = x_new.copy()

#输出结果

print("Solution: ", x) # 输出变量x的值作为方程Ax=b的解