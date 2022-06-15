import numpy as np
# 逐元運算(elementwise)-要相同等級陣列跟資料 要同樣的"shape"
# data1=np.array([3,2,10])
# data2=np.array([1,3,6])
# res = data1+data2
# print("+",res)
# res = data1-data2
# print("-",res)
# res = data1>data2
# print(res)
# res = data1==data2
# print("比較是否相等",res)

# 矩陣運算(matrix)
# data1 = np.array([
#   [1,3]
# ])  # 1x2
# data2 = np.array([
#   [2,-4,3],
#   [1,3,-1]
# ])  # 2x3
# res = data1.dot(data2) #內積 1x3 (data1 的後矩要跟data2的前矩對上)
# print(res)
# res = data1@data2 #也是內積
# print(res)
# res = np.outer(data1,data2) # 外積 2x6 [1x2 2x3]
# print(res)  #

# 統計運算(statistics)
# ndaarry 指多維陣列
# data=np.array([
#   [2,1,7],
#   [3,5,2]
# ])  # 2x3
# res=data.cumsum() #逐級累加 2+1+7+3+5+2
# print(res)
# res=data.cumsum(axis=0) # 針對欄 逐級累加 [2,1,7][5,6,9]→[2,1,7][2+3,1+5,7+2]
# print(res)

# res=data.sum(axis=0) #直欄相加 colume
# print(res)
# res=data.sum(axis=1) #橫列相加 row
# print(res)
# res=data.max(axis=0)  #針對直欄找最大值
# print(res)
# res=data.max(axis=1)  #針對橫列找最大值
# print(res)

# res=data.sum()
# print("總和",res)
# res=data.max()
# print("最大值",res)
# res=data.min()
# print("最小值",res)
# res=data.mean()
# print("平均數",res)
# res=data.std()
# print("標準差",res)