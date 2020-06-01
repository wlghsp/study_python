import numpy as np
from scipy import stats

np.random.seed(0)

#data_A = np.random.randint(0,100,10000)
data_B = np.random.normal(size=100)

mean = np.mean(data_B)
median = np.median(data_B)
mode = stats.mode(data_B)

print("평균값: ", mean.round(2))
print("중앙값: ", median)
print("최빈값 : {} ( {} ) ".format(mode[0][0], mode[1][0]))