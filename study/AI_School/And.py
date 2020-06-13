import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']= '2'

import numpy as np

x = np.array([1,1], [1,0], [0,1], [0,0])
y = np.array([1], [0], [0], [0])
w = tf.random.normal([2],0,1)
b = tf.random.normal([1],0,1)
b_x = 1

import math
def sigmoid(x):
  return 1/(1 + math.exp(-x))

for i in range(2000):
    error_sum = 0
    for j in range(4):
        output = sigmoid(np.sum(x[j]*w)+b_x*b)
        error = y[j][0] - output
        w = w + x[j] * 0.1 * error
        b = b + b_x * 0.1 * error
        error_sum += error

for i in range(4):
    print('X: ', x[i], 'Y: ', y[i], 'Output:', sigmoid(np.sum(x[i]*w)+b))
