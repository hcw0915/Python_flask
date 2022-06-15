import numpy as np
# 多維陣列的索引 Indexing
# 單維度的資料
# data=np.array([1,2,3,4])
# print(data[2])
# # 多維度的資料
# data=np.array([
#   [2,3,4],
#   [5,6,7]
# ])  #2x3
# print(data[0,1]) #3
# 多維陣列的切片 Slicing
# 單維度的切片
# data=np.array([2,3,4,5])
# print(data[0:2])
# print(data[1:])
# print(data[:2])
# # 多維度的切片
# data=np.array([
#   [0,1,2],[3,4,5],
#   [5,4,3],[2,1,0]
# ])  #2x2x3
# print(data[1:3,0:2])  #[[3,4],[5,4]]
# print(data[0:2,1])  #[1,4]
# 使用...代表全都要

# data=np.array([
#   [
#     [8,1,3],
#     [-5,5,2]
#   ],
#   [
#     [0,1,6],
#     [4,4,-3]
#   ]
# ])
# print(data[0,...])  #[[8 1 3][-5 5 2]]
# print(data[...,1:3])  #全部都要，每個陣列的 1、2號位置 [1:3]