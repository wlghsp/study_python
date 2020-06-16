import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']= '2'


tf.compat.v1.set_random_seed(2020)
x = 1
y = 0
w = tf.random.normal([1],0,1)

import math

def sigmoid(x):
  return 1/(1 + math.exp(-x))

output = sigmoid(x * w)
print(output)

for i in range(1000):
  output = sigmoid(x * w )
  error = y - output
  w = w + x * 0.1 * error #경사하강법

  if i % 100 == 99:
    print("학습횟수:", i, "Error:", error,"예측결과:", output)
