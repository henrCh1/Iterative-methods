# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 15:27:38 2023

@author: 86319
"""
import numpy as np

# 初始化变量
x = np.zeros(4)  # 初始化解向量x为4维零向量
b = np.array([4, 12, 8, 34]) # 将长度为4的数组赋值给b
A = np.array([[5, -1, -1, -1], [-1, 10, -1, -1], [-1, -1, 5, -1], [-1, -1, -1, 10]]) # 将4x4的矩阵赋值给A

# 迭代次数
num_iter = 100

# 迭代开始前的初始化
max_diff = 1e-4  # 最大迭代误差
diff = np.zeros(4)  # 初始化每个未知数的迭代误差

# 执行高斯-塞德尔迭代
for i in range(num_iter):
    for j in range(4):
        # 保存旧的解向量x
        x_old = x.copy()
        # 计算第j个变量的新值
        x[j] = (b[j] - np.dot(A[j,:j], x[:j]) - np.dot(A[j,(j+1):], x[(j+1):]))/A[j,j]
        # 计算每个未知数的迭代误差
        diff[j] = np.abs(x[j] - x_old[j])
    # 判断是否已经收敛
    if np.max(diff) < max_diff:
        break

# 输出解向量x
print("结果为 ", x)
