#隨機模組
import random
#隨機選取
data=random.choice([1,4,5,6,6,63,7,23])
print(data)
data=random.sample([1,4,6,7,23,2],3)
print(data)
#隨機調換順序(洗牌)
data=[1,3,5,6,7]
random.shuffle(data)
print(data)
#隨機取得亂數
data=random.random()  #0~1的隨機亂數
print(data)
data=random.uniform(0.0,1.0)
print(data)
data=random.uniform(60,100) #60~100的隨機亂數
print(data)
data=random.normalvariate(100,10) #平均數為100,標準差為10的常態分佈
print(data)
data=random.normalvariate(0,5) #平均數為0，標準差為5的常態分佈
print(data)


#統計模組
import statistics as stat
data=stat.mean([1,3,5,67,2]) #取平均數
print(data)
data=stat.median([1,2,3,4,5,65,6666]) #取中位數
print(data)
data=stat.stdev([1,2,3,4,5,65,100]) #查數列標準差、常態分布
print(data)