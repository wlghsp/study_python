# 딥러닝을 구동하는데 필요한 케라스 함수 호출
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 필요한 라이브러리 불러오기
import numpy as np
import tensorflow as tf

# 실행할 때마다 같은 결과를 출력하기 위해 설정하는 부분
np.random.seed(3)
tf.random.set_seed(3)

# 준비된 수술 환자 데이터를 불러오기
Data_set = np.loadtxt("/Users/jihochoi/downloads/deeplearning/dataset/ThoraricSurgery.csv", delimiter=",")

# 환자의 기록과 수술 결과를 X와 Y로 구분하여 저장
X = Data_set[:,0:17]
Y = Data_set[:,17]

# 딥러닝 구조르 결정(모델을 설정하고 실행)
model = Sequential()
model.add(Dense(30, input_dim=17, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 딥러닝 실행
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
model.fit(X,Y, epochs=100, batch_size=10)
